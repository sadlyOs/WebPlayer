import {Navigate} from 'react-router-dom'
import {checkUser} from '../../api.js'
import { useEffect, useState } from 'react'
import s from './Home.module.css'

export default function Home(props) {
    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const response = await checkUser();
            setData(response);
        }
        fetchData();
    }, []);

    if (data === 401) {
        return <Navigate to='/login' />
    }

    return (
        <div className={s.music_conteiner}>
            <div className={s.wrapper}>
                <article className={s.conteiner_content}>
                    <h2>Ваши плейлисты</h2>
                    <section className={s.playlist_conteiner}>
                        
                    </section>
                </article>
            </div>
        </div>
    )
}