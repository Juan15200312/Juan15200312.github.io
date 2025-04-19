function procesarDatosMoneda(){

    let importe = document.getElementById('importe').value;
    let moneda1 = document.getElementById('moneda1').value;
    let moneda2 = document.getElementById('moneda2').value;

    if (importe==="" || moneda1==="seleccione" || moneda2==="seleccione"){
        alert("Rellene todos los campos. ")
        return
    }

    const boton = document.getElementById('botonE');
    boton.disabled = true;

    ['titulo', 'importe_final', 'fecha_cambio'].forEach(id => {
        const elem = document.getElementById(id);
        if (elem) elem.remove();
    });

    const datosMonedasHtml = {
        importe: importe,
        moneda1: moneda1,
        moneda2: moneda2
    }
    const options = {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(datosMonedasHtml)
    }
    let url = '/conversionMoneda'

    fetch(url, options)
    .then(response => {
        if (!response.ok) {
            throw new Error('Error en la respuesta del servidor');
        }
        return response.json();
    })
    .then(datosMonedasHtml =>{
        console.log(datosMonedasHtml.mensaje)
        if (datosMonedasHtml.resultado){
            const titulo = document.createElement('h3');
            titulo.id = 'titulo'
            titulo.textContent = 'Resultado de la conversion: '
            document.getElementById('resultado_moneda').appendChild(titulo)

            const importe_final = document.createElement('p')
            importe_final.id = 'importe_final'
            importe_final.textContent = "Importe final: "+convertirMoneda(datosMonedasHtml.datosMoneda1, datosMonedasHtml.datosMoneda2, importe)
            document.getElementById('resultado_moneda').appendChild(importe_final)

            const fecha_cambio = document.createElement('p')
            fecha_cambio.id = 'fecha_cambio'
            fecha_cambio.textContent = "Última actualización: "+datosMonedasHtml.datosMoneda2["ultimo_cambio"]
            document.getElementById('resultado_moneda').appendChild(fecha_cambio)

        }else {
            alert(datosMonedasHtml.mensaje)
        }
    })
    .catch((error) => {
        console.error("Error: ",error);
        alert("Hubo un error al intentar enviar el formulario.")
    })
    .finally(() => {
        boton.disabled = false;
    });

}

function convertirMoneda(moneda1, moneda2, importe){
    let mon1 = parseFloat(moneda2["cambio_dolar"])
    let mon2 = parseFloat(moneda1["cambio_dolar"])
    let cambio = mon1/mon2
    if (moneda2["simbolo"]==="before"){
        return importe_final = Number((parseFloat(importe) * cambio).toFixed(2)) + " " + moneda2["simbolo"]
    }else{
        return importe_final = moneda2["simbolo"] + " " + Number((parseFloat(importe) * cambio).toFixed(2))
    }
}