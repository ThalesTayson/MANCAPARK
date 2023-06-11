import React from "react";

const Tabela = ({objts}) => {

    // ----
    const itens = Object.keys(objts);


    return (
        <nav class="nav-menu">
            <ul>
                {itens.map((value) => {
                            return (<li>
                                <input class="menu-item" type="checkbox" id={"item-" + value}/>
                                <label for={"item-" + value}>{objts[value]}</label>
                            </li>);
                        })}
            </ul>
           
        </nav>
    );
};

export default Tabela;