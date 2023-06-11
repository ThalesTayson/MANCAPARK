import React, { useState } from "react";

const Checkbox = ({ attrs, required, focus, value, id, label_tag }) => {

  const [s_value, setValue] = useState(value);
  
  const onClickCheck = (e) => {
    setValue((s_value)? false: true);
  }

  return (
    <div className="Field-check">
        <input autoFocus={focus} type="checkbox" onClick={onClickCheck} id={id} checked={s_value} />
        <label htmlFor={id} >{label_tag}</label>
    </div>
  );

};

export default Checkbox;