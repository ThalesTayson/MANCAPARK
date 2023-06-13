import React, { useState } from "react";
import Tabela from "../COMPONENTES/tabelas";
import Form from "../COMPONENTES/forms";

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

    const [form, setForm] = useState(<></>)
    const [fundo, setFundo] = useState(<></>)

    const closeForm = () => {
        setForm(<></>);
        setFundo(<></>);
    };

    const req_form = ( link ) => {
        alert(link);
        //setFundo(<div onClick={closeForm} className="fundoVidro" />)
        //setForm(<Form link={link} />);
    };

    return (
        <>
        <header>
            <span>{"Estacionamento"}</span>
        </header>
        <Tabela data={tableExample} call_function={req_form} />
        </>
    );
};

export default Estacionamento;