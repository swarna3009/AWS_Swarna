const express = require('express');
const app = express();

app.set('view engine', 'ejs');

const URL = process.env.API_URL || 'http://localhost:8000/api';

app.get('/', async (req, res) => {
    try {
        const response = await fetch(URL);
        const result = await response.json();

        console.log(result);
        res.render('index', result);
    } catch (err) {
        console.error(err);
        res.status(500).send('Internal Server Error');
    }
});

app.listen(3000, '0.0.0.0', () => {
    console.log('Docker listening on port 3000!');
});