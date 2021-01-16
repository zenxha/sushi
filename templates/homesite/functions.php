<?php
$username = $_POST['username'];
$password = $_POST['password'];
if (!empty($username) || !empty($password){
$host = "localhost";
    $dbUsername = "root";
    $dbPassword = "";
    $dbname = "Users.db";
    //create connection
    $conn = new mysqli($host, $dbUsername, $dbPassword, $dbname);
    if (mysqli_connect_error()) {
     die('Connect Error('. mysqli_connect_errno().')'. mysqli_connect_error());
     } else {
        $SELECT = "SELECT email From register Where email = ? Limit 1";
             $INSERT = "INSERT Into register (username, password) values(?, ?)";
             //Prepare statement
             $stmt = $conn->prepare($SELECT);
             $stmt->bind_param("s", $email);
             $stmt->execute();
             $stmt->bind_result($username);
             $stmt->store_result();
             $stmt->store_result();
             $stmt->fetch();
             $rnum = $stmt->num_rows;
             if ($rnum==0) {
              $stmt->close();
              $stmt = $conn->prepare($INSERT);
              $stmt->bind_param("ssssii", $username, $password);
              $stmt->execute();
              echo "New record inserted sucessfully";
             } else {
              echo "Someone already register using this Username";
             }
             $stmt->close();
             $conn->close();
            }
     }
