import s from './Login.module.css';
import { useCallback } from 'react';
import { authorization } from '../../api';
import { LoginForm } from '../../components';

export default function Login() {
    return (
        <div className={s.login_conteiner}>
            <div className={s.wrapper}>
                <div className={s.login_form}>
                    <LoginForm />
                </div>
            </div>
        </div>
    )
}