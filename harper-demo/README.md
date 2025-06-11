# HarperDB Demo

A simple Node.js app that connects to a local HarperDB instance. It provides two endpoints:

- `POST /add`: Inserts a task into the `harper_demo.tasks` table
- `GET /list`: Lists all tasks from the table

This project is part of an exploratory blog post. See the write-up here: https://mmdc.net/harperdb-first-impressions/

## Setup

```sh
npm install
node index.js
```
You’ll need a running HarperDB instance on localhost:9925 with:
	•	Schema: harper_demo
	•	Table: tasks (hash attribute: id)
