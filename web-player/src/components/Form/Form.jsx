import s from './Form.module.css'
import Button from '../Button'

export default function Form({ children, handleSubmit, InputList, idErr, show }) {
    const LinksBlock = () => {
        if (show === "login") {
            return (
                <div className={s.form__links}>
                <a href="/registration">Зарегестрироваться</a>
                <a href="/accounts/password/reset">Забыли пароль?</a>
                </div> 
            )
        }
        else {
            return (
                <div className={s.form__links}>
                    <a href="/login">Вход</a>
                </div> 
            )
            
        }
    }
    return (
        <>
            <div className={s.form_header}>
                <h2>{children}</h2>
            </div>
            <form className={s.form_content} onSubmit={handleSubmit}>
                {InputList}
                <p id={idErr}></p>
                <Button>Подтвердить</Button>
                <LinksBlock />
            </form>
            
        </>
            
    )
}