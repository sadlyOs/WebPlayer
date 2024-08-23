import s from './Login.module.css'
import { Input } from '../../components'
import { useCallback } from 'react'
import { authorization } from '../api'

export default function Login() {

    const handleClick = useCallback((username, password) => {
        return async () => {
            await authorization(username, password)
        }
    })

    return (
        <div className={s.login_conteiner}>
            <div className={s.wrapper}>
                <div className={s.login_form}>
                    <div className={s.form_header}>
                        <h2>Авторизация</h2>
                    </div>
                    <div className={s.form_content}>
                        <div className={s.input__username}>
                            <div className={s.input__username__content}>
                                <label htmlFor="username">Username</label><br />
                                <input type="username" placeholder='name1234' required/>
                            </div>
                        </div>

                        <div className={s.input__password}>
                            <div className={s.input__password__content}>
                                <label htmlFor="password">Password</label><br />
                                <input type="password" placeholder='password' required/>
                            </div>
                        </div>

                        <Input value="Вход" />
                    </div>
                </div>
            </div>
        </div>
    )
}