import React, { useEffect, useState } from "react";
import Tabela from "../COMPONENTES/tabelas";
import Form from "../COMPONENTES/forms";
import { submit } from "../util";

const Precos = ({}) => {

    const [data, setData] = useState([]);
    const [form, setForm] = useState(<></>)
    const [fundo, setFundo] = useState(<></>)

    const get_tabela = () => {
        let Method = "GET";
        let link = "/precos/lista";
        submit({Method, link})
            .then((resp) => resp.json())
            .then((resp) => {
                let _data = resp;
                setData(_data.data);
            });
    }

    const messages = ({status='info', msg}) => {
        alert(status + ' ' + msg);
    }

    const closeForm = () => {
        setForm(<></>);
        setFundo(<></>);
    };

    const req_form = ( link ) => {
        setFundo(<div onClick={closeForm} className="fundoVidro" />)
        setForm(<Form link={link} messages={messages} />);
    };

    useEffect(()=>{
        if (data.length === 0) {
            get_tabela();
        }
    },[data])

    return (
        <>
        <header>
            <span>{"Tabela de Preços"}</span>
        </header>
        <div className="menu-superior">
            <input type="button" value={"ADICIONAR PREÇO"} onClick={() => req_form("/precos/create")}/>
        </div>
        <Tabela data={data} call_function={req_form} />
        {fundo}
        {form}
        </>
    );
};

export default Precos;