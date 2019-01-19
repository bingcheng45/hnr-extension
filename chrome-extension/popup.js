// Wait for DOM to be ready
document.addEventListener('DOMContentLoaded', () => {
  const API_URL = 'http://localhost:5000/api/attack';

  const dropdownItems = document.getElementsByClassName('dropdown-item');

  function showView (views, viewToShow) {
    for (let view of views) {
      if (view.getAttribute('id') === viewToShow) {
        view.classList.remove('hide');
      } else {
        view.classList.add('hide');
      }
    }
  }

  for (let item of dropdownItems) {
    item.addEventListener('click', function (e) {
      document.getElementById('type').lastElementChild.innerText = this.getAttribute('data-label');
      showView(document.getElementsByClassName('view'), this.getAttribute('data-view'));
    });
  }

  // Handles dropdown list when clicked
  document.getElementById('dropdown').addEventListener('click', () => {
    const dropdownList = document.getElementById('dropdown-list');
    const shade = document.getElementById('shade');

    if (dropdownList.classList.contains('hide')) {
      shade.classList.remove('hide');
      dropdownList.classList.remove('hide');
    } else {
      shade.classList.add('hide');
      dropdownList.classList.add('hide');
    }
    // dropdownList.classList.contains('hide') ? dropdownList.classList.remove('hide') : dropdownList.classList.add('hide');;
  });

  // Submits textarea input to backend
  document.getElementById('generate-text-btn').addEventListener('click', async function () {
    let textInput;
    let requestSuccess = false;

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
     requestSuccess = true;
    } catch (err) {
      console.log(err);
    } finally {
      this.removeAttribute('disabled');
      textInput.removeAttribute('disabled');
      this.innerHTML = 'Generate';

      if (requestSuccess) {
        document.getElementById('dropdown').classList.add('hide');
        showView(document.getElementsByClassName('view'), 'results-view');
      }
    }
  });

  // Redirect user back to home page
  document.getElementById('convert-again-btn').addEventListener('click', function () {
    document.getElementById('dropdown').classList.remove('hide');
    showView(document.getElementsByClassName('view'), 'text-view');

  });
}, false);

// Convert text to image
function textToImage (text) {
  const ctx = document.createElement('CANVAS').getContext('2d');
  ctx.canvas.width = ctx.measureText(text).width;
  ctx.fillText(text, 0, 10);
  return ctx.canvas.toDataURL();
}