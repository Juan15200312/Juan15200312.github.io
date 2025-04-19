function traducirTexto() {
    let texto = document.getElementById('texto').value;
    let idioma = document.getElementById('idioma').value;

    if (texto === "" || idioma === 'seleccione') {
        alert("Rellene todos los campos. ")
        return
    }
    const boton = document.getElementById('boton-enviar');
    boton.disabled = true;

    const datosTraductor = {
        texto: texto,
        idioma: idioma
    }
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(datosTraductor)
    }
    let url = "/traductor"

    fetch(url, options)
        .then(response => {
            if (!response.ok) {
                throw new Error('Error en la respuesta del servidor');
            }
            return response.json();
        })
        .then(datosTraductor => {
            console.log(datosTraductor.mensaje)
            if (datosTraductor.resultadoText) {
                document.getElementById('resultado-tr').value = datosTraductor.mensaje
            }
        })
        .catch((error) => {
            console.error("Error: ", error);
            alert("Hubo un error al intentar enviar el formulario.")
        })
        .finally(() => {
            boton.disabled = false;
        });

}