<?php
$jsonData = file_get_contents('data.json'); // Загрузка JSON-данных из файла
$data = json_decode($jsonData, true); // Декодирование JSON в ассоциативный массив

if ($data === null) {
    echo "Ошибка при чтении JSON-файла.";
} else {
    // Красиво выводим JSON-данные
    echo "<pre>";
    echo json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
    echo "</pre>";
}