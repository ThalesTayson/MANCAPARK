import React, { useEffect, useState } from "react";
import {submit} from './util';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';

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
                <Link to='/sistema-inventario/'>Home</Link>
                <Link to='/sistema-inventario/localidades'>lista</Link>
            </div>
            <Routes>
                <Route exact path='/sistema-inventario/' element={<Filtro 
                    andar={andar} 
                    setor={setor}
                    local={local}
                    setAndar={setAndar}
                    setSetor={setSetor}
                    setLocal={setLocal}
                    localidades={localidades}
                    /> } />
                <Route path='/sistema-inventario/localidades' element={<Localidades
                                localidades={localidades}
                                setLocalidades={setLocalidades} 
                        />} />
            </Routes>
        </Router>
    </>
    );
};
  
export default App;