import React, { useEffect, useState } from "react";
import {submit} from './util';
import './App.css';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
import Estacionamento from './pages/estacionamento';
import Clientes from './pages/clientes';
import Dashboard from './pages/dashboard';
import Veiculos from './pages/veiculos';
import Mensalidades from './pages/mensalidades';
import UpdatePreco from './pages/update-preco';
import Tipos from './pages/tipos';
import Marcas from './pages/marcas';
import Modelos from './pages/modelos';

const filter = (value, itens) =>{
    for (const item of itens){
        let text = String(item.textContent).toUpperCase();
        if (text.includes(value.toUpperCase())){
            if (item.classList.contains("hideItem")) item.classList.remove("hideItem");
        } else {
            item.classList.add("hideItem");
        }
    }
}
window.addEventListener("load",() =>{
    const subItens = document.getElementsByClassName("subItens-menu");

    for (const subItem of subItens){
        const input = subItem.getElementsByClassName('search-itens')[0];
        const itens = subItem.getElementsByClassName("subItens-menu-itens")[0].children;
        input.addEventListener("input",() => {
            filter(input.value,itens);
        })
    }
})

const App = () => {
    

    useEffect(()=>{
        
    },[])
    return (
    <>
        <div className="container">
            <Router>
                <nav class="nav-menu">
                    <span className="title">{"MANCAPARK"}</span>
                    <ul>
                        <li>
                            <input class="menu-item" type="checkbox" id="item-home"/>
                            <label for="item-home"><Link to='/'>{"Home"}</Link></label>
                        </li>
                        <li>
                            <input class="menu-item" type="checkbox" id="item-mensalidades"/>
                            <label for="item-mensalidades">{"Mensalidades"}</label>
                            <section class="subItens-menu">
                                <ul class="subItens-menu-itens">
                                    <li><Link to='/mensalidades'>{"Mensalidades"}</Link></li>
                                    <li><Link to='/clientes'>{"Clientes"}</Link></li>
                                    <li><Link to='/update-preco'>{"Atualizar Valor"}</Link></li>
                                </ul>
                            </section>
                        </li>
                        <li>
                            <input class="menu-item" type="checkbox" id="item-veiculos"/>
                            <label for="item-veiculos">{"Veiculos"}</label>
                            <section class="subItens-menu">
                                <ul class="subItens-menu-itens">
                                    <li><Link to='/veiculos'>{"Veiculos"}</Link></li>
                                    <li><Link to='/tipos'>{"Tipos"}</Link></li>
                                    <li><Link to='/marcas'>{"Marcas"}</Link></li>
                                    <li><Link to='/modelos'>{"Modelos"}</Link></li>
                                </ul>
                            </section>
                        </li>
                        <li>
                            <input class="menu-item" type="checkbox" id="item-dashboard"/>
                            <label for="item-dashboard"><Link to='/dashboard'>{"Dashboard"}</Link></label>
                        </li>
                        <li>
                            <input class="menu-item" type="checkbox" id="item-dashboard"/>
                            <label for="item-dashboard">{"Sair"}</label>
                        </li>
                    </ul> 
                </nav>
                <main>
                    <Routes>
                        <Route exact path='/' element={<Estacionamento 
                            /> } />
                        <Route path='/mensalidades' element={<Mensalidades
                                />} />
                        <Route path='/clientes' element={<Clientes
                                />} />
                        <Route path='/update-preco' element={<UpdatePreco
                                />} />
                        <Route path='/veiculos' element={<Veiculos
                                />} />
                        <Route path='/tipos' element={<Tipos
                                />} />
                        <Route path='/marcas' element={<Marcas
                                />} />
                        <Route path='/modelos' element={<Modelos
                                />} />
                        <Route path='/dashboard' element={<Dashboard
                                />} />
                    </Routes>
                </main>
            </Router>
        </div>
    </>
    );
};
  
export default App;