<html>
<head>
	<link rel="stylesheet" href="estilos.css" type="text/css">
	<script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
	<script>
		$(document).ready(function(){
			$('#f1').hide();

			$('#btn1').click(function(){
				$('#f1').show();
			});
			$('#btn2').click(function(){
				$('#f1').hide();
			});
		});//main 
	</script>
	</head>
<body>
	<div class="panel-1" id="e1"><B>Control de alumnos<B></div>

    <div class="panel-1" id="f1">
    	<div class="panel-2" id="btn2">
	<form action="insertar.php" method="POST">
    <input type="text" name="idProd" size="5">
    <input type="text" name="nombre" size="2">
    <input type="text" name="precio" size="2">
    <input type="text" name="exis" size="2">
    <input type="submit" value="registrar"><br>
    <select name="cars" id="cars">
      <option value="volvo">Volvo</option>
      <option value="saab">Saab</option>
      <option value="mercedes">Mercedes</option>
      <option value="audi">Audi</option>
    </select>

  </form>
</div>
	<button id="btn1">Activar</button>
	<button id="btn2">Desactivar</button>
	<br>
</body>
</html>