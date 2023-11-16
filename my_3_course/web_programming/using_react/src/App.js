import React, {useEffect, useState} from 'react';
import './App.css';
import Form from './Form';
import Table from './Table';
import Search from './Search';

const App = () => {
    const [originalData, setOriginalData] = useState([]);
    const [filteredData, setFilteredData] = useState([]);

    useEffect(() => {
        fetchDataAndPopulateTable();
    }, []);

    const fetchDataAndPopulateTable = () => {
        fetch('http://localhost:8000/get_data')
            .then(response => response.json())
            .then(data => {
                setOriginalData(data);
                setFilteredData(data);
            })
            .catch(error => console.log('Ошибка получения данных:', error));
    };

    const resetForm = () => {
        document.getElementById('myForm').reset();
        document.getElementById('myForm').removeAttribute('data-editing');
        document.querySelector('.btn.btn-primary').value = 'Сохранить';
    };

    const handleFormSubmit = (formData) => {
        const isEditing = document.getElementById('myForm').hasAttribute('data-editing');

        if (isEditing) {
            const itemId = document.getElementById('myForm').getAttribute('data-editing');
            fetch(`http://localhost:8000/edit_data/${itemId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            })
                .then(() => {
                    fetchDataAndPopulateTable();
                    resetForm();
                })
                .catch(error => console.error('Ошибка обновления данных:', error));
        } else {
            fetch('http://localhost:8000/save_data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
                mode: 'cors',
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(() => {
                    fetchDataAndPopulateTable();
                    resetForm();
                })
                .catch(error => console.error('Ошибка сохранения данных:', error));
        }
    };

    const handleEditButtonClick = (itemId) => {
        document.querySelector('.btn.btn-primary').value = 'Редактировать';
        const tableRow = document.querySelector(`[data-id="${itemId}"]`);
        const name = tableRow.querySelector('td:nth-child(1)').innerText;
        const email = tableRow.querySelector('td:nth-child(2)').innerText;
        const group = tableRow.querySelector('td:nth-child(3)').innerText;

        document.getElementById('name').value = name;
        document.getElementById('email').value = email;
        document.getElementById('group').value = group;

        document.getElementById('myForm').setAttribute('data-editing', itemId);
    };

    const handleDeleteButtonClick = (itemId) => {
        fetch(`http://localhost:8000/delete_data/${itemId}`, {
            method: 'DELETE'
        })
            .then(() => {
                fetchDataAndPopulateTable();
            })
            .catch(error => console.error('Ошибка удаления данных:', error));
    };

    const handleSearchChange = (searchText) => {
        if (!searchText) {
            setFilteredData(originalData);
        } else {
            const filtered = originalData.filter(item => {
                return (
                    item.name.toLowerCase().includes(searchText.toLowerCase()) ||
                    item.email.toLowerCase().includes(searchText.toLowerCase()) ||
                    item.group.toLowerCase().includes(searchText.toLowerCase())
                );
            });
            setFilteredData(filtered);
        }
    };

    const handleToggleColumn = (columnIndex) => {
        const table = document.getElementById("dataTable");
        const headerRow = table.querySelector("thead tr");
        const rows = table.querySelectorAll("tbody tr");
        const isColumnVisible = !headerRow.querySelectorAll("th")[columnIndex].classList.contains("hidden");

        headerRow.querySelectorAll("th")[columnIndex].classList.toggle("hidden", isColumnVisible);

        rows.forEach((row) => {
            const cells = row.querySelectorAll("td");
            cells[columnIndex].classList.toggle("hidden", isColumnVisible);
        });
    };

    return (
        <div className="container">
            <h1 className="mt-4">Форма с сохранением в localStorage и на сервер</h1>
            <Form onSubmit={handleFormSubmit} resetForm={resetForm}/>
            <Search onSearchChange={handleSearchChange} onToggleColumn={handleToggleColumn}/>
            <Table
                data={filteredData}
                onEditButtonClick={handleEditButtonClick}
                onDeleteButtonClick={handleDeleteButtonClick}
            />
        </div>
    );
};

export default App;
