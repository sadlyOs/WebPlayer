import s from './Registration.module.css'
import { RegisterForm }  from '../../components'

export default function Registration() {
    return (
        <div className={s.login_conteiner}>
            <div className={s.wrapper}>
                <div className={s.login_form}>
                    <RegisterForm />
                </div>            
            </div>
        </div>
    )
}