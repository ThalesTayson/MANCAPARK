
const submit = async ({Method, params={}, body=null, link=""}) =>{
    const csrftoken = getCookie('csrftoken');
    
    if (Method === 'GET') {
        if (Object.keys(params).length === 0){
            return fetch(link);
        }
        link += '?' + new URLSearchParams(params);
    } else if (Method === 'POST') {
        if (body === null){
            body = new FormData();
            let keys = Object.keys(params);
            for (let k of keys) {
                if ( params[k] ) {
                    if (typeof params[k] === 'object'){
                        for (let i in params[k]){
                            body.append(k, params[k][i]);
                        }
                    } else {
                        body.append(k, params[k]);
                    }
                }
            };
        }
    }
    const request = {
        method: Method,
        mode: 'same-origin',
        headers: { 'X-CSRFToken': csrftoken }
    }
    if (body) request['body'] = body;

    return fetch(link, request);
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

export { submit }