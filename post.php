<?php

$imageData=$_POST['cat'];
$chat_id = $_POST['chat_id'];
echo $chat_id;
if (!empty($chat_id) && !empty($imageData)) {
$filteredData=substr($imageData, strpos($imageData, ",")+1);
$unencodedData=base64_decode($filteredData);
$fp = fopen( $chat_id.'.png', 'wb' );
fwrite( $fp, $unencodedData);
fclose( $fp );
#fuck php 
shell_exec("python3 poster.py ". $chat_id);
}