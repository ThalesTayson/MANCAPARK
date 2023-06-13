import React, { useState } from "react";
import Tabela from "../COMPONENTES/tabelas";
import Form from "../COMPONENTES/forms";

const Clientes = ({}) => {

    // ----

    return (
        <>
        <header>
            <span>{"Clientes"}</span>
        </header>
        <div className="menu-superior">
            <input type="button" value={"ADICIONAR ENTRADA"}/>
            <input type="button" value={"ADICIONAR SAIDA"}/>
        </div>
        <Tabela data={[]} call_function={alert} />
        </>
    );
};

export default Clientes;