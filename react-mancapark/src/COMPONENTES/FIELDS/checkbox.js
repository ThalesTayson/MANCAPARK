import React, { useState, useRef, useEffect } from "react";
import SVG_Exclamation from '../../SVG/exclamation.svg';

const Checkbox = ({ attrs, focus, value, getValue, updateValue, id, label_tag, error}) => {

  const ref = useRef(null);

  const [init, setInit] = useState(true);

  const [_get, setGet] = useState(false);
  const [_value, setValue ] = useState(value);

  const onClickCheck = (e) => {
    updateValue(id, (_value)? false: true);
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
    <div className="Field-check">
        <input ref={ref} autoFocus={focus} type="checkbox" onClick={onClickCheck} id={id} checked={_value} />
        <label htmlFor={id} >{label_tag}</label>
        {(error === "")? <></> : <span className="icon_error" title={error}><SVG_Exclamation /></span>}
    </div>
  );

};

export default Checkbox;