function iniciarConCiudadPredeterminada() {
    document.getElementById('ciudad').value = `Madrid`;
    mandarCiudad();
}

window.addEventListener('DOMContentLoaded', iniciarConCiudadPredeterminada);

function mandarCiudad(){
    let ciudad = document.getElementById('ciudad').value;

    if (ciudad===""){
        alert("Rellene con una ciudad. ")
      return
    }
    const datosCiudad = {
      ciudad: ciudad
    }
    const options = {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(datosCiudad)
    };
    let url = '/climaGlobal'

    fetch(url, options)
    .then(response => {
        if (!response.ok) {
            throw new Error('Error en la respuesta del servidor');
        }
        return response.json();
    })
    .then(datosCiudad =>{
        console.log(datosCiudad.mensaje)
        if (datosCiudad.resultado){
            const datosClimaGlobal = datosCiudad.datosClimaGlobal
            console.log(datosClimaGlobal)
            procesarDatos(datosClimaGlobal)
        } else {
            alert(datosCiudad.mensaje)
        }

    })
    .catch((error) => {
        console.error("Error: ",error);
        alert("Hubo un error al intentar enviar el formulario.")
    });


function procesarDatos(datos){
    document.getElementById('nombre-ciudad').innerHTML = datos["nombre"]
    document.getElementById('pais').innerHTML = datos["pais"]

    const offsetSegundos = datos["zona_horaria"];

    function formatearHora(offset) {
        const fecha = new Date();
        const utc = fecha.getTime() + (fecha.getTimezoneOffset() * 60000);

        const horaCiudad = new Date(utc + (offset * 1000));

        return horaCiudad.toLocaleTimeString('es-ES', {
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
        });
    }

    setInterval(() => {
        document.getElementById('hora-actual').innerHTML = `Hora local: ${formatearHora(offsetSegundos)}`;
    }, 1000);

    document.querySelector('.icono-clima').style.backgroundImage = `url(http://192.168.1.25:7550/static/images/images-clima/${datos["icono"]}.png)`
    document.getElementById('descripcion-clima').innerHTML = datos["descripcion"].charAt(0).toUpperCase() +datos["descripcion"].slice(1)
    document.getElementById('temp-actual').innerHTML = datos["temperatura"]
    document.getElementById('temp-min').innerHTML = datos["temperatura_min"]
    document.getElementById('temp-max').innerHTML = datos["temperatura_max"]
    document.getElementById('sensacion-termica').innerHTML = datos["sensacion_termica"]
    document.getElementById('sensacion-termica2').innerHTML = datos["sensacion_termica"]
    document.getElementById('velocidad-viento').innerHTML = datos["viento"]
    document.getElementById('humedad').innerHTML = datos["humedad"]
    document.getElementById('presion').innerHTML = datos["presion"]
    document.getElementById('visibilidad').innerHTML = parseInt(datos["visibilidad"])/10

    function convertirTimestamp(timestamp, offset) {
        const fecha = new Date((timestamp + offset) * 1000);
        return fecha.toLocaleTimeString('es-ES', {
            hour: '2-digit',
            minute: '2-digit'
        });
    }

    const amanecer = convertirTimestamp(datos["amanecer"], offsetSegundos);
    const atardecer = convertirTimestamp(datos["atardecer"], offsetSegundos);
    document.getElementById('horarios-sol').innerHTML = `${amanecer} / ${atardecer}`;

    document.getElementById('ciudad').value = ``
}}



















