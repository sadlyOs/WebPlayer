import s from './LoginForm.module.css'
import Button from '../Button'
import Input from '../Input';
import { useState } from 'react'
import { authorization } from '../../api';
import { Navigate, useNavigate } from 'react-router-dom';

export default function LoginForm() {
    const navigate = useNavigate();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const handleSubmit = async (e) => {
        e.preventDefault();
        const result = await authorization(username, password);
        if (result.status === 401) {
            const error = document.getElementById('error');
            error.style.display = 'block';
            error.innerText = result.data.detail;
        }
        else {
            console.log(result);
            localStorage.setItem('token', result.data.access_token);
            navigate('/');
        }
    };
    const handleChangeUsername = (e) => setUsername(e.target.value);
    const handleChangePassword = (e) => setPassword(e.target.value);

    
    return (
        <>
            <div className={s.form_header}>
                <h2>Авторизация</h2>
            </div>
            <form onSubmit={handleSubmit} className={s.form_content}>  
                <Input onChange={handleChangeUsername} value={username} type="username" placeholder="name1234">Username</Input>
                <Input onChange={handleChangePassword} value={password} type="password" placeholder="password">Password</Input>
                <p id='error'></p>
                <Button>Подтвердить</Button>
                <div className={s.form__links}>
                    <a href="/registration">Зарегестрироваться</a>
                    <a href="/accounts/password/reset">Забыли пароль?</a>
                </div>
            </form>
        </>
    )
}