import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Connect to the Redis server
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis Client Error', err);
});

async function main() {
  try {
    // Connect to the Redis server
    await client.connect();

    // Set a value and then display it
    await client.set('school', 'Holberton');
    const value1 = await client.get('school');
    console.log(value1);

    // Set another value and display it
    await client.set('school', 100);
    const value2 = await client.get('school');
    console.log(value2);
  } catch (err) {
    console.error(err);
  } finally {
    // Close the client after all operations are done
    await client.quit();
  }
}

main();
