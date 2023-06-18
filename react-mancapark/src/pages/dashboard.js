import React, { useEffect, useState } from "react";
import { submit } from "../util";
import Card from "../COMPONENTES/card";
import Charts from "../COMPONENTES/graph";
import "../CSS/Dashboard.css";

const getScreen_dash_row = () => {
    const w = document.body.clientWidth - 200;
    const h = (document.body.clientHeight - 70) / 2;
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
    const [graficoEntradas, setEntradas] = useState([{"data":"12/07", "VALOR": "44.3"},{"data":"13/07", "VALOR": "30.3"},{"data":"14/07", "VALOR": "41.3"}]);

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
                <Card title={"Total a Receber"} valor={"R$ 458,30"} indice={7.54834532} legendIndice={" em relação as ultimas 24h."}/>
                <Card title={"Total de Entradas Hoje"} valor={247} indice={4.33934532} legendIndice={" em relação aos ultimos 30 dias."}/>
                <Card title={"Total Recebido"} valor={"R$ 1350,80"} indice={2.33934532} legendIndice={" em relação aos ultimos 30 dias."}/>
            </div>
            <div className="chart-entradas">
                <Charts 
                    width={scren_dash_row.w * .5} 
                    height={scren_dash_row.h - 40} 
                    title={"Entradas no Estacionamento"} 
                    data={graficoEntradas} 
                />
            </div>
        
        </section>
        <section className="dash-row">
            <div className="chart-faturamento">
                <Charts 
                    width={scren_dash_row.w * .7} 
                    height={scren_dash_row.h - 40} 
                    title={"Faturamento"} 
                    data={graficoFaturamento} 
                />
            </div>
        </section>
        </>
    );
};

export default Dashboard;