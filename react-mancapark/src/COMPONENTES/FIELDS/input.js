import React, { useState, useRef, useEffect } from "react";

const Input = ({ type, attrs, required, focus, values, updateValue, id, label_tag }) => {

  const ref = useRef(null);
  
  const onInputValue = (e) => {
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
    <div className={(type === 'hidden')? 'Field Hidden': 'Field'}>
      <input ref={ref} autoFocus={focus} type={type} autoComplete={false} onInput={onInputValue} 
      required={required} id={id} value={value} />
      <label htmlFor={id}>{label_tag}</label>
    </div>
  );

};

export default Input;