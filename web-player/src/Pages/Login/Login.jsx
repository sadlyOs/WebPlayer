import s from './Login.module.css';
import { authorization } from '../../api';
import { Form, Input } from '../../components';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function Login() {
    const navigate = useNavigate();
    const [state, setState] = useState({
        userNameLog: '',
        passwordLog: ''
    }); 

    const handleSubmit = async (e) => {
        e.preventDefault();
        const result = await authorization(state.userNameLog, state.passwordLog);
        if (result.status === 401) {
            const error = document.getElementById('errorLog');
            error.style.display = 'block';
            error.innerText = "Не правильное имя или пароль";
        }
        else {
            console.log(result);
            localStorage.setItem('token', result.data.access_token);
            navigate('/');
        }
    };

    const handleChange = (e) => {
        const { id, value } = e.target;
        setState(prevState => ({
            ...prevState,
            [id]: value
        }))
    };

    const InputList = [
        <Input key={1} id='userNameLog' onChange={handleChange} value={state.userNameLog} type='username' placeholder='name1234'>Username</Input>,
        <Input key={2} id='passwordLog' onChange={handleChange} value={state.passwordLog} type='password'>Password</Input>,
    ]

    return (
        <div className={s.login_conteiner}>
            <div className={s.wrapper}>
                <div className={s.login_form}>
                    <Form handleSubmit={handleSubmit} InputList={InputList} idErr='errorLog' show="login">Авторизация</Form>
                </div>
            </div>
        </div>
    )
}