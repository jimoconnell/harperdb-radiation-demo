const express = require('express');
const axios = require('axios');
const app = express();
const port = 3000;

app.use(express.json());
app.use(express.static('public'));

const HARPERDB_URL = 'https://your-cloud-url.harperdbcloud.com';
const HARPERDB_AUTH = {
  username: 'user',
  password: 'password',
};

// Add task
app.post('/add', async (req, res) => {
  try {
    const data = req.body;

    const response = await axios.post(HARPERDB_URL, {
      operation: 'insert',
      schema: 'tasks',
      table: 'tasks',
      records: [data],
    }, {
      auth: HARPERDB_AUTH,
    });

    res.json(response.data);
  } catch (err) {
    console.error(err.response?.data || err.message);
    res.status(500).send('Error inserting into tasks table');
  }
});

// Add radiation reading
app.post('/radiation', async (req, res) => {
  try {
    const data = req.body;

    const response = await axios.post(HARPERDB_URL, {
      operation: 'insert',
      schema: 'tasks',
      table: 'radiation',
      records: [data],
    }, {
      auth: HARPERDB_AUTH,
    });

    res.json(response.data);
  } catch (err) {
    console.error(err.response?.data || err.message);
    res.status(500).send('Error inserting into radiation table');
  }
});
app.get('/radiation/list', async (req, res) => {
  try {
    const response = await axios.post(HARPERDB_URL, {
      operation: 'sql',
      sql: 'SELECT * FROM tasks.radiation ORDER BY timestamp DESC LIMIT 100',
    }, {
      auth: HARPERDB_AUTH,
    });

    res.json(response.data);
  } catch (err) {
    console.error(err.message);
    res.status(500).send('Error reading from radiation table');
  }
});
// List tasks
app.get('/list', async (req, res) => {
  try {
    const response = await axios.post(HARPERDB_URL, {
      operation: 'sql',
      sql: 'SELECT * FROM tasks.tasks',
    }, {
      auth: HARPERDB_AUTH,
    });

    res.json(response.data);
  } catch (err) {
    console.error(err.message);
    res.status(500).send('Error reading from tasks table');
  }
});
app.listen(port, () => {
	  console.log(`Server running at http://localhost:${port}`);
});
