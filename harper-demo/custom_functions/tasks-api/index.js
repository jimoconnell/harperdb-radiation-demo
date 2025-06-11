module.exports = async (server) => {
  console.log(">> /api/tasks/stats custom function LOADED");

  server.get('/api/tasks/stats', async (req, res) => {
    const sql = 'SELECT completed FROM harper_demo.tasks';
    const response = await server.harperdb.query(sql);

    const total = response.length;
    const completed = response.filter(r => r.completed === true).length;
    res.send({ total, completed, pending: total - completed });
  });
};
