import React, { useState } from "react";
import SVG_Icon_three_dots from '../SVG/three-dots.svg';
import "../CSS/Tabela.css";

const Menu = ({data, call_function}) =>{
    
    const [choices, setChoices] = useState(<></>)

    const _onFocus = (e) =>{
        setChoices(<ul className="menu-three-dots">
            {data.map((row) => <li><a onClick={() => {call_function(row.link)}}>{row.value}</a></li>)}
        </ul>)
    }
    const _onBlur = (e) =>{
        setTimeout(() => setChoices(<></>), 200)
    }

    return (<>
        <td>
        <button className="btn-icon-three-dots" onFocus={_onFocus} onBlur={_onBlur}>
            <svg width="16" height="16" xmlns="http://www.w3.org/2000/svg">
                <use href='#icon-three-dots' />
            </svg>
        </button>
        {choices}
        </td>
    </>);
}

const Tabela = ({ data , call_function }) => {

    const titles = data[0];

    return (<>
        <div className="container-table">
            <table>
                <thead>
                    <tr>
                        {(titles)? titles.map(value => <th>{value}</th>) : <></>}
                    </tr>
                </thead>
                <tbody>
                    {(data.length > 0 )? data.map(( row, index ) => {
                        if (index == 0) return <></>
                        return <tr>
                            {row.map(value => {
                                if (typeof value == 'object'){
                                    return <Menu data={value} call_function={call_function} />
                                } 
                                return <td>{value}</td>
                            })}
                        </tr>
                    }
                    ) : <></>}
                </tbody>
            </table>
        </div>
        <div style={{display: "none"}}>
            <SVG_Icon_three_dots id={"icon-three-dots"} />
        </div>

    </>);
};

export default Tabela;