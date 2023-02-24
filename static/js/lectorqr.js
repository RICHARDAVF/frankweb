const video = document.getElementById('qr-video');

// Pedir acceso a la cámara
navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } })
  .then(stream => {
    video.srcObject = stream;
  })
  .catch(error => {
    console.error(error);
  });
const canvas = document.createElement('canvas');
const ctx = canvas.getContext('2d');
let canvasStream;
    
video.addEventListener('loadedmetadata', () => {
canvas.width = video.videoWidth;
canvas.height = video.videoHeight;
canvasStream = canvas.captureStream();
});
video.addEventListener('play', () => {
    function step() {
      ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
      const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
      const code = jsQR(imageData.data, imageData.width, imageData.height);
      if (code) {
        fetch(`/search_person/?q=${code.data}`)
        .then(response => response.json())
        .then(data => {
        const person = data.data[0];
        document.getElementById("nombre").value = person.nombre || "";
        document.getElementById("apellidos").value = person.apellidos || "";
        });
        document.getElementById("dni").value = code.data || '';
        // Detener la cámara y hacer lo que sea necesario con el código QR encontrado
        video.pause();
        canvasStream.getTracks()[0].stop();
      } else {
        requestAnimationFrame(step);
      }
    }
    requestAnimationFrame(step);
  });
   