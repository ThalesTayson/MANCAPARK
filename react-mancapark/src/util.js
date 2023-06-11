async function submit(Method,params={}, body=null, url="") {
    const csrftoken = getCookie('csrftoken');
    
    if (Method === 'GET') {
        if (Object.keys(params).length === 0){
            return fetch(url);
        }
        url += '?' + new URLSearchParams(params);
    } else if (Method === 'POST') {
        if (body === null){
            body = new FormData();
            let keys = Object.keys(params);
            for (let k of keys) {
                if ( params[k] ) {
                    body.append(k, params[k]);
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

    return fetch(url, request);
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