import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'

import {BrowserRouter, Routes, Route} from 'react-router-dom'
import {HomePage, LoginPage} from './Pages/Pages.jsx'

import './App.css'

function App() {

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path='' element={<HomePage username="dima" password="ssfsdfsd"/>} />
          <Route path='/login' element={<LoginPage />} />
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
