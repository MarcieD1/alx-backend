import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';
import kue from 'kue';

const app = express();
const port = 1245;

const client = createClient();
const getAsync = promisify(client.get).bind(client);
const queue = kue.createQueue();

let reservationEnabled = true;

function reserveSeat(number) {
    client.set('available_seats', number);
}

async function getCurrentAvailableSeats() {
    const seats = await getAsync('available_seats');
    return parseInt(seats, 10);
}

// Initialize available seats to 50
reserveSeat(50);

app.get('/available_seats', async (req, res) => {
    const numberOfAvailableSeats = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', (req, res) => {
    if (!reservationEnabled) {
        return res.json({ status: 'Reservation are blocked' });
    }

    const job = queue.create('reserve_seat').save((err) => {
        if (err) {
            return res.json({ status: 'Reservation failed' });
        }
        res.json({ status: 'Reservation in process' });
    });

    job.on('complete', () => {
        console.log(`Seat reservation job ${job.id} completed`);
    }).on('failed', (err) => {
        console.log(`Seat reservation job ${job.id} failed: ${err}`);
    });
});

app.get('/process', (req, res) => {
    res.json({ status: 'Queue processing' });

    queue.process('reserve_seat', async (job, done) => {
        const availableSeats = await getCurrentAvailableSeats();

        if (availableSeats <= 0) {
            reservationEnabled = false;
            return done(new Error('Not enough seats available'));
        }

        reserveSeat(availableSeats - 1);

        if (availableSeats - 1 === 0) {
            reservationEnabled = false;
        }

        done();
    });
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
