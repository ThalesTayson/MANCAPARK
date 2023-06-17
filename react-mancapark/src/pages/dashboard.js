import React, { useEffect, useState } from "react";
import { submit } from "../util";
import Chart from 'chart.js/auto'
 
const Dashboard = ({ message }) => {

    const [data, setData] = useState([]);
    const [graficoFaturamento, setFaturamento] = useState([]);
    const [graficoEntradas, setEntradas] = useState([]);

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
                graficoEntradas(_data.data);
            });
    }

    const chart = () => {
        new Chart(
            document.getElementById('acquisitions'),
            {
              type: 'bar',
              data: {
                labels: data.map(row => row.year),
                datasets: [
                  {
                    label: 'Acquisitions by year',
                    data: data.map(row => row.count)
                  }
                ]
              }
            }
          );
    }
    
    useEffect(()=>{


    })

    return (
        <>
        <header>
            <span>{"Dashboard"}</span>
        </header>
        <section>

        </section>
        <section></section>
        </>
    );
};

export default Dashboard;