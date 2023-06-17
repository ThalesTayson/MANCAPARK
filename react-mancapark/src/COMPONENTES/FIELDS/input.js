import React, { useState, useRef, useEffect } from "react";
import SVG_Exclamation from '../../SVG/exclamation.svg';

const Input = ({ type, attrs, required, focus, value, getValue, updateValue, id, label_tag, error }) => {

  const ref = useRef(null);

  const [init, setInit] = useState(true);

  const [_get, setGet] = useState(false);
  const [_value, setValue ] = useState(value);

  const onInputValue = (e) => {
    updateValue(id, e.target.value);
    setGet(true);
  }

  useEffect(()=>{
    if (init) {
      updateValue(id, value);
      setInit(false);
    }
    if (ref !== null){
      let keysAttr = Object.keys(attrs);
      for (let key of keysAttr){
        if (!ref.current.getAttribute(key)){
          ref.current.setAttribute(key, attrs[key]);
        }
      }
    }
    if (_get){
      setValue(getValue(id));
      setGet(false);
    }
  }, [ref, _get, init]);

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