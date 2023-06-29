window.addEventListener('load', () =>{
    document.getElementById('btn_open_login').addEventListener('click', () => {
        const main = document.getElementsByTagName('main')[0];
        main.classList.remove('hidden-mobile');
    });
    document.getElementById('btn_cancelar').addEventListener('click', () => {
        const main = document.getElementsByTagName('main')[0];
        main.classList.add('hidden-mobile');
    });
});