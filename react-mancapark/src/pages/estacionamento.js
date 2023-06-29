import React, { useEffect, useState } from "react";
import Tabela from "../COMPONENTES/tabelas";
import Form from "../COMPONENTES/forms";
import { submit } from "../util";

const Estacionamento = ({ message }) => {

    const [data, setData] = useState([]);
    const [form, setForm] = useState(<></>)
    const [fundo, setFundo] = useState(<></>)

    const get_tabela = () => {
        let Method = "GET";
        let link = "/estacionamento/lista";
        submit({Method, link})
            .then((resp) => resp.json())
            .then((resp) => {
                let _data = resp;
                setData(_data.data);
            });
    }

    const closeForm = () => {
        setForm(<></>);
        setFundo(<></>);
    };

    const req_form = ( link ) => {
        setFundo(<div onClick={closeForm} className="fundoVidro" />)
        setForm(<Form link={link} messages={message} update_data={get_tabela} />);
    };

    useEffect(()=>{

        const consulta_com_intervalo = setInterval(get_tabela,1500)

        return () => clearInterval(consulta_com_intervalo);

    })

    return (
        <>
        <header>
            <span>{"Estacionamento"}</span>
        </header>
        <div className="menu-superior">
            <input type="button" value={"ADICIONAR ENTRADA"} onClick={() => req_form("/estacionamento/lancar-entrada")}/>
            <input type="button" value={"ADICIONAR SAIDA"} onClick={() => req_form("/estacionamento/lancar-saida")}/>
        </div>
        <Tabela data={data} call_function={req_form} />
        {fundo}
        {form}
        </>
    );
};

export default Estacionamento;