const dni = document.getElementById('dni');
dni.addEventListener('input', function() {
  const query = dni.value.trim();
  
  if (query) {
    fetch(`/search_person/?q=${query}`)
      .then(response => response.json())
      .then(data => {
          const person = data.data[0];
          document.getElementById("nombre").value = person.nombre || "";
          document.getElementById("apellidos").value = person.apellidos || "";
      });
  } 
});