import React, { useState } from "react";
import SVG_Icon_error from '../SVG/error.svg';
import SVG_Icon_info from '../SVG/info.svg';
import SVG_Icon_success from '../SVG/success.svg';
import SVG_Icon_alert from '../SVG/alert.svg';
import '../CSS/Alert.css';

const Alert = ({ motivo, message }) => {
    const _style = {};
    
    let icon = <></>;

    switch (motivo) {
        case "error":
            _style["color"] = "red";
            icon = <SVG_Icon_error width="50" height="50"/>;
            break;
        case "alert":
            _style["color"] = "yellow";
            icon = <SVG_Icon_alert width="50" height="50"/>;
            break;
        case "success":
            _style["color"] = "green";
            icon = <SVG_Icon_success width="50" height="50"/>;
            break;
        default:
            _style["color"] = "white";
            icon = <SVG_Icon_info width="50" height="50"/>;
            break;
    }

    return (<>
        <div className="message-alert">
            <span className="main-message">
                <span style={_style} className="icon">{icon}</span>
                <span className="message">{message}</span>
            </span>
        </div>
    </>);

};

export default Alert;