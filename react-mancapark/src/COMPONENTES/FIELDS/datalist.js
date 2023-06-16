import React, { useState, useRef, useEffect } from "react";
import SVG_Exclamation from '../../SVG/exclamation.svg';

const Datalist = ({ attrs, required, focus, value, updateValue, id, label_tag, choices, error }) => {

  const ref = useRef(null);

  const [_get, setGet] = useState(true);
  const [_value, setValue ] = useState("");

  const keys_choices = Object.keys(choices);

  const onChangeValue = (e) => {
    let _value_ = "";
    try {
      _value_ = document.getElementById("option_datalist_" + e.target.value).getAttribute("_value");
    } catch (error) {
      _value_ = "";
    }
    updateValue(id, _value_);
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
    if (_get){
      setValue(value(id));
      setGet(false);
    }
  }, [ref, _get]);

  return (
    <div className="Field" >
        <input ref={ref} required={required} onChange={onChangeValue} autoFocus={focus} id={id}
        list={'choices_' + id} value={choices[_value]} />
        <datalist id={'choices_' + id}>
          {keys_choices.map((key)=> {return <option id={"option_datalist_" + choices[key]} _value={key} value={choices[key]}/>})}
        </datalist>
        <span class="bar"></span>
        <label htmlFor={id}>{label_tag}</label>
        {(error === "")? <></> : <span className="icon_error" title={error}><SVG_Exclamation /></span>}
    </div>
  );

};

export default Datalist;