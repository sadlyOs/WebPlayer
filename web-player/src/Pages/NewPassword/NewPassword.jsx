import { useNavigate, useParams, useSearchParams } from "react-router-dom"
import { Form, Input } from "../../components";
import s from "./NewPassword.module.css";
import { useState, useEffect } from "react";
import { getTokenDecode, updatePassword } from "../../api";

export default function NewPassword() {
    const navigate = useNavigate()
    const [searchParams, setSearchParams] = useSearchParams()
    const [response, setResponse] = useState([])
    useEffect(() => {
        const axiosData = async () => {
            const result = await getTokenDecode(searchParams.get('token'));
            setResponse(result);
        }
        axiosData();
    }, [])

    if (response.status === 401) navigate('/accounts/password/reset')

    const [state, setState] = useState({
        userNewPassword: '',
        userNewPasswordConf: ''
    })

    const handleSubmit = async (e) => {
        e.preventDefault()
        const error = document.getElementById('errorNewConf');
        if (state.userNewPassword.length < 8) {
            error.style.display = 'block';
            error.innerText = "Пароль не может иметь меньше чем 8 символов";
        }
        else if (state.userNewPassword !== state.userNewPasswordConf) {
            error.style.display = 'block';
            error.innerText = 'Пароли не совпадают';
        }
        else {
            const result = await updatePassword(response.data.user.sub, state.userNewPasswordConf)
            console.log(result)
            if (result.status === 403) {
                error.style.display = 'block';
                error.innerText = "Нельзя изменить пароль на уже существующий, напишите новый пароль.";
            }
            else navigate('/login')
        }
    }

    const handleChange = (event) => {
        const { id, value } = event.target;
        setState(prevState => ({
            ...prevState,
            [id]: value
            })
        )
    }

    

    const InputList = [
        <Input key={1} id='userNewPassword' type='password' onChange={handleChange} value={state.userNewPassword}>New password</Input>,
        <Input key={2} id='userNewPasswordConf' type='password' onChange={handleChange} value={state.userNewPasswordConf}>Confirm password</Input>
    ]
    return (
        <div className={s.NewPassword_conteiner}>
            <div className={s.wrapper}>
                <div className={s.NewPassword_form}>
                    <Form handleSubmit={handleSubmit} InputList={InputList} idErr='errorNewConf'>Новый пароль</Form>
                </div>
            </div>
        </div>
    )
}