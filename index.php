<html>
<head>
<meta charset="UTF-8" />
<title>web enabled garage</title>
</head>
<body>

<!-- comment out camera
<?php
exec("sudo fswebcam --no-banner -d /dev/video0 -r 352x288 /var/www/html/image.jpg");
echo ("<img src=\"image.jpg\"><br>");
?>
-->

<br><br>

<?php
if (isset($_POST['Button_Right'])) {
    exec("sudo python /home/pi/garage/pythonR.py");
}
if (isset($_POST['Button_Left'])){
    exec("sudo python /home/pi/garage/pythonL.py");
}
?>

<form method="post">
<button name="Button_Left">Left Door</button>
<button name="Button_Right">Right Door</button>
</form>
<br><br>

<br>
</body>
</html>

