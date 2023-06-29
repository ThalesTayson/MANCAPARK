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

    const [parked, setParked] = useState({});
    const [entrances, setEntrances] = useState({});
    const [payments_receive, setReceive] = useState({});
    const [payments_received, setReceived] = useState({});

    const [graficoFaturamento, setFaturamento] = useState([]);

    const [graficoEntradas, setEntradas] = useState([]);

    const [graficoTipos, setTipos] = useState([]);

    const get_dados = () => {
        let Method = "GET";
        let link = "/dashboard/dados";
        submit({Method, link})
            .then((resp) => resp.json())
            .then((resp) => {
                let _data = resp;
                setParked(_data.data.parked);
                setEntrances(_data.data.entrances);
                setReceive(_data.data.payments_receive);
                setReceived(_data.data.payments_received);
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
        let link = "/dashboard/grafico-entradas";
        submit({Method, link})
            .then((resp) => resp.json())
            .then((resp) => {
                let _data = resp;
                setEntradas(_data.data);
            });
    }

    const get_graficoTipos = () => {
        let Method = "GET";
        let link = "/dashboard/grafico-tipos";
        submit({Method, link})
            .then((resp) => resp.json())
            .then((resp) => {
                let _data = resp;
                setTipos(_data.data);
            });
    }

    useEffect(()=>{
        if (graficoEntradas.length === 0){
            get_graficoEntradas();
        }
        if (graficoFaturamento.length === 0){
            get_graficoFaturamento();
        }
        if (graficoTipos.length === 0){
            get_graficoTipos();
        }
        if (Object.keys(parked).length === 0){
            get_dados();
        }
    }, [graficoEntradas, graficoFaturamento, graficoTipos, parked] )

    return (
        <>
        <header>
            <span>{"Dashboard"}</span>
        </header>
        <section className="dash-row">
            <div className="dash-cards">
                <Card data={parked}/>
                <Card data={payments_receive}/>
                <Card data={entrances}/>
                <Card data={payments_received}/>
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
                    title={"Tipos Frequentes (Ultimos 30 dias)"} 
                    data={graficoTipos} 
                />
            </div>
            
        </section>
        </>
    );
};

export default Dashboard;