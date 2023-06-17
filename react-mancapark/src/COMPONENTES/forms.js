import React, { useEffect, useState } from "react";
import Input from './FIELDS/input';
import Select from './FIELDS/select';
import Checkbox from './FIELDS/checkbox';
import TextArea from './FIELDS/text-area';
import Datalist from "./FIELDS/datalist";
import { submit } from "../util";
import '../CSS/Form.css';

const Form = ({ link, messages, update_data }) => {

    const [hasForm, setHasform] = useState(false);
    const [values, setValues] = useState({});
    const [fields, setFields] = useState([]);
    const [title, setTitle] = useState(null);
    const [btn_var, setBtn_var] = useState(null);

    const submit_form = (e) => {
        e.preventDefault();
        let Method = "POST";
        let params = values;
        setFields([]);
        submit({Method, params, link})
            .then((resp) => resp.json())
            .then((resp) => {
                let data = resp;
                if (Object.keys(data).includes('form')) setHasform(true);
                setFields(data.form);
                let { status , msg } = data.message
                messages({status ,msg});
                if (status === 'success') update_data();
            });
    }

    const getValue = (field) => {
        return values[field];
    }

    const updateValue = (field, value) => {
        let _values = values;
        _values[field] = value;
        setValues(_values);
    };

    const get_form = () => {
        let Method = "GET";
        submit({Method, link})
            .then((resp) => resp.json())
            .then((resp) => {
                let data = resp;
                setFields(data.form);
                setTitle(data.title);
                setBtn_var(data.var_btn_value);
            });
    }

    useEffect(()=>{
        if (!hasForm){
            get_form();
        }
    }, [hasForm]);

    return (
        <form className="form-generic" onSubmit={submit_form}>
                <fieldset>
                    <legend>{title}</legend>
                    <div className="fields">
                        {fields.map((field, index)=>{
                            if (field.input_type === 'select'){
                                return <Select attrs={field.attrs} focus={(index === 0)} required={field.is_required} id={field.id.toString()} label_tag={field.label} 
                                    value={field.value} getValue={getValue} updateValue={updateValue} choices={field.options} multiple={field.is_multiple} error={field.error}/>
                            } else if (field.input_type === 'checkbox'){
                                return <Checkbox attrs={field.attrs} focus={(index === 0)} required={field.is_required} id={field.id.toString()} label_tag={field.label} 
                                    value={field.value} getValue={getValue} updateValue={updateValue} error={field.error}/>
                            } else if (field.input_type === 'datalist'){
                                return <Datalist attrs={field.attrs} focus={(index === 0)} required={field.is_required} id={field.id.toString()} label_tag={field.label} 
                                    value={field.value} getValue={getValue} updateValue={updateValue} choices={field.options} error={field.error}/>
                            } else if (field.input_type === 'textArea'){
                                return <></>
                            } else {
                                return <Input attrs={field.attrs} focus={(index === 0)} required={field.is_required} type={field.input_type} id={field.id.toString()} label_tag={field.label} 
                                        value={field.value} getValue={getValue} updateValue={updateValue} error={field.error}/>
                            }
                        })}
                        {fields.map((field, index)=>{
                            if (field.input_type === 'textArea'){
                                return <TextArea attrs={field.attrs} focus={(index === 0)} required={field.is_required} id={field.id.toString()} label_tag={field.label} 
                                    value={field.value} getValue={getValue} updateValue={updateValue} error={field.error}/>
                            }
                        })}
                        
                    </div>
                    <div className="rodape-form">
                        <input type="submit" value={btn_var} />
                    </div>
                </fieldset>
            </form>
    );
};

export default Form;