// Wait for DOM to be ready
document.addEventListener('DOMContentLoaded', () => {
  const API_URL = 'http://localhost:5000/api/attack';

  const dropdownItems = document.getElementsByClassName('dropdown-item');




  const header = document.getElementById("header");
  header.addEventListener("click", function(event) {
    copyTextToClipboard("Bob");
  });
  function copyTextToClipboard(text) {
    if (!navigator.clipboard) {
      fallbackCopyTextToClipboard(text);
      return;
    }
    navigator.clipboard.writeText(text).then(
      function() {
        console.log("Async: Copying to clipboard was successful!");
      },
      function(err) {
        console.error("Async: Could not copy text: ", err);
      }
    );
  }





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
      
      textInput = document.getElementById('text');
      console.log(textInput);
      imageElem = document.getElementById('image');
      var image = new Image();
      image.src = imageElem;
      console.log(imageElem.src);
      // Split the base64 string in data and contentType
var block = imageElem.src.split(";");
// Get the content type of the image
var contentType = block[0].split(":")[1];// In this case "image/gif"
// get the real base64 content of the file
var realData = block[1].split(",")[1];// In this case "R0lGODlhPQBEAPeoAJosM...."
console.log(realData);

// Convert it to a blob to upload
var blob = b64toBlob(realData, contentType);
// // Create a FormData and append the file with "image" as parameter name
// var formDataToUpload = new FormData(form);
// formDataToUpload.append("image", blob);
// console.log(formDataToUpload);
      
var link = document.createElement('a');
        console.log(blob);
        


        link.href = window.URL.createObjectURL(blob);
        link.download = 'test.png';

        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);



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

// ************************ Drag and drop ***************** //
let dropArea = document.getElementById("drop-area")

  // Prevent default drag behaviors
  ;['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false)
    document.body.addEventListener(eventName, preventDefaults, false)
  })

  // Highlight drop area when item is dragged over it
  ;['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, highlight, false)
  })

  ;['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, unhighlight, false)
  })

// Handle dropped files
dropArea.addEventListener('drop', handleDrop, false)

function preventDefaults(e) {
  e.preventDefault()
  e.stopPropagation()
}

function highlight(e) {
  dropArea.classList.add('highlight')
}

function unhighlight(e) {
  dropArea.classList.remove('active')
}

function handleDrop(e) {
  var dt = e.dataTransfer
  var files = dt.files

  handleFiles(files)
}

let uploadProgress = []
let progressBar = document.getElementById('progress-bar')

function initializeProgress(numFiles) {
  progressBar.value = 0
  uploadProgress = []

  for (let i = numFiles; i > 0; i--) {
    uploadProgress.push(0)
  }
}

function updateProgress(fileNumber, percent) {
  uploadProgress[fileNumber] = percent
  let total = uploadProgress.reduce((tot, curr) => tot + curr, 0) / uploadProgress.length
  console.debug('update', fileNumber, percent, total)
  progressBar.value = total
}

function handleFiles(files) {
  console.log(files);
  files = [...files]
  initializeProgress(files.length)
  files.forEach(uploadFile)
  files.forEach(previewFile)
}

function previewFile(file) {
  let reader = new FileReader()
  reader.readAsDataURL(file)
  reader.onloadend = function () {
    let img = document.createElement('img')
    img.src = reader.result
    console.log(img.src);
    var clipboardData = window.clipboardData;
    clipboardData.setData('text', 'copied some text!');
    document.getElementById('gallery').appendChild(img)
  }
  var blob = new Blob([file], { type: 'application/pdf' });
        var link = document.createElement('a');
        console.log(blob);
        link.href = window.URL.createObjectURL(blob);
        link.download = 'test.png';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
}

function uploadFile(file, i) {
  var url = 'http://localhost:5000/api/attack'
  var xhr = new XMLHttpRequest()
  var formData = new FormData()
  xhr.open('POST', url, true)
  xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest')

  // Update progress (can be used to show progress indicator)
  xhr.upload.addEventListener("progress", function (e) {
    updateProgress(i, (e.loaded * 100.0 / e.total) || 100)
  })

  xhr.addEventListener('readystatechange', function (e) {
    if (xhr.readyState == 4 && xhr.status == 200) {
      updateProgress(i, 100) // <- Add this
    }
    else if (xhr.readyState == 4 && xhr.status != 200) {
      // Error. Inform the user
    }
  })

  formData.append('upload_preset', 'ujpu6gyk')
  formData.append('file', file)
  console.log(formData);
  xhr.send(formData)
}


var control = document.getElementById("fileElem");
control.addEventListener("change", function (event) {

  // When the control has changed, there are new files


  files = control.files,
    len = files.length;
  handleFiles(files);
  for (var i = 0; i < len; i++) {

    console.log("Filename: " + files[i].name);
    console.log("Type: " + files[i].type);
    console.log("Size: " + files[i].size + " bytes");
  }

}, false);

// ?text to image?
var tCtx = document.getElementById('textCanvas').getContext('2d'),
    imageElem = document.getElementById('image');

document.getElementById('text').addEventListener('keyup', function (){
    tCtx.canvas.width = tCtx.measureText(this.value).width;
    tCtx.fillText(this.value, 0, 10);
    imageElem.src = tCtx.canvas.toDataURL();
    console.log(imageElem.src);
}, false);

function b64toBlob(b64Data, contentType, sliceSize) {
  contentType = contentType || '';
  sliceSize = sliceSize || 512;

  var byteCharacters = atob(b64Data);
  var byteArrays = [];

  for (var offset = 0; offset < byteCharacters.length; offset += sliceSize) {
      var slice = byteCharacters.slice(offset, offset + sliceSize);

      var byteNumbers = new Array(slice.length);
      for (var i = 0; i < slice.length; i++) {
          byteNumbers[i] = slice.charCodeAt(i);
      }

      var byteArray = new Uint8Array(byteNumbers);

      byteArrays.push(byteArray);
  }

var blob = new Blob(byteArrays, {type: contentType});
return blob;
}