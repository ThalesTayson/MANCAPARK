import React, { useState } from "react";

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
            <svg id={"icon-three-dots"} xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                <path d="M9.5 13a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/>
            </svg>
        </div>

    </>);
};

export default Tabela;