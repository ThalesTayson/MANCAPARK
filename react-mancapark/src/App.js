import React, { useEffect, useState } from "react";
import {submit} from './util';
import './CSS/App.css';
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
import Alert from './COMPONENTES/alert';

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

const App = () => {
    
    const [AlertMsg, setMessage] = useState(<></>);

    const message = ({status ,msg}) => {
        setMessage(<Alert motivo={status} message={msg} />);
        setTimeout(() => setMessage(<></>), 5500);
    }

    useEffect(()=>{
        
    },[])
    return (
    <>
        {AlertMsg}
        <div className="container">
            <Router>
                <nav className="nav-menu">
                    <span className="title">{"MANCAPARK"}</span>
                    <ul>
                        <li>
                            <input className="menu-item" type="checkbox" id="item-home"/>
                            <label htmlFor="item-home"><Link to=''>{"Home"}</Link></label>
                        </li>
                        <li>
                            <input className="menu-item" type="checkbox" id="item-mensalidades"/>
                            <label htmlFor="item-mensalidades">{"Mensalidades"}</label>
                            <section className="subItens-menu">
                                <ul className="subItens-menu-itens">
                                    <li><Link to='/mensalidades'>{"Mensalidades"}</Link></li>
                                    <li><Link to='/clientes'>{"Clientes"}</Link></li>
                                    <li><Link to='/update-preco'>{"Tabela de Preços"}</Link></li>
                                </ul>
                            </section>
                        </li>
                        <li>
                            <input className="menu-item" type="checkbox" id="item-veiculos"/>
                            <label htmlFor="item-veiculos">{"Veiculos"}</label>
                            <section className="subItens-menu">
                                <ul className="subItens-menu-itens">
                                    <li><Link to='/veiculos'>{"Veiculos"}</Link></li>
                                    <li><Link to='/tipos'>{"Tipos"}</Link></li>
                                    <li><Link to='/marcas'>{"Marcas"}</Link></li>
                                    <li><Link to='/modelos'>{"Modelos"}</Link></li>
                                </ul>
                            </section>
                        </li>
                        <li>
                            <input className="menu-item" type="checkbox" id="item-dashboard"/>
                            <label htmlFor="item-dashboard"><Link to='/dashboard'>{"Dashboard"}</Link></label>
                        </li>
                        <li>
                            <input className="menu-item" type="checkbox" id="item-dashboard"/>
                            <label htmlFor="item-dashboard">{"Sair"}</label>
                        </li>
                    </ul> 
                </nav>
                <main>
                    <Routes>
                        <Route exact path='' element={<Estacionamento message={message}
                            /> } />
                        <Route path='/mensalidades' element={<Mensalidades message={message}
                                />} />
                        <Route path='/clientes' element={<Clientes message={message}
                                />} />
                        <Route path='/update-preco' element={<UpdatePreco message={message}
                                />} />
                        <Route path='/veiculos' element={<Veiculos message={message}
                                />} />
                        <Route path='/tipos' element={<Tipos message={message}
                                />} />
                        <Route path='/marcas' element={<Marcas message={message}
                                />} />
                        <Route path='/modelos' element={<Modelos message={message}
                                />} />
                        <Route path='/dashboard' element={<Dashboard message={message}
                                />} />
                    </Routes>
                </main>
            </Router>
        </div>
    </>
    );
};
  
export default App;