import s from './LoginForm.module.css'
import Button from '../Button'
import { useState } from 'react'
import { authorization } from '../../Pages/api';
import { Navigate } from 'react-router-dom';

export default function LoginForm() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const handleSubmit = async (e) => {
        e.preventDefault();
        const result = await authorization(username, password);
        if (result.status === 401) {
            alert(result.data.detail)
        }
        else {
            return <Navigate to=''/>
        }
    };
    const handleChangeUsername = (e) => setUsername(e.target.value);
    const handleChangePassword = (e) => setPassword(e.target.value);

    
    return (
        <div className={s.login_form}>
            <div className={s.form_header}>
                <h2>Авторизация</h2>
            </div>
            <form onSubmit={handleSubmit} className={s.form_content}>
                <div className={s.input__username}>
                    <div className={s.input__username__content}>
                        <label htmlFor="username">Username</label><br />
                        <input value={username} onChange={handleChangeUsername} type="username" placeholder='name1234' required/>
                    </div>
                </div>

                <div className={s.input__password}>
                    <div className={s.input__password__content}>
                        <label htmlFor="password">Password</label><br />
                        <input value={password} onChange={handleChangePassword} type="password" placeholder='password' required/>
                    </div>
                </div>
                <Button>Da</Button>
            </form>
        </div>
    )
}