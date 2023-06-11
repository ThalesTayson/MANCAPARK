import React, { useState } from "react";

const Select = ({ attrs, required, focus, value, id, label_tag, choices }) => {

  const [s_value, setValue] = useState(value);
  
  const onChangeValue = (e) => {
    setValue(e.target.value);
  }

  return (
    <div className="Field" >
      <select required={required} autoFocus={focus} onChange={onChangeValue} id={id}>
          {choices.map((row)=> {
            if (s_value === row.value) {
              return <option selected value={row.value}>{row.text}</option>
            } else {
              return <option value={row.value}>{row.text}</option>
            }
          })}
      </select>
      <label htmlFor={id}>{label_tag}</label>
    </div>
  );

};

export default Select;