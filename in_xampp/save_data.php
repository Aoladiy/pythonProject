<?php
// Проверяем, что запрос пришел методом POST
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Получаем данные из тела запроса
    $data = file_get_contents("php://input");

    // Парсим JSON-данные
    $decodedData = json_decode($data, true);

    if ($decodedData !== null) {
        // Открываем файл data.json для записи
        $file = fopen("data.json", "w");

        if ($file) {
            // Записываем данные в файл
            fwrite($file, json_encode($decodedData));

            // Закрываем файл
            fclose($file);

            // Возвращаем успешный ответ
            echo json_encode(array("message" => "Данные успешно сохранены в data.json"));
        } else {
            // Ошибка при открытии файла
            echo json_encode(array("error" => "Ошибка при открытии файла"));
        }
    } else {
        // Ошибка при парсинге JSON
        echo json_encode(array("error" => "Ошибка при парсинге JSON-данных"));
    }
} else {
    // Неверный метод запроса
    echo json_encode(array("error" => "Неверный метод запроса"));
}
?>
