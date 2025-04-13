document.getElementById('formulario').addEventListener('submit', function(event){
    event.preventDefault();

    let nombre = document.getElementById("nombre").value;
    let correo = document.getElementById("correo").value;
    let mensaje = document.getElementById("mensaje").value;

    if (nombre==="" || correo==="" || mensaje.length<2){
        alert("Rellene todos los campos.")
        return
    }
    const datos = {
        nombre: nombre,
        correo: correo,
        mensaje: mensaje
    };
    const options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(datos)
    };

    let url= "/enviar";

    fetch(url, options)
        .then(response => {
            if (!response.ok) {
                throw new Error('Error en la respuesta del servidor');
            }
            return response.json();
        })
        .then(data => {
            alert(data.mensaje);
            document.getElementById("formulario").reset();
        })
        .catch((error) =>{
            console.error("Error:" , error);
            alert("Hubo un error al intentar enviar el formulario. ");
        });

});

document.querySelectorAll('nav a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);
        const headerHeight = document.querySelector('header').offsetHeight;

        window.scrollTo({
            top: targetElement.offsetTop - headerHeight,
            behavior: 'smooth'

        });
    });
});

function smoothScroll(target) {
  const element = document.querySelector(target);
  element.scrollIntoView({
    behavior: 'smooth',
    block: 'start'
  });
}

