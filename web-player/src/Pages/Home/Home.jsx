import {Navigate} from 'react-router-dom'
import {checkUser} from '../../api.js'
import { useEffect, useState } from 'react'

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
        <>
            <h1>Home</h1>
        </>
    )
}