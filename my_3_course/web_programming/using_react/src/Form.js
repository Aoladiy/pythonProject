import React, {useState} from 'react';

const Form = ({onSubmit, resetForm}) => {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        group: 'ПИ21-1',
    });

    const handleChange = (e) => {
        const {name, value} = e.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: value,
        }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit(formData);
        resetForm();
    };

    const handleCancel = () => {
        resetForm();
    };

    return (
        <form onSubmit={handleSubmit} id="myForm" className="mt-4">
            <div className="form-group">
                <label htmlFor="name">Имя:</label>
                <input
                    type="text"
                    id="name"
                    name="name"
                    className="form-control"
                    value={formData.name}
                    onChange={handleChange}
                    required
                />
            </div>
            <div className="form-group">
                <label htmlFor="email">Email:</label>
                <input
                    type="email"
                    id="email"
                    name="email"
                    className="form-control"
                    value={formData.email}
                    onChange={handleChange}
                    required
                />
            </div>
            <div className="form-group">
                <label htmlFor="group">Группа:</label>
                <select
                    id="group"
                    name="group"
                    className="form-control"
                    value={formData.group}
                    onChange={handleChange}
                >
                    <option value="ПИ21-1">ПИ21-1</option>
                    <option value="ПИ21-2">ПИ21-2</option>
                    <option value="ПИ21-3">ПИ21-3</option>
                    <option value="ПИ21-4">ПИ21-4</option>
                    <option value="ПИ21-5">ПИ21-5</option>
                    <option value="ПИ21-6">ПИ21-6</option>
                    <option value="ПИ21-7">ПИ21-7</option>
                </select>
            </div>
            <div className="btn-group">
                <input type="submit" className="btn btn-primary" value="Сохранить"/>
                <button type="button" className="btn btn-secondary" onClick={handleCancel}>
                    Отменить изменение
                </button>
            </div>
        </form>
    );
};

export default Form;
