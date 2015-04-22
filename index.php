
<?php
 
 $images  = array("blackbg.jpg","whitebg.jpg");

 foreach($images as $image)
 {
    $command = escapeshellcmd('./image.py '.$image);
    $output = shell_exec($command);
    echo "<br> Image: <a href='".$image."' >".$image."</a>";
    echo "<br> bgcolor: ".$output;
 }

?>