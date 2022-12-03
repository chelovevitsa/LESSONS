<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styl_1.css?v=1">

    <title>Wędkowanie</title>
   
</head>
<body>
    <div class="header">
        <h1>Portal dla wędkarzy</h1>
    </div>
    <div class="blocks">
        <div class="left-block">
            <div class="first-table">
                <h3>Ryby zamieszkujące rzeki</h3>
                <ol>
                    <?php
                    include_once 'skrypt.php';
                    $db = connect_db();
                    get_fishes($db);
                    ?>
                </ol>
            </div>
            <div class="second-table">
                <h3>Ryby drapieżne naszych wód</h3>
                <table>
                    <tr>
                        <th>L.p.</th>
                        <th>Gatunek</th>
                        <th>Występowanie</th>
                    </tr>
                    <?php
                        get_wystepowanie($db);
                        disconnect_db($db);
                    ?>
                </table>
            </div>
        </div>
        <div class="right-block">
            <img class="img" src="ryba1.jpg" alt="Sum">
            <a href="kwerendy.txt">Pobierz kwerendy</a>
        </div>
        </div>
    </div>
    <div class="footer">
    <p>Stronę wykonał: 00000000000</p>
    </div>
</body>
</html>