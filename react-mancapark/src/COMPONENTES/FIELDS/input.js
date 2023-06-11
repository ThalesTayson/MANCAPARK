import React from "react";
import mask from '../maskaras';

class Input extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: this.props.value,

    };
  }
  onInputValue = (e) => {
    let data = e.nativeEvent.data;
    let value = (this.state.value)? this.state.value : null;
    if (this.props.mask && e.nativeEvent.inputType === 'insertText') {
      value = mask[this.props.mask](value, data);
    } else if ( this.props.mask && e.nativeEvent.inputType === 'deleteContentBackward'){
      value = mask[this.props.mask](value, 'bkspc');
    }
    this.setState({value: (this.props.mask)? value : e.target.value});
  }
  style = () =>{
    let style = {maxHeight:'20px'};
    if (this.props.width){
      style['width'] = this.props.width + 'px';
      style = {width: this.props.width + 'px'};
    } else {
      if (this.props.type === 'text'){
        style['width'] = '450px';
      }
    }
    return style
  }
  render() {
    let input, _step, _type;
    if (this.props.type === 'decimal'){
      _type = 'number';
      _step = 'any';
    } else if (this.props.type === 'number')  {
      _step = '1';
      _step = 'number';
    } else {
      _type = this.props.type;
    };
    
    if (this.props.mask){
      input = <input autoFocus={this.props.focus} type={'text'} autoComplete="false" onInput={this.onInputValue} required={this.props.required} id={this.props.name} 
      value={mask[this.props.mask]((this.state.value)? this.state.value: 0)} />
    }else {
      input = <input maxLength={this.props.maxLength} autoFocus={this.props.focus} step={_step} type={_type} autoComplete="false" onInput={this.onInputValue} 
      required={this.props.required} id={this.props.name} value={this.state.value} />
    }
    return (
        <div className={(this.props.type === 'hidden')? 'Field Hidden': 'Field'} style={this.style()}>
            {input}
            <label htmlFor={this.props.name}>{this.props.label_tag}</label>
        </div>
    );
  }
}

export default Input;