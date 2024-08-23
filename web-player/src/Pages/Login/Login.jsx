import s from './Login.module.css'
import { useCallback } from 'react'
import { authorization } from '../api'
import LoginForm from '../../components/Form'

export default function Login() {

    const handleClick = useCallback((username, password) => {
        return async () => {
            // await authorization(username, password)
            console.log(username, password);
        }
    })

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