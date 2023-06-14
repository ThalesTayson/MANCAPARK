import React, { useEffect, useState } from "react";
import Tabela from "../COMPONENTES/tabelas";
import Form from "../COMPONENTES/forms";
import { submit } from "../util";

const Mensalidades = ({}) => {

    const [data, setData] = useState([]);
    const [form, setForm] = useState(<></>)
    const [fundo, setFundo] = useState(<></>)

    const get_tabela = () => {
        let Method = "GET";
        let link = "/mensalidades/lista";
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
            <span>{"Mensalidades Ativas"}</span>
        </header>
        <div className="menu-superior">
            <input type="button" value={"ADICIONAR MENSALIDADE"} onClick={() => req_form("/mensalidades/create")}/>
        </div>
        <Tabela data={data} call_function={req_form} />
        {fundo}
        {form}
        </>
    );
};

export default Mensalidades;