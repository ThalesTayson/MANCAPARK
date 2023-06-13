import React, { useState, useRef, useEffect } from "react";

const Select = ({ attrs, required, focus, value, updateValue, id, label_tag, choices }) => {

  const ref = useRef(null);

  const keys_choices = Object.keys(choices);

  const onChangeValue = (e) => {
    updateValue(id, e.target.value);
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
      <select ref={ref} required={required} autoFocus={focus} onChange={onChangeValue} id={id}>
          {keys_choices.map((key)=> {
            if (value === key) {
              return <option selected value={key}>{choices[key]}</option>
            } else {
              return <option value={key}>{choices[key]}</option>
            }
          })}
      </select>
      <label htmlFor={id}>{label_tag}</label>
    </div>
  );

};

export default Select;