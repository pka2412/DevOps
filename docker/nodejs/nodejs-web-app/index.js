const express = require('express');
const app = express();
const port = 3000;

// Set EJS as the view engine
app.set('view engine', 'ejs');

// Middleware to parse incoming request bodies
app.use(express.urlencoded({ extended: true }));

// Serve static files from the 'public' directory
app.use(express.static('public'));

// Sample to-do list data
const todoList = [
  { id: 1, task: 'Buy groceries' },
  { id: 2, task: 'Finish project' },
];

// Route to render the to-do list
app.get('/', (req, res) => {
  res.render('index', { todoList });
});

// Route to add a new task
app.post('/add', (req, res) => {
  const newTask = req.body.task;
  const newId = todoList.length + 1;
  todoList.push({ id: newId, task: newTask });
  res.redirect('/');
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

