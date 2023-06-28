import React, { useEffect, useState } from 'react';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { Pie } from 'react-chartjs-2';

ChartJS.register(ArcElement, Tooltip, Legend);

const backgroundColors = [
    'rgba(255, 99, 132, 0.2)',
    'rgba(54, 162, 235, 0.2)',
    'rgba(255, 206, 86, 0.2)',
    'rgba(75, 192, 192, 0.2)',
    'rgba(153, 102, 255, 0.2)',
    'rgba(255, 159, 64, 0.2)',
  ]
const borderColors = [
    'rgba(255, 99, 132, 1)',
    'rgba(54, 162, 235, 1)',
    'rgba(255, 206, 86, 1)',
    'rgba(75, 192, 192, 1)',
    'rgba(153, 102, 255, 1)',
    'rgba(255, 159, 64, 1)',
]

const ChartPie = ({ width, height, title, data, label }) => {

    const [labels, setLabels] = useState([]);
    const [datasets, setDatasets] = useState([]);

    const options = {
        responsive: false,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: title,
            },
        },
    };

    useEffect(()=>{

      if ( data.length > 0){
        const keys = Object.keys(data[0]);

        setLabels(data.map( (row) => { return row[keys[0]] } ));
        setDatasets([
            {
              label: label,
              data: data.map( (row) => { return row[keys[1]] } ),
              backgroundColor: data.map( (row, index) => { return backgroundColors[index] } ),
              borderColor: data.map( (row, index) => { return borderColors[index] } ),
              borderWidth: 1,
            },
        ]);

      }
    }, [data])
  
    return <Pie width={width} height={height} options={options} data={{labels: labels, datasets: datasets}} />;
}

export default ChartPie;