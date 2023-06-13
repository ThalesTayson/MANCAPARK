import React, { useEffect, useState } from "react";
import Input from './FIELDS/input';
import Select from './FIELDS/select';
import Checkbox from './FIELDS/checkbox';
import TextArea from './FIELDS/text-area';
import Datalist from "./FIELDS/datalist";
import { submit } from "../util";

const Form = ({ link }) => {

    const [values, setValues] = useState({});
    const [fields, setFields] = useState([]);
    const [title, setTitle] = useState(null);
    const [btn_var, setBtn_var] = useState(null);
    const [errors, setErrors] = useState({});
    const [message, setMessage] = useState(null);

    const submit_form = (e) => {
        e.preventDefault();
        const form = new FormData(e.target);
        submit("POST", body=form, url=link)
            .then((resp) => resp.json())
            .then((resp) => {
                data = resp;
                setFields(data.form);
                setErrors(data.errors);
                setMessage(data.message);
                let _values = values;
                for (let field of data.form){
                    _values[field] = field.value;
                }
                setValues(_values);
            });
    }

    const updateValue = (field, value) => {
        let _values = values;
        _values[field] = value;
        setValues(_values);
    };

    const get_form = () => {
        submit("GET", url=link)
            .then((resp) => resp.json())
            .then((resp) => {
                data = resp;
                setFields(data.form);
                setTitle(data.title);
                setBtn_var(data.var_btn_value);
                let _values = values;
                for (let field of data.form){
                    _values[field] = field.value;
                }
                setValues(_values);
            });
    }

    useEffect(()=>{
        if (fields.length === 0){
            get_form();
        }
    }, [fields]);

    return (
        <form onSubmit={submit_form}>
                <fieldset>
                    <legend>{title}</legend>
                    <div className="fields">
                        {fields.map((field, index)=>{
                            if (field.input_type === 'select'){
                                return <Select attrs={field.attrs} focus={(index === 0)} required={field.is_required} id={field.id.toString()} label_tag={field.label} 
                                    values={values[field.id]} updateValue={updateValue} choices={field.options} multiple={field.multiple}/>
                            } else if (field.input_type === 'checkbox'){
                                return <Checkbox attrs={field.attrs} focus={(index === 0)} required={field.is_required} id={field.id.toString()} label_tag={field.label} 
                                    values={values[field.id]} updateValue={updateValue} />
                            } else if (field.input_type === 'datalist'){
                                return <Datalist attrs={field.attrs} focus={(index === 0)} required={field.is_required} id={field.id.toString()} label_tag={field.label} 
                                    values={values[field.id]} updateValue={updateValue} choices={field.options}/>
                            } else if (field.input_type === 'textArea'){
                                return <></>
                            } else {
                                return <Input attrs={field.attrs} focus={(index === 0)} required={field.is_required} type={field.input_type} id={field.id.toString()} label_tag={field.label} 
                                        values={values[field.id]} updateValue={updateValue} />
                            }
                        })}
                        {fields.map((field, index)=>{
                            if (field.input_type === 'textArea'){
                                return <TextArea attrs={field.attrs} focus={(index === 0)} required={field.is_required} id={field.id.toString()} label_tag={field.label} 
                                    values={values[field.id]} updateValue={updateValue} />
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