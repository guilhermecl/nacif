import { useState, useEffect } from 'react';
import axios from 'axios';

export default function Todos() {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    axios
      .get('/todos/', { headers: { Authorization: `Bearer ${localStorage.getItem('token')}` } })
      .then(res => setTodos(res.data))
      .catch(err => alert('Error fetching todos: ' + err.message));
  }, []);

  return (
    <div>
      <h2>Your Todos</h2>
      <ul>
        {todos.map(t => (
          <li key={t.id}>
            {t.title} - {new Date(t.due_date).toLocaleString()}
          </li>
        ))}
      </ul>
    </div>
  );
}