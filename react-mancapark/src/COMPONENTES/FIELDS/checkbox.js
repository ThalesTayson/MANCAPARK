import React, { useState, useRef, useEffect } from "react";

const Checkbox = ({ attrs, focus, value, id, label_tag, updateValue }) => {

  const ref = useRef(null);
  
  const onClickCheck = (e) => {
    updateValue(id, (value)? false: true);
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
    <div className="Field-check">
        <input ref={ref} autoFocus={focus} type="checkbox" onClick={onClickCheck} id={id} checked={value} />
        <label htmlFor={id} >{label_tag}</label>
    </div>
  );

};

export default Checkbox;