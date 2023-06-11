import React from "react";

class TextArea extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: this.props.value
    };
  }
  onInputValue = (e) => {
    this.setState({value: e.target.value});
  }
  style = () =>{
    let style = {};
    if (this.props.width){
      style = {width: this.props.width + 'px'};
    }
    return style
  }
  render() {
    return (
        <div className="Field" style={this.style()}>
            <textarea autoFocus={this.props.focus} autoComplete="false" onInput={this.onInputValue} 
              required={this.props.required} id={this.props.name} rows={3} cols={30}>{this.state.value}</textarea>
            <label htmlFor={this.props.name}>{this.props.label_tag}</label>
        </div>
    );
  }
}

export default TextArea;