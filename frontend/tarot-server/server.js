// server.js
const express = require('express');
const cors = require('cors');
const app = express();
const port = 5000;

app.use(cors()); // Для разрешения кросс-доменных запросов
app.use(express.json()); // Для работы с JSON в запросах

// Пример простого маршрута для проверки работы сервера
app.get('/', (req, res) => {
	res.send('Сервер работает!');
});

// Запуск сервера
app.listen(port, () => {
	console.log(`Сервер запущен на порту ${port}`);
});

const cards = require('./cards');

// Получение случайной карты
app.get('/api/random-card', (req, res) => {
	const randomIndex = Math.floor(Math.random() * cards.length);
	const randomCard = cards[randomIndex];
	res.json(randomCard);
});