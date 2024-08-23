import s from './LoginForm.module.css'
import Button from '../Button'

export default async function LoginForm() {
    return (
        <>
            <div className={s.form_header}>
                <h2>Авторизация</h2>
            </div>
            <form className={s.form_content}>
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
                <Button>Da</Button>
            </form>
        </>
    )
}