import React, { useEffect, useState } from "react";
import {submit} from './util';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
import Estacionamento from './estacionamento';
import Clientes from './clientes';
import Dashboard from './dashboard';
import Veiculos from './veiculos';
import Logout from './logout';

const App = () => {
    

    useEffect(()=>{
        if (Object.keys(localidades).length === 0) {
            submit({},'GET','/sistema-inventario/get-localidades')
                .then(response => response.json())
                .then(data => {
                    setLocalidades(data);
                });
        }
    },[])
    return (
    <>
        <Router>
            <div className='App'>
                <Link to='/'>Home</Link>
                <Link to='/clientes'>Clientes</Link>
                <Link to='/veiculos'>Veiculos</Link>
                <Link to='/dashboard'>Dashboard</Link>
                <Link to='/logout'>Sair</Link>
            </div>
            <Routes>
                <Route exact path='/' element={<Estacionamento 
                    /> } />

                <Route path='/clientes' element={<Clientes
                        />} />
                <Route path='/veiculos' element={<Veiculos
                        />} />
                <Route path='/dashboard' element={<Dashboard
                        />} />
                <Route path='/logout' element={<Logout
                        />} />
            </Routes>
        </Router>
    </>
    );
};
  
export default App;