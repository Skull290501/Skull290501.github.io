<html>
<head>
	<link rel="stylesheet" href="estilos.css" type="text/css">
	<script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
	<style>
		}
		table{
			margin-left: auto;
			margin-right: auto;
			text-align: center;
		}
	</style>
	<script>
		$(document).ready(function(){

			$('#btn1').click(function(){
				var cad1;
				var cad2;
				var cad3;
				var cad4;
				var cad5;
				var rfc;

				cad1= $('#nombre').val().substring(0,1);
				cad2= $('#appa').val().substring(0,2);
				cad3= $('#apma').val().substring(0,1);
				cad4= $('#nacimi').val().substring(2,4);
				cad6= $('#nacimi').val().substring(5,7);
				cad5= $('#nacimi').val().substring(8,10);
				rfc=cad2+cad3+cad1+cad4+cad6+cad5+"R7A";
				$('#res').val(rfc.toUpperCase());
			});

		$('#btn2').click(function(){
			$.ajax({
				url: "https://jsonplaceholder.typicode.com/users/"+$('#idU').val(),
				method: "GET",
				success: function(data){
				    $('#nom').val(data.name);
				    $('#em').val(data.email);	
				    $('#cel').val(data.phone);	
				}
			} );
		} );
			});		
	//main    
	</script>         
	</head>
<body>
	<table border="0" class="center">
		<tr>	
	<div class="panel-1" id="x1">
		id: <input type="text" id="idU" size="10">
		<button id="btn2">Consultar Api Rest</button><br>
		<br>
		Nombre: <input type="text" id="nom" size="25">
		<br>
		Email: <input type="text" id="em" size="25">
		<br>
		Telefono: <input type="text" id="cel" size="25">
	</div>
    </tr>
	<font size="5">
	<tr>	
	<div class="panel-3" id="e1"><B>Control de alumnos<B>
    nombre: <input type="text" id="nombre" size="13"><br>
    apellido pat: <input type="text" id="appa" size="13"><br>
    apellido mat: <input type="text" id="apma" size="13"><br>
    fech nac: <input type="date" id="nacimi" size="13"><br>
    rfc: <input type="text" id="res" size="15"> <button id="btn1">obtener</button><br>
    </div>
    </tr>
 </table>
</body>
</html>