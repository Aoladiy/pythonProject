import React from 'react';

const Table = ({data, onEditButtonClick, onDeleteButtonClick}) => {
    const renderTableRows = () => {
        return data.map(item => (
            <tr key={item.id} data-id={item.id}>
                <td>{item.name}</td>
                <td>{item.email}</td>
                <td>{item.group}</td>
                <td>
                    <button className="edit-btn" onClick={() => onEditButtonClick(item.id)}>
                        Редактировать
                    </button>
                    <button className="delete-btn" onClick={() => onDeleteButtonClick(item.id)}>
                        Удалить
                    </button>
                </td>
            </tr>
        ));
    };

    return (
        <table id="dataTable" className="table table-dark mt-4">
            <thead>
            <tr>
                <th>Имя</th>
                <th>Email</th>
                <th>Группа</th>
                <th>Действия</th>
            </tr>
            </thead>
            <tbody>
            {data.length > 0 ? (
                renderTableRows()
            ) : (
                <tr>
                    <td colSpan="4">Нет данных</td>
                </tr>
            )}
            </tbody>
        </table>
    );
};

export default Table;
