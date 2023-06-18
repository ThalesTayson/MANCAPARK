import React, { useEffect, useState } from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const Charts = ({ width, height, title, data }) => {

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

      if ( data.length > 0 && labels ){
        const keys = Object.keys(data[0]);
        const _labels = data.map( (row) => { return row[keys[0]] } );
        const _datasets = [];
        for (const key of keys){
          if (keys.indexOf(key) !== 0){
            _datasets.push({
              label: key,
              data: data.map( (row) => { return row[key] } ),
              backgroundColor: 'rgba(255, 99, 132, 0.5)'
            });
          }
        };
        setDatasets(_datasets);
        setLabels(_labels);
      }
    }, [data])
  
    return <Bar width={width} height={height} options={options} data={{labels: labels, datasets: datasets}} />;
}

export default Charts;