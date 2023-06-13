import React, { useState, useRef, useEffect } from "react";

const Datalist = ({ attrs, required, focus, value, updateValue, id, label_tag, choices }) => {

  const ref = useRef(null);

  const keys_choices = Object.keys(choices);

  const onChangeValue = (e) => {
    let _value = "";
    try {
      _value = document.getElementById("option_datalist_" + e.target.value).getAttribute("_value");
    } catch (error) {
      _value = "";
    }
    updateValue(id, _value);
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
        <input ref={ref} required={required} onChange={onChangeValue} autoFocus={focus} id={id}
        list={'choices_' + id} value={choices[value]} />
        <datalist id={'choices_' + id}>
          {keys_choices.map((key)=> {return <option id={"option_datalist_" + choices[key]} _value={key} value={choices[key]}/>})}
        </datalist>
        <label htmlFor={id}>{label_tag}</label>
    </div>
  );

};

export default Datalist;