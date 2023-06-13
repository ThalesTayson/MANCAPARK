import React, { useEffect, useState } from "react";
import Tabela from "../COMPONENTES/tabelas";
import Form from "../COMPONENTES/forms";
import { submit } from "../util";

const tableExample= [
    ["DATA/HORA DA ENTRADA","VEICULO", "CLIENTE", "TEMPO (h)", "VALOR", "..."],
    ["12/06/2023 17:57","nrq-0000 asdasd sadasd", "Thales Vargas", "1h 30m", "R$ 15,00", [
        {"value": "ATUALIZAR CADASTRO", 'link': "marcas/{id}/update"},
        {"value": "ATUALIZAR STATUS", 'link': "marcas/{id}/status/update"},
    ]],

    ["12/06/2023 17:57","nrq-0000 asdasd sadasd", "Thales Vargas", "1h 30m", "R$ 15,00", [
        {"value": "ATUALIZAR CADASTRO", 'link': "marcas/{id}/update"},
        {"value": "ATUALIZAR STATUS", 'link': "marcas/{id}/status/update"},
    ]],

    ["12/06/2023 17:57","nrq-0000 asdasd sadasd", "Thales Vargas", "1h 30m", "R$ 15,00", [
        {"value": "ATUALIZAR CADASTRO", 'link': "marcas/{id}/update"},
        {"value": "ATUALIZAR STATUS", 'link': "marcas/{id}/status/update"},
    ]],

    ["12/06/2023 17:57","nrq-0000 asdasd sadasd", "Thales Vargas", "1h 30m", "R$ 15,00", [
        {"value": "ATUALIZAR CADASTRO", 'link': "marcas/{id}/update"},
        {"value": "ATUALIZAR STATUS", 'link': "marcas/{id}/status/update"},
    ]],

    ["12/06/2023 17:57","nrq-0000 asdasd sadasd", "Thales Vargas", "1h 30m", "R$ 15,00", [
        {"value": "ATUALIZAR CADASTRO", 'link': "marcas/{id}/update"},
        {"value": "ATUALIZAR STATUS", 'link': "marcas/{id}/status/update"},
    ]],

    ["12/06/2023 17:57","nrq-0000 asdasd sadasd", "Thales Vargas", "1h 30m", "R$ 15,00", [
        {"value": "ATUALIZAR CADASTRO", 'link': "marcas/{id}/update"},
        {"value": "ATUALIZAR STATUS", 'link': "marcas/{id}/status/update"},
    ]],

    ["12/06/2023 17:57","nrq-0000 asdasd sadasd", "Thales Vargas", "1h 30m", "R$ 15,00", [
        {"value": "ATUALIZAR CADASTRO", 'link': "marcas/{id}/update"},
        {"value": "ATUALIZAR STATUS", 'link': "marcas/{id}/status/update"},
    ]],

    ["12/06/2023 17:57","nrq-0000 asdasd sadasd", "Thales Vargas", "1h 30m", "R$ 15,00", [
        {"value": "ATUALIZAR CADASTRO", 'link': "marcas/{id}/update"},
        {"value": "ATUALIZAR STATUS", 'link': "marcas/{id}/status/update"},
    ]],

    ["12/06/2023 17:57","nrq-0000 asdasd sadasd", "Thales Vargas", "1h 30m", "R$ 15,00", [
        {"value": "ATUALIZAR CADASTRO", 'link': "marcas/{id}/update"},
        {"value": "ATUALIZAR STATUS", 'link': "marcas/{id}/status/update"},
    ]],

    ["12/06/2023 17:57","nrq-0000 asdasd sadasd", "Thales Vargas", "1h 30m", "R$ 15,00", [
        {"value": "ATUALIZAR CADASTRO", 'link': "marcas/{id}/update"},
        {"value": "ATUALIZAR STATUS", 'link': "marcas/{id}/status/update"},
    ]],

    ["12/06/2023 17:57","nrq-0000 asdasd sadasd", "Thales Vargas", "1h 30m", "R$ 15,00", [
        {"value": "ATUALIZAR CADASTRO", 'link': "marcas/{id}/update"},
        {"value": "ATUALIZAR STATUS", 'link': "marcas/{id}/status/update"},
    ]],

    ["12/06/2023 17:57","nrq-0000 asdasd sadasd", "Thales Vargas", "1h 30m", "R$ 15,00", [
        {"value": "ATUALIZAR CADASTRO", 'link': "marcas/{id}/update"},
        {"value": "ATUALIZAR STATUS", 'link': "marcas/{id}/status/update"},
    ]],

    ["12/06/2023 17:57","nrq-0000 asdasd sadasd", "Thales Vargas", "1h 30m", "R$ 15,00", [
        {"value": "ATUALIZAR CADASTRO", 'link': "marcas/{id}/update"},
        {"value": "ATUALIZAR STATUS", 'link': "marcas/{id}/status/update"},
    ]],

    ["12/06/2023 17:57","nrq-0000 asdasd sadasd", "Thales Vargas", "1h 30m", "R$ 15,00", [
        {"value": "ATUALIZAR CADASTRO", 'link': "marcas/{id}/update"},
        {"value": "ATUALIZAR STATUS", 'link': "marcas/{id}/status/update"},
    ]],

    ["12/06/2023 17:57","nrq-0000 asdasd sadasd", "Thales Vargas", "1h 30m", "R$ 15,00", [
        {"value": "ATUALIZAR CADASTRO", 'link': "marcas/{id}/update"},
        {"value": "ATUALIZAR STATUS", 'link': "marcas/{id}/status/update"},
    ]],

    ["12/06/2023 17:57","nrq-0000 asdasd sadasd", "Thales Vargas", "1h 30m", "R$ 15,00", [
        {"value": "ATUALIZAR CADASTRO", 'link': "marcas/{id}/update"},
        {"value": "ATUALIZAR STATUS", 'link': "marcas/{id}/status/update"},
    ]],

    ["12/06/2023 17:57","nrq-0000 asdasd sadasd", "Thales Vargas", "1h 30m", "R$ 15,00", [
        {"value": "ATUALIZAR CADASTRO", 'link': "marcas/{id}/update"},
        {"value": "ATUALIZAR STATUS", 'link': "marcas/{id}/status/update"},
    ]],
]

const Estacionamento = ({}) => {

    const [data, setData] = useState([]);
    const [form, setForm] = useState(<></>)
    const [fundo, setFundo] = useState(<></>)

    const get_tabela = () => {
        let Method = "GET";
        let url = "http://localhost:8000/estacionamento/lista";
        submit({Method, url})
            .then((resp) => resp.json())
            .then((resp) => {
                let _data = resp;
                console.log(_data);
                setData(_data.data);
            });
    }

    const closeForm = () => {
        setForm(<></>);
        setFundo(<></>);
    };

    const req_form = ( link ) => {
        alert(link);
        //setFundo(<div onClick={closeForm} className="fundoVidro" />)
        //setForm(<Form link={link} />);
    };

    useEffect(()=>{
        if (data.length === 0) {
            get_tabela();
        }
    },[data])

    return (
        <>
        <header>
            <span>{"Estacionamento"}</span>
        </header>
        <div className="menu-superior">
            <input type="button" value={"ADICIONAR ENTRADA"}/>
            <input type="button" value={"ADICIONAR SAIDA"}/>
        </div>
        <Tabela data={data} call_function={req_form} />
        </>
    );
};

export default Estacionamento;