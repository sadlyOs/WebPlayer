import s from './ResetPassword.module.css';
import {Form, Input} from '../../components'
import { useState } from 'react'
import { getUserEmail } from '../../api';



export default function ResetPassword() {
    const [state, setState] = useState({
        emailRes: ""
    })

    const sendEmailPasswordReset = async (e) => {
        e.preventDefault();
        const result = await getUserEmail(state.emailRes);
        if (result.status === 404) {
            const error = document.getElementById('errorRes');
            error.style.display = 'block';
            error.innerText = "Пользователь с такой почтой не существует";
        }
        else {
            console.log(result);
            alert("Мы отправили ссылку для сброса к вам на почту")
        }
    }

    const handleChange = (e) => {
        const { id, value } = e.target;
        setState(prevState => ({
            ...prevState,
            [id]: value
        }))
    }
    const formList = [
        <Input key={1} id='emailRes' onChange={handleChange} value={state.emailRes} type="email" placeholder="example@gmail.com">Email</Input>
    ]
    return (
        <div className={s.reset_conteiner}>
            <div className={s.wrapper}>
                <div className={s.reset_form}>
                    <Form handleSubmit={sendEmailPasswordReset} InputList={formList} idErr="errorRes">Сброс пароля</Form>
                </div>
            </div>
        </div>
        
    )
}