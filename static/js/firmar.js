let isDrawing = false;

function drawOnCanvas(event) {
  if (!isDrawing) {
    return;
  }
  const canvas = document.getElementById("canvas");
  const ctx = canvas.getContext("2d");
  ctx.lineTo(event.offsetX, event.offsetY);
  ctx.stroke();
}

function startDrawing(event) {
  isDrawing = true;
  const canvas = document.getElementById("canvas");
  const ctx = canvas.getContext("2d");
  ctx.beginPath();
  ctx.moveTo(event.offsetX, event.offsetY);
}

function stopDrawing() {
  isDrawing = false;
}

document.getElementById("canvas").addEventListener("mouseup", stopDrawing);
document.getElementById("canvas").addEventListener("mouseleave", stopDrawing);

function clearCanvas() {
  const canvas = document.getElementById("canvas");
  const ctx = canvas.getContext("2d");
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}
function saveImage() {
    var csrf_token = $("#csrf_token").val();  
    var image = canvas.toDataURL("image/png").replace(/^data:image\/(png|jpg);base64,/, "");
    var dni = document.getElementById("formulario2").elements.dni.value;
    // Send POST request to server to save the image
    $.ajax({
        url: "/guardar_firma/",
        type: "POST",
        data: { image_b64: image, csrfmiddlewaretoken: csrf_token,dni:dni}
       
    });
}
