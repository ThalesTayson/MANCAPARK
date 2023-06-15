import React, { useState, useRef, useEffect } from "react";
import SVG_Exclamation from '../../SVG/exclamation.svg';

const Input = ({ type, attrs, required, focus, value, updateValue, id, label_tag, error }) => {

  const ref = useRef(null);

  const [_value, setValue ] = useState(value);

  const onInputValue = (e) => {
    setValue(e.target.value);
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
  }, [ref, _value]);

  return (
    <div className={(type === 'hidden')? 'Field Hidden': 'Field'}>
      <input ref={ref} autoFocus={focus} type={type} autoComplete={false} onInput={onInputValue} 
      required={required} id={id} value={_value} />
      <label htmlFor={id}>{label_tag}</label>
      <span class="bar"></span>
      {(error === "")? <></> : <span className="icon_error" title={error}><SVG_Exclamation /></span>}
    </div>
  );

};

export default Input;