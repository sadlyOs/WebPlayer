import s from './Input.module.css'
export default function Input({ children, type='submit'}) {
    return (
        <input type={type} value={children} className={s.input} />
    );
}