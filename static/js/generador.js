function iniciarGeneradorQR() {
    let urlQR = document.getElementById('urlQR').value;

    if (urlQR === "") {
        alert("Rellene los campos. ")
        return
    }

    ['descrip-titulo', 'imagenGeneradaQR', 'botones-dinamicos', 'descargarImg', 'descrip-texto'].forEach(id => {
        const elem = document.getElementById(id);
        if (elem) elem.remove();
    });

    const datosGenerador = {
        urlQR: urlQR
    }
    const options = {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(datosGenerador)
    };
    let url = '/generadorQR'

    fetch(url, options)
        .then(response => {
            if (!response.ok) {
                throw Error('Error en la respuesta del servidor. ')
            }
            return response.json()
        })
        .then(datosGenerador => {
            console.log(datosGenerador.mensaje)
            console.log(datosGenerador.urlImagen)
            if (datosGenerador.urlImagen) {
                const titulo = document.createElement('h1');
                titulo.id = 'descrip-titulo'
                titulo.textContent = 'Imagen QR generada'
                document.getElementById('text').appendChild(titulo)

                const cuadroImagen = document.createElement('div')
                cuadroImagen.id = 'imagenGeneradaQR'
                cuadroImagen.className = 'imagenGeneradaQR'
                document.getElementById('text').appendChild(cuadroImagen)

                document.querySelector('.imagenGeneradaQR').style.width = '280px'
                document.querySelector('.imagenGeneradaQR').style.height = '280px'
                cuadroImagen.style.backgroundImage = `url(${datosGenerador.urlImagen})`

                const botones = document.createElement('div')
                botones.id = 'botones-dinamicos'
                botones.className = 'botones'
                document.getElementById('text').appendChild(botones)

                const boton = document.createElement('button');
                boton.id = 'descargarImg';
                boton.textContent = 'Descargar Imagen';
                boton.addEventListener('click', () => descargarImagen(datosGenerador.urlDescarga));
                botones.appendChild(boton);

                const descrip = document.createElement('p')
                descrip.id = 'descrip-texto'
                descrip.textContent = 'Este generador de imagenes QR te permite convertir tus url o textos en codigo QR y descargarlos GRATIS.'
                document.getElementById('text').appendChild(descrip)
                document.getElementById('urlQR').value = '';
            }
        })
        .catch((error) => {
            console.error("Error:", error);
            alert("Hubo un error al intentar enviar el formulario. ");
        });
}

function descargarImagen(urlDescarga) {
    window.location.href = urlDescarga;
}