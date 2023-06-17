import React, { useState } from "react";
import '../CSS/Card.css';
import SVG_Icon_down from '../SVG/arrow-down.svg';
import SVG_Icon_up from '../SVG/arrow-up.svg';

const Card = ({ title, valor, indice, descricaoIndice }) => {
    let icon = <></>;
    
    if (indice > 0){
        icon = <SVG_Icon_up width="50" height="50"/>;
    } else if (indice < 0){
        icon = <SVG_Icon_down width="50" height="50"/>;
    }

    return (<>
        <div className="dash-card">
            <h4 className="dash-title">
                {title}
            </h4>
            <p className="dash-valor">
                {valor}
            </p>
            <p className="dash-indice">
                <span>{icon}{Number(indice).toFixed(4)}</span><span>{descricaoIndice}</span>
            </p>
        </div>
    </>);

};

export default Alert;