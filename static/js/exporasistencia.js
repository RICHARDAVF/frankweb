document.getElementById('export-to-excel-asistencia').addEventListener('click', function() {
    var fecha = new Date();
    var nombreFecha = fecha.getFullYear() + "-" + (fecha.getMonth() + 1) + "-" + fecha.getDate();
    var wb = XLSX.utils.table_to_book(document.getElementById('asistencia'), { sheet: "Sheet 1" });
    XLSX.writeFile(wb, "Asistencia-" + nombreFecha + ".xlsx");
   
  });
