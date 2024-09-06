import s from './Registration.module.css'
import { Form, Input }  from '../../components'
import { useState } from 'react'
import { registration } from '../../api'
import { useNavigate } from 'react-router-dom'


export default function Registration() {
    const navigate = useNavigate();
    const [state, setState] = useState({
        emailReg: "",
        userNameReg: "",
        passwordReg: "",
        confirmPasswordReg: ""
    });

    const handleSubmit = async (e) => {
        e.preventDefault();
        const error = document.getElementById('errorReg');
        if (state.passwordReg.length < 8) {
            error.style.display = 'block';
            error.innerText = "Пароль не может иметь меньше чем 8 символов";
        }
        else if (state.passwordReg !== state.confirmPasswordReg) {
            error.style.display = 'block';
            error.innerText = 'Пароли не совпадают';
        }
        else if (state.userNameReg.length < 3) {
            error.style.display = 'block';
            error.innerText = 'У username должно быть больше чем 3 символов';
        }
        else {
            const response = await registration(state.userNameReg, state.emailReg, state.passwordReg);
            console.log(response);
            if (response.status === 400) {
                error.style.display = 'block';
                error.innerText = 'Имя или почта уже существуют';
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

    const InputList = [
        <Input key={1} id='emailReg' onChange={handleChange} value={state.email} type="email" placeholder='example@gmail.com'>Email</Input>,
        <Input key={2} id='userNameReg' onChange={handleChange} value={state.userName} type='username' placeholder='name1234'>Username</Input>,
        <Input key={3} id='passwordReg' onChange={handleChange} value={state.password} type='password'>Password</Input>,
        <Input key={4} id='confirmPasswordReg' onChange={handleChange} value={state.confirmPassword} type='password'>Confirm password</Input>
    ];
    return (
        <div className={s.login_conteiner}>
            <div className={s.wrapper}>
                <div className={s.login_form}>
                    <Form InputList={InputList} handleSubmit={handleSubmit} idErr={'errorReg'}>Регистрация</Form>
                </div>            
            </div>
        </div>
    )
}