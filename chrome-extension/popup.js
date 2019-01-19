// Wait for DOM to be ready
document.addEventListener('DOMContentLoaded', () => {
  const API_URL = 'http://localhost:5000/api/attack';

  const dropdownItems = document.getElementsByClassName('dropdown-item');

  for (let item of dropdownItems) {
    item.addEventListener('click', function (e) {
      document.getElementById('type').lastElementChild.innerText = this.getAttribute('data-label');

      const views = document.getElementsByClassName('view');
      const viewToRender = this.getAttribute('data-view');
      
      for (let view of views) {
        if (view.getAttribute('id') === viewToRender) {
          view.classList.remove('hide');
        } else {
          view.classList.add('hide');
        }
      }
    });
  }

  // Handles dropdown list when clicked
  document.getElementById('dropdown').addEventListener('click', () => {
    const dropdownList = document.getElementById('dropdown-list');

    dropdownList.classList.contains('hide') ? dropdownList.classList.remove('hide') : dropdownList.classList.add('hide');;
  });

  // Submits textarea input to backend
  document.getElementById('generate-text-btn').addEventListener('click', async function () {
    let textInput;

    try {
      console.log('start');
      textInput = document.getElementById('text');

      this.setAttribute('disabled', true);
      textInput.setAttribute('disabled', true);
      this.innerHTML = 'Generating...';
  
      /*
      // make async call to call server
      const resp = await fetch(API_URL, {
        method: 'POST',
        cache: 'no-cache'
      });
      */

    } catch (err) {
      console.log(err);
    } finally {
      this.removeAttribute('disabled');
      textInput.removeAttribute('disabled');
      this.innerHTML = 'Generate';
    }
  });
}, false);

// Convert text to image
function textToImage (text) {
  const ctx = document.createElement('CANVAS').getContext('2d');
  ctx.canvas.width = ctx.measureText(text).width;
  ctx.fillText(text, 0, 10);
  return ctx.canvas.toDataURL();
}