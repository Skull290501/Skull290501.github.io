<?php  

$conex = mysqli_connect("localhost","root","","practica");

$id = $_REQUEST['id'];

$consulta = "DELETE FROM formaspirante WHERE id = $id";

$res = $conex->query($consulta);

if ($res) {
    echo "Se elimino";
    ?>
    <script type="text/javascript"> 
    window.location.href="http://www.example-url.com" 
    </script> 
    <?php   
}else{
    echo "No se elimno";
}


?>
