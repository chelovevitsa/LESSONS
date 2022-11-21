<?php
function add($serwer, $uzytkownik, $haslo, $nazwa, $array){
$db = mysqli_connect($serwer, $uzytkownik, $haslo, $nazwa);

$mysql = "INSERT INTO rezerwacje (data_rez, liczba_osob, telefon) VALUES ('{$array[0]}', {$array[1]}, {$array[2]})";
$db->query($mysql);
$db->close();
}

function clear($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

$data = $ilosc_osob = $telefon = $zgoda = "";

if($_SERVER['REQUEST_METHOD'] == "POST"){
    $data = clear($_POST["data"]);
    $ilosc_osob = clear($_POST["ilosc_osob"]);
    $telefon = clear($_POST["telefon"]);
    $zgoda = clear($_POST["zgoda"]);

    if(add('localhost', 'root', '', 'baza', array($data, $ilosc_osob, $telefon)) == NULL){
        echo("Dodano rezerwacje do bazy");
    }
    else{
        echo("ERROR");
    }
}

?>