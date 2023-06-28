import React, { useEffect, useState } from "react";
import { submit } from "../util";
import Card from "../COMPONENTES/card";
import Bar from "../COMPONENTES/Charts/ChartBar";
import Pie from "../COMPONENTES/Charts/ChartPie";
import "../CSS/Dashboard.css";

const is_mobile = () => {
    if (window.screen.width < window.screen.height){
        return true;
    }
    return false;
};

const getScreen_dash_row = () => {
    let w ,h;
    h = (document.body.clientHeight - 70) / 2;
    if (is_mobile()){
        w = screen.width - 20;
    } else {
        w = document.body.clientWidth - 200;
    }
    return {w, h};
    
}
const Dashboard = ({ message }) => {

    const scren_dash_row = getScreen_dash_row();

    const [data, setData] = useState({});

    const [graficoFaturamento, setFaturamento] = useState([
        {"data":"12/07", "VALOR": "44.3"},{"data":"13/07", "VALOR": "30.3"},{"data":"14/07", "VALOR": "41.3"},
        {"data":"15/07", "VALOR": "44.3"},{"data":"16/07", "VALOR": "30.3"},{"data":"17/07", "VALOR": "41.3"},
        {"data":"18/07", "VALOR": "44.3"},{"data":"19/07", "VALOR": "30.3"},{"data":"20/07", "VALOR": "41.3"},
        {"data":"21/07", "VALOR": "44.3"},{"data":"22/07", "VALOR": "30.3"},{"data":"23/07", "VALOR": "41.3"},
        {"data":"12/07", "VALOR": "44.3"},{"data":"13/07", "VALOR": "30.3"},{"data":"14/07", "VALOR": "41.3"},
        {"data":"15/07", "VALOR": "44.3"},{"data":"16/07", "VALOR": "30.3"},{"data":"17/07", "VALOR": "41.3"},
        {"data":"18/07", "VALOR": "44.3"},{"data":"19/07", "VALOR": "30.3"},{"data":"20/07", "VALOR": "41.3"},
        {"data":"21/07", "VALOR": "44.3"},{"data":"22/07", "VALOR": "30.3"},{"data":"23/07", "VALOR": "41.3"}
    ]);

    const [graficoEntradas, setEntradas] = useState([
        {"data":"12/07", "VALOR": "44.3"},
        {"data":"13/07", "VALOR": "30.3"},
        {"data":"12/07", "VALOR": "44.3"},
        {"data":"13/07", "VALOR": "30.3"},
        {"data":"12/07", "VALOR": "44.3"},
        {"data":"13/07", "VALOR": "30.3"},
        {"data":"12/07", "VALOR": "44.3"},
        {"data":"13/07", "VALOR": "30.3"},
        {"data":"14/07", "VALOR": "41.3"}
    ]);

    const [graficoTipos, setTipos] = useState([
        {"key":"Carro", "qtd": "22"},
        {"key":"Moto", "qtd": "15"},
        {"key":"Caminhão", "qtd": "3"},
    ]);

    const get_dados = () => {
        let Method = "GET";
        let link = "/dashboard/dados";
        submit({Method, link})
            .then((resp) => resp.json())
            .then((resp) => {
                let _data = resp;
                setData(_data.data);
            });
    }

    const get_graficoFaturamento = () => {
        let Method = "GET";
        let link = "/dashboard/grafico-faturamento";
        submit({Method, link})
            .then((resp) => resp.json())
            .then((resp) => {
                let _data = resp;
                setFaturamento(_data.data);
            });
    }

    const get_graficoEntradas = () => {
        let Method = "GET";
        let link = "/estacionamento/grafico-entradas";
        submit({Method, link})
            .then((resp) => resp.json())
            .then((resp) => {
                let _data = resp;
                setEntradas(_data.data);
            });
    }

    useEffect(()=>{

    }, [] )

    return (
        <>
        <header>
            <span>{"Dashboard"}</span>
        </header>
        <section className="dash-row">
            <div className="dash-cards">
                <Card title={"Estacionados"} valor={50} indice={1.33934532} legendIndice={" em relação das ultimas 24h."}/>
                <Card title={"Total a Receber"} valor={"R$ 458,30"} indice={0} legendIndice={" em relação as ultimas 24h."}/>
                <Card title={"Total de Entradas Hoje"} valor={247} indice={4.33934532} legendIndice={" em relação aos ultimos 30 dias."}/>
                <Card title={"Total Recebido"} valor={"R$ 1350,80"} indice={-2.33934532} legendIndice={" em relação aos ultimos 30 dias."}/>
            </div>
            <div className="chart">
                <Bar 
                    width={(is_mobile())? scren_dash_row.w - 20 : (scren_dash_row.w * .5) - 20} 
                    height={(is_mobile())? (scren_dash_row.h * 0.8) - 60 : scren_dash_row.h - 20} 
                    title={"Entradas no Estacionamento"} 
                    data={graficoEntradas} 
                />
            </div>
        
        </section>
        <section className="dash-row">
            <div className="chart">
                <Bar 
                    width={(is_mobile())? scren_dash_row.w - 20 : scren_dash_row.w * .7} 
                    height={(is_mobile())? (scren_dash_row.h * 0.8) - 60 : scren_dash_row.h - 20} 
                    title={"Faturamento"} 
                    data={graficoFaturamento} 
                />
            </div>
            <div className="chart">
                <Pie 
                    width={(is_mobile())? (scren_dash_row.w) - 20 : (scren_dash_row.w * .3) - 60} 
                    height={(is_mobile())? (scren_dash_row.w * 0.7) :scren_dash_row.h - 20} 
                    title={"Tipos Frequentes"} 
                    data={graficoTipos} 
                />
            </div>
            
        </section>
        </>
    );
};

export default Dashboard;