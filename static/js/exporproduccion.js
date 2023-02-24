document.getElementById('export-to-excel-produccion').addEventListener('click', function() {
    var fecha = new Date();
    var nombreFecha = fecha.getFullYear() + "-" + (fecha.getMonth() + 1);
    var wb = XLSX.utils.table_to_book(document.getElementById('produccion'), { sheet: "Sheet 1" });
    XLSX.writeFile(wb, "Producion-" + nombreFecha + ".xlsx");
   
  });
