import s from './Login.module.css'
import { useCallback } from 'react'
import { authorization } from '../api'
import LoginForm from '../../components/Form'

export default function Login() {
    return (
        <div className={s.login_conteiner}>
            <div className={s.wrapper}>
                <LoginForm />
            </div>
        </div>
    )
}