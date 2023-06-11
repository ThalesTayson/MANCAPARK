import React, { useState } from "react";

const Datalist = ({ attrs, required, focus, value, id, label_tag, choices }) => {

  const [s_value, setValue] = useState(value);
  
  const onChangeValue = (e) => {
    setValue(e.target.value);
  }

  return (
    <div className="Field" >
        <input required={required} onChange={onChangeValue} autoFocus={focus} id={id}
        list={'choices_' + id} value={s_value} />
        <datalist id={'choices_' + id}>
          {choices.map((row)=> {return <option value={row.text}/>})}
        </datalist>
        <label htmlFor={id}>{label_tag}</label>
    </div>
  );

};

export default Datalist;