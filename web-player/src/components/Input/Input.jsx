import s from './Input.module.css'

export default function Input({children, type, placeholder, onChange=null, value=null, id=null}) {
    return (
        <div className={s.input__conteiner}>
            <div className={s.input__content}>
                <label htmlFor={type}>{children}</label><br />
                <input
                    id={id}
                    onChange={onChange}
                    value={value}
                    type={type}
                    name={type}
                    placeholder={placeholder}
                    required />
            </div>
        </div>
    )
}