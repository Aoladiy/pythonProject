document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById('myForm');
    const cancelButton = document.getElementById('cancelButton');

    // Функция для очистки формы
    function resetForm() {
        form.reset();
        form.removeAttribute('data-editing');
        document.querySelector('.btn.btn-primary').value = 'Сохранить';
    }

    // Обработчик события для кнопки "Отменить изменение"
    cancelButton.addEventListener('click', function () {
        resetForm();
    });

    // Функция для получения данных из сервера и отображения их в таблице
    function fetchDataAndPopulateTable() {
        fetch('http://localhost:8000/get_data')
            .then(response => response.json())
            .then(data => {
                const tableBody = document.querySelector('#dataTable tbody');
                tableBody.innerHTML = ''; // Очищаем текущие данные в таблице

                data.forEach(item => {
                    const row = tableBody.insertRow(-1);
                    row.innerHTML = `
                            <td>${item.name}</td>
                            <td>${item.email}</td>
                            <td>${item.group}</td>
                            <td>
                                <button class="edit-btn" data-id="${item.id}">Редактировать</button>
                                <button class="delete-btn" data-id="${item.id}">Удалить</button>
                            </td>
                        `;
                });

                attachEditAndDeleteListeners(); // Присоединяем обработчики событий к кнопкам
            })
            .catch(error => console.log('Ошибка получения данных:', error));
    }

    fetchDataAndPopulateTable(); // Получаем данные и отображаем их при загрузке страницы

    // Обработчик события для отправки формы
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(form);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });

        const isEditing = form.hasAttribute('data-editing');

        if (isEditing) {
            // Если это редактирование, обработать редактирование данных
            const itemId = form.getAttribute('data-editing');
            fetch(`http://localhost:8000/edit_data/${itemId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
                .then(() => {
                    fetchDataAndPopulateTable(); // Обновляем таблицу после редактирования
                    this.reset(); // Сброс формы
                    this.removeAttribute('data-editing');
                })
                .catch(error => console.error('Ошибка обновления данных:', error));
            resetForm();
        } else {
            // Если это добавление новых данных
            fetch('http://localhost:8000/save_data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
                mode: 'cors',
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(() => {
                    fetchDataAndPopulateTable(); // Обновляем данные в таблице после сохранения
                    this.reset();
                })
                .catch(error => console.error('Ошибка сохранения данных:', error));
            resetForm();
        }
    });

    // Обработчики событий для кнопок "Редактировать" и "Удалить"
    function attachEditAndDeleteListeners() {
        document.querySelectorAll('.edit-btn').forEach(button => {
            button.addEventListener('click', function () {
                document.querySelector('.btn.btn-primary').value = 'Редактировать';
                const itemId = this.getAttribute('data-id');
                const tableRow = this.parentElement.parentElement;
                const name = tableRow.querySelector('td:nth-child(1)').innerText;
                const email = tableRow.querySelector('td:nth-child(2)').innerText;
                const group = tableRow.querySelector('td:nth-child(3)').innerText;

                // Заполнение формы данными для редактирования
                document.getElementById('name').value = name;
                document.getElementById('email').value = email;
                document.getElementById('group').value = group;

                // Установка атрибута, указывающего на то, что форма находится в процессе редактирования
                document.getElementById('myForm').setAttribute('data-editing', itemId);
            });
        });

        document.querySelectorAll('.delete-btn').forEach(button => {
            button.addEventListener('click', function () {
                const itemId = this.getAttribute('data-id');
                fetch(`http://localhost:8000/delete_data/${itemId}`, {
                    method: 'DELETE'
                })
                    .then(() => {
                        fetchDataAndPopulateTable(); // Обновляем данные в таблице после удаления
                    })
                    .catch(error => console.error('Ошибка удаления данных:', error));
            });
        });
    }

    attachEditAndDeleteListeners();
});