import s from './ResetPassword.module.css';
import {ResetForm} from '../../components'

export default function ResetPassword() {
    return(
        <div className={s.reset_conteiner}>
            <div className={s.wrapper}>
                <div className={s.reset_form}>
                    <ResetForm />
                </div>            
            </div>
        </div>
    )
}