import React, { useState, useRef, useEffect } from "react";
import SVG_Exclamation from '../../SVG/exclamation.svg';

const Select = ({ attrs, required, focus, value, updateValue, id, label_tag, choices, multiple, error}) => {

  const ref = useRef(null);

  const keys_choices = Object.keys(choices);

  const [_value, setValue ] = useState(value);

  const onChangeValue = (e) => {
    if (!multiple){
      setValue(e.target.value);
    } else {
      const options = e.target.selectedOptions;
      const values = Array.from(options).map(({ value }) => value);
      setValue(values);
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
    updateValue(id, _value);
  }, [ref], _value);

  return (
    <div className="Field" >
      <select ref={ref} multiple={multiple} required={required} autoFocus={focus} onChange={onChangeValue} id={id}>
          {(_value === "")? <option selected value={""}>{""}</option> : <option value={""}>{""}</option>}
          {keys_choices.map((key)=> {
            try {
              if ((!multiple) && _value === key) {
                return <option selected value={value}>{choices[key]}</option>
              } else if (_value.includes(key)){
                return <option value={key}>{choices[key]}</option>
              }
            } catch (error) {
              console.log("multiple are blank");  
            }
            return <option value={key}>{choices[key]}</option>
          })}
      </select>
      <label htmlFor={id}>{label_tag}</label>
      <span class="bar"></span>
      {(error === "")? <></> : <span className="icon_error" title={error}><SVG_Exclamation /></span>}
    </div>
  );

};

export default Select;