<?php

error_reporting(0);

require_once 'Folder.php';



header('Content-Type: application/json');

$ctrl = isset($_GET['ctrl']) ? strip_tags($_GET['ctrl']) : null;
$path = isset($_GET['path']) ? strip_tags($_GET['path']) : null;
$json = [];

$href = $_SERVER['REQUEST_SCHEME'] . '://' . $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI'];

$file = dirname(__FILE__) . '';

if ($ctrl) {
    // feeds
    $file .= '/' . $ctrl;

    $result = Folder::getContent($file);

    $posts = [];
    foreach ($result['files'] as $feed) {
        $name = substr($feed['name'], 0, -5);
        $json[] = [
            'name' => $name,
            'link' => $href . '/' . $name,
            'total' => count(json_decode(file_get_contents($file . '/' . $feed['name'])))
        ];
    }

    // website
    if ($path) {
        $file .= '/' . $path . '.json';

        if (file_exists($file)) {
            $json = json_decode(file_get_contents($file));
        }
    }
} else {
    $json = [
        'name' => 'posts',
        'link' => $href . 'posts'
    ];
}

echo json_encode($json);
