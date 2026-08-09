<?php

$key = $_REQUEST["needle"] ?? "";

if ($key !== "") {
    $safeKey = escapeshellarg($key);
    passthru("grep -i $safeKey dictionary.txt");
}

?>
