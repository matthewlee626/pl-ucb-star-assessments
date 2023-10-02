const items = document.querySelectorAll('.item');
const dropzone = document.querySelector('.dropzone');

items.forEach(item => {
    item.addEventListener('dragstart', (e) => {
        e.dataTransfer.setData('text/plain', e.target.textContent);
    });
});

dropzone.addEventListener('dragover', (e) => {
    e.preventDefault();
});

dropzone.addEventListener('drop', (e) => {
    e.preventDefault();
    const data = e.dataTransfer.getData('text/plain');
    const newItem = document.createElement('div');
    newItem.textContent = data;
    dropzone.appendChild(newItem);
});