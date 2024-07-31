import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;

const listProducts = [
    { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
    { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

const client = createClient();
const getAsync = promisify(client.get).bind(client);

function getItemById(id) {
    return listProducts.find(product => product.id === id);
}

async function getCurrentReservedStockById(itemId) {
    const stock = await getAsync(`item.${itemId}`);
    return stock ? parseInt(stock, 10) : 0;
}

function reserveStockById(itemId, stock) {
    client.set(`item.${itemId}`, stock);
}

app.get('/list_products', (req, res) => {
    res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId, 10);
    const product = getItemById(itemId);
    if (!product) {
        return res.json({ status: 'Product not found' });
    }
    const currentQuantity = await getCurrentReservedStockById(itemId);
    res.json({ ...product, currentQuantity });
});

app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId, 10);
    const product = getItemById(itemId);
    if (!product) {
        return res.json({ status: 'Product not found' });
    }
    const currentQuantity = await getCurrentReservedStockById(itemId);
    if (currentQuantity <= 0) {
        return res.json({ status: 'Not enough stock available', itemId });
    }
    reserveStockById(itemId, currentQuantity - 1);
    res.json({ status: 'Reservation confirmed', itemId });
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
