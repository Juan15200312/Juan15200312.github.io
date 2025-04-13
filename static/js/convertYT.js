document.getElementById('convert_form').addEventListener('submit', function(event){
    event.preventDefault();

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
            if (!response.ok) {
                throw new Error('Error en la respuesta del servidor');
            }
            return response.json();
        })
        .then(datosUrl =>{
            alert(datosUrl.mensaje)
            if (datosUrl.descarga){
                window.location.href = datosUrl.descarga
                document.getElementById('convert_form').reset();
            }
        })
        .catch((error) => {
            console.error("Error: ",error);
            alert("Hubo un error al intentar enviar el formulario.")
        });

});
