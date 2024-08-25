import s from './RegisterForm.module.css'
import Button from '../Button'
import Input from '../Input'
import { useState } from 'react'
import { registration } from '../../api'
import { useNavigate } from 'react-router-dom'

export default function RegisterForm() {
    const navigate = useNavigate()
    const [state, setState] = useState({
        email: "",
        userName: "",
        password: "",
        confirmPassword: ""
    })

    const handleSubmit = async (e) => {
        e.preventDefault();
        const error = document.getElementById('error-reg');
        if (state.password.length < 8) {
            error.style.display = 'block';
            error.innerText = "Пароль не может иметь меньше чем 8 символов";
        }
        else if (state.password !== state.confirmPassword) {
            error.style.display = 'block';
            error.innerText = 'Пароли не совпадают';
        }
        else if (state.userName.length < 3) {
            error.style.display = 'block';
            error.innerText = 'У username должно быть больше чем 3 символов';
        }
        else {
            const response = await registration(state.userName, state.email, state.password);
            console.log(response);
            if (response.status === 400) {
                error.style.display = 'block';
                error.innerText = 'Юзернейм или почта уже существуют';
            }
            else {
                navigate('/login');
            }
        }
    }

    const handleChange = (e) => {
        const { id, value } = e.target;
        setState(prevState => ({
            ...prevState,
            [id]: value
        }))
    }

    return (
        <>
            <div className={s.form_header}>
                <h2>Регистрация</h2>
            </div>
            <form onSubmit={handleSubmit} className={s.form_content}>
                {/* <div className={s.input__conteiner}>
                    <div className={s.input__content}>
                        <label htmlFor="email">Email</label><br />
                        <input
                            id='email'
                            value={state.email}
                            onChange={handleChange} type="email"
                            placeholder='example@gmail.com'
                            required />
                    </div>
                </div> */}
                <Input id='email' onChange={handleChange} value={state.email} type="email" placeholder='example@gmail.com'>Email</Input>

                <div className={s.input__conteiner}>
                    <div className={s.input__content}>
                        <label htmlFor="username">Username</label><br />
                        <input
                            id='userName'
                            value={state.userName}
                            onChange={handleChange}
                            type="username"
                            placeholder='name1234'
                            required />
                    </div>
                </div>

                <div className={s.input__conteiner}>
                    <div className={s.input__content}>
                        <label htmlFor="password">Password</label><br />
                        <input
                            id='password'
                            value={state.password}
                            onChange={handleChange}
                            type="password"
                            placeholder='password'
                            required />
                    </div>
                </div>

                <div className={s.input__conteiner}>
                    <div className={s.input__content}>
                        <label htmlFor="password">Confirm password</label><br />
                        <input
                            id='confirmPassword'
                            value={state.confirmPassword}
                            onChange={handleChange}
                            type="password"
                            placeholder='password'
                            required />
                    </div>
                </div>

                <p id='error-reg'></p>
                <Button>Подтвердить</Button>
                <div className={s.form__links}>
                    <a href="/login">Войти</a>
                </div>
            </form>
        </>
    )
}