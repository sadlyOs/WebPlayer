import s from './Button.module.css'
export default function Button({ children, type='submit', onClick}) {
    return (
        <button type={type} className={s.button}>{children}</button>
    );
}