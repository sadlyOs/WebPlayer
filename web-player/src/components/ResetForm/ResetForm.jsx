import s from './ResetForm.module.css'
import Button from '../Button'
import Input from '../Input'

export default function ResetForm() {
    return (
        <>
            <div className={s.form_header}>
                <h2>Сброс пароля</h2>
            </div>
            <form className={s.form__content}>
                <p>Введите почту для подтверждения сброса</p>
                <Input type="email" placeholder="example@gmail.com">Email</Input>

                <Button>Подтвердить</Button>
            </form>
        </>
    )
}