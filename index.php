<html>
<head>
	<link rel="stylesheet" href="estilos.css" type="text/css">
	<script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
	<script>
		function valid(){
			var x, y, res, op;
			x= document.getElementById("num1").value;
			y= document.getElementById("num2").value;
			op= document.getElementById("cars").value;

			if(x.value != ""){
				if(y.value != ""){
					if(op=="suma"){
						res=parseFloat(x)+parseFloat(y);
					}
					if(op=="resta"){
						res=parseFloat(x)-parseFloat(y);
					}
					if(op=="multiplicacion"){
						res=parseFloat(x)*parseFloat(y);
					}
					if(op=="division"){
						res=parseFloat(x)/parseFloat(y);
					}
				}
				else{
					alert("debe ingresar el segundo numero");
				}
			}
			else{
				alert("debe ingresar el primer numero");
			}
			document.getElementById("res").innerHTML=res;
		}
	</script>

	</style>
</head> 
	<body>
		<font size="5">
		<div class="panel-1" id="jsjs"> <B>Operaciones</B>
		<br>


		<select name="cars" id="cars">
			<font size="5">
			<option value="suma">suma</option>
			<option value="resta">resta</option>
			<option value="multiplicacion">multiplicacion</option>
			<option value="division">division</option>
		</select>
		<br>
		<br>
		<font size="5">

		<label for="num1"> numero1: </label>
		<input type="text"  size="2" id="num1">
		<label for="num2"> numero2: </label>
		<input type="text" size="2" id="num2">
		<br>
		<br>
		

		<button id="boton1" size="5" onclick="valid()">generar</button>
		<br>
		<br>
		<label for="res">resultado: <label id="res"></label> </label>
		</div>
</body>
</html>