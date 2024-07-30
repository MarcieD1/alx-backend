# Redis Queuing System in Node.js

This project demonstrates how to use Redis with Node.js to perform basic and advanced operations. It includes setting up a Redis server, connecting to it using a Node.js client, and performing various operations such as setting and getting values, and working with hashes.

## Prerequisites

- Node.js
- npm (Node Package Manager)
- Redis

## Installation

### Redis

1. **Download, extract, and compile Redis**:
   ```sh
   wget http://download.redis.io/releases/redis-6.0.10.tar.gz
   tar xzf redis-6.0.10.tar.gz
   cd redis-6.0.10
   make
   ```

2. **Start Redis in the background**:
   ```sh
   src/redis-server &
   ```

3. **Verify Redis is working**:
   ```sh
   src/redis-cli ping
   ```

4. **Set and get a value in Redis**:
   ```sh
   src/redis-cli set Holberton "School"
   src/redis-cli get Holberton
   ```

5. **Save the data to create `dump.rdb`**:
   ```sh
   src/redis-cli save
   ```

6. **Copy `dump.rdb` to the project root**:
   ```sh
   cp dump.rdb /home/mdes2019/alx-backend/0x03-queuing_system_in_js
   ```

### Node.js

1. **Install dependencies**:
   ```sh
   npm install redis
   ```

## Usage

### 0. Redis Client

Create a file named `0-redis_client.js`:

```javascript
import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
```

Run the script:

```sh
npm run dev 0-redis_client.js
```

### 1. Redis Client and Basic Operations

Create a file named `1-redis_op.js`:

```javascript
import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
```

Run the script:

```sh
npm run dev 1-redis_op.js
```

### 2. Redis Client and Async Operations

Create a file named `2-redis_op_async.js`:

```javascript
import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

const getAsync = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  const value = await getAsync(schoolName);
  console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
```

Run the script:

```sh
npm run dev 2-redis_op_async.js
```

### 3. Redis Client and Advanced Operations

Create a file named `4-redis_advanced_op.js`:

```javascript
import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

function createHash() {
  client.hset('HolbertonSchools', 'Portland', 50, redis.print);
  client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
  client.hset('HolbertonSchools', 'New York', 20, redis.print);
  client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
  client.hset('HolbertonSchools', 'Cali', 40, redis.print);
  client.hset('HolbertonSchools', 'Paris', 2, redis.print);
}

function displayHash() {
  client.hgetall('HolbertonSchools', (err, reply) => {
    console.log(reply);
  });
}

createHash();
displayHash();
```

Run the script:

```sh
npm run dev 4-redis_advanced_op.js
```

## License

This project is licensed under the MIT License.
```

This `README.md` file provides a comprehensive guide on how to set up and run your Redis queuing system project in Node.js.
