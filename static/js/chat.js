const input = document.getElementById('myInput');

function resizeInput() {
  input.style.height = 'auto';
  input.style.height = input.scrollHeight + 'px';
}

input.addEventListener('input', resizeInput);
