// Wait for DOM to be ready
document.addEventListener('DOMContentLoaded', () => {
  const dropdownItems = document.getElementsByClassName('dropdown-item');

  for (let item of dropdownItems) {
    item.addEventListener('click', function (e) {
      document.getElementById('type').lastElementChild.innerText = this.getAttribute('data-label');
    });
  }

  // Handles dropdown list when clicked
  document.getElementById('dropdown').addEventListener('click', () => {
    const dropdownList = document.getElementById('dropdown-list');

    dropdownList.classList.contains('hide') ? dropdownList.classList.remove('hide') : dropdownList.classList.add('hide');;
  });

  // Submits textarea input to backend
  document.getElementById('generate-text-btn').addEventListener('click', () => {
    const textInput = document.getElementById('text');

  });
}, false);

// Convert text to image
function textToImage (text) {
  const ctx = document.createElement('CANVAS').getContext('2d');
  ctx.canvas.width = ctx.measureText(text).width;
  ctx.fillText(text, 0, 10);
  return ctx.canvas.toDataURL();
}