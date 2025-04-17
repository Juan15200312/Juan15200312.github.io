document.getElementById('convert_form').addEventListener('submit', function(event){
    event.preventDefault();

    const textDiv = document.getElementById('text');
    const container = document.getElementById('container');

    ['pros', 'titulo', 'descarga'].forEach(id => {
        const elem = document.getElementById(id);
        if (elem) elem.remove();
    });

    const pros = document.createElement('div')
    pros.id = 'pros'
    pros.className = 'pros'
    container.insertBefore(pros,textDiv)

    const barra_carga = document.createElement('progress')
    barra_carga.id='progress'
    pros.appendChild(barra_carga)

    let urlYT = document.getElementById('urlYT').value;
    let format = document.getElementById('format').value;

    if (urlYT ==="" || format==="formato"){
        alert("Seleccione un formato. ")
        return
    }

    const datosUrl = {
        urlYT: urlYT,
        format: format
    }
    const options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(datosUrl)
    };
    let url = '/convertYT'

    fetch(url, options)
        .then(response => {
            if (!response.ok) throw new Error('Error en la respuesta del servidor');
            return response.json();
        })
        .then(datosUrl =>{
            console.log(datosUrl.mensaje)
            while (pros.firstChild){
                    pros.removeChild(pros.firstChild)
            }
            const titulo = document.createElement('div')
                titulo.id = 'titulo'
                container.insertBefore(titulo, textDiv)

            const titulo_des = document.createElement('p')
                titulo_des.id = 'titulo-des'
                titulo_des.textContent = datosUrl.mensaje
                titulo.appendChild(titulo_des)

            if (datosUrl.descargar){
                const descarga = document.createElement('div')
                descarga.id = 'descarga'
                descarga.className = 'descarga'
                container.insertBefore(descarga, textDiv)

                const botonDescarga = document.createElement('button')
                botonDescarga.id = 'botonDescarga'
                botonDescarga.className = 'botonDescarga'
                botonDescarga.textContent = 'Descargar'
                botonDescarga.addEventListener('click', () => descargarMusica(datosUrl.descargar, descarga));
                descarga.appendChild(botonDescarga);
            }
        })
        .catch((error) => {
            console.error("Error: ",error);
            alert("Hubo un error al intentar enviar el formulario.")
        });
});

function descargarMusica(urlDescarga, descarga){
    document.getElementById('urlYT').value = '';
    const titulo = document.getElementById('titulo');
    if (titulo) titulo.remove();
    if (descarga) descarga.remove();
    window.location.href = urlDescarga
}