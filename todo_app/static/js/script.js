/* todo_app/static/js/script.js */

// Add event listener to the "Edit" buttons
const editButtons = document.querySelectorAll('.edit-btn');
editButtons.forEach((button) => {
  button.addEventListener('click', (event) => {
    const taskElement = event.target.closest('li');
    const taskId = taskElement.dataset.taskId;
    // Implement the logic to show an edit form or perform other actions for editing.
    // You can use AJAX or forms to handle the edit process.
  });
});

// Add event listener to the "Delete" buttons
const deleteButtons = document.querySelectorAll('.delete-btn');
deleteButtons.forEach((button) => {
  button.addEventListener('click', (event) => {
    const taskElement = event.target.closest('li');
    const taskId = taskElement.dataset.taskId;
    // Implement the logic to show a confirmation dialog for deletion.
    // You can use AJAX or forms to handle the delete process.
  });
});
