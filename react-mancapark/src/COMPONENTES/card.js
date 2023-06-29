import React, { useState } from "react";
import '../CSS/Card.css';
import SVG_Icon_down from '../SVG/arrow-down.svg';
import SVG_Icon_up from '../SVG/arrow-up.svg';

const Card = ({ data }) => {
    const valor = data?.total;
    const title = data?.title;
    const indice = data?.indexes;
    const legendIndice = data?.subtitle;

    let icon = <></>;
    const style = {color: "#837e7e"};

    if (indice > 0){
        icon = <SVG_Icon_up width="50" height="50"/>;
        style["color"] = "#00c300";
    } else if (indice < 0){
        icon = <SVG_Icon_down width="50" height="50"/>;
        style["color"] = "#ff3939";
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
                <span className="indice" style={style}>{icon}{Number(indice).toFixed(2)}{"%"}</span><span className="indice-legend">{" " + legendIndice}</span>
            </p>
        </div>
    </>);

};

export default Card;