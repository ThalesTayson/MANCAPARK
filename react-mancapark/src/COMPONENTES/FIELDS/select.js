import React, { useState, useRef, useEffect } from "react";
import SVG_Exclamation from '../../SVG/exclamation.svg';

const Select = ({ attrs, required, focus, value, updateValue, id, label_tag, choices, multiple, error}) => {

  const ref = useRef(null);

  const keys_choices = Object.keys(choices);

  const onChangeValue = (e) => {
    if (!multiple){
      updateValue(id, e.target.value);
    } else {
      const options = e.target.selectedOptions;
      const values = Array.from(options).map(({ value }) => value);
      updateValue(id, values);
    }
  }

  useEffect(()=>{
    if (ref !== null){
      let keysAttr = Object.keys(attrs);
      for (let key of keysAttr){
        if (!ref.current.getAttribute(key)){
          ref.current.setAttribute(key, attrs[key]);
        }
      }
    }
  }, [ref]);

  return (
    <div className="Field" >
      <select ref={ref} multiple={multiple} required={required} autoFocus={focus} onChange={onChangeValue} id={id}>
          {(value === "")? <option selected value={""}>{"------"}</option> : <option value={""}>{"------"}</option>}
          {keys_choices.map((key)=> {
            if (value === key) {
              return <option selected value={value}>{choices[key]}</option>
            } else {
              return <option value={key}>{choices[key]}</option>
            }
          })}
      </select>
      <label htmlFor={id}>{label_tag}</label>
      {(error === "")? <></> : <span className="icon_error" title={error}><SVG_Exclamation /></span>}
    </div>
  );

};

export default Select;