<html>
<head>
	<link rel="stylesheet" href="estilos.css" type="text/css">
	<script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
      
	</head>
<body>
	<font size="5">
	 <div class="panel-1"style="max-width: 700px;">

        <div class="text-center" style="margin: 20px 0px 20px 0px;">
            <span class="text-secondary">REGISTRO DE JUGADORES</span>
        </div>
        <form method="post" action="">
            <div class="row">
                <div class="col-lg-12">
                    <div id="inputFormRow">
                        <div class="input-group mb-3">
                            <input type="text" name="title[]" class="form-control m-input" placeholder="Ingresar jugador" autocomplete="off">
                            <div class="input-group-append">
                                <button id="elimFila" type="button" class="btn btn-danger">Eliminar</button>
                                <br>
                                
                            </div>
                        </div>
                    </div>
                    <br>
                    <div id="newRow"></div>
                    <button id="nuevaFila" type="button" class="btn btn-info">Agregar jugador</button>
                    <br>
                    <br>
                </div>
            </div>
        </form>
    </div>

    <script type="text/javascript">
        // add row
        $("#nuevaFila").click(function () {
            var html = '';
            html += '<div id="inputFormRow">';
            html += '<div class="input-group mb-3">';
            html += '<input type="text" name="title[]" class="form-control m-input" placeholder="Nuevo Jugador" autocomplete="off">';
            html += '<div class="input-group-append">';
            html += '<button id="elimFila" type="button" class="btn btn-danger">Eliminar</button>';
            html += '<br>';
            html += '<br>';
            html += '</div>';
            html += '</div>';

            $('#newRow').append(html);
        });

        // eliminar filas jsjs
        $(document).on('click', '#elimFila', function () {
            $(this).closest('#inputFormRow').remove();
        });
    </script>
</body>
</html>