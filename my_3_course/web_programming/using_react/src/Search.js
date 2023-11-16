import React from 'react';

const Search = ({onSearchChange, onToggleColumn}) => {
    return (
        <div>
            <label>
                <input
                    type="checkbox"
                    onChange={() => onToggleColumn(0)}
                />
                Имя
            </label>
            <label>
                <input
                    type="checkbox"
                    onChange={() => onToggleColumn(1)}
                />
                Email
            </label>
            <label>
                <input
                    type="checkbox"
                    onChange={() => onToggleColumn(2)}
                />
                Группа
            </label>
            <label>
                Поиск по всем полям:
                <input type="text" onChange={(e) => onSearchChange(e.target.value)}/>
            </label>
        </div>
    );
};

export default Search;
