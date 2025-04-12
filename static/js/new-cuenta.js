document.getElementById('crear_form').addEventListener('submit', function(event){
    event.preventDefault();

    let nombre = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let ter_cond = document.getElementById("ter_cond").checked;

    if (nombre==="" || email==="" || password===""){
        alert("Rellene todos los campos. ")
        return
    }
    if (!ter_cond){
        alert("Lea y acepte los terminos y condiciones.")
        return;
    }

    const datosCuentaNueva = {
        nombre: nombre,
        email: email,
        password: password
    }

    const options = {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(datosCuentaNueva)
    }

    let url = "/crearCuenta"

    fetch(url, options)
        .then(response => {
           if (!response.ok){
               throw new Error('Error en la respuesta del servidor')
           }
           return response.json()
        })
        .then(datosCuentaNueva => {
            alert(datosCuentaNueva.mensaje)
            document.getElementById('crear_form').reset();
            let resultado = datosCuentaNueva.resultado
            if (resultado){
                window.location.href = 'http://192.168.1.25:7550/login.html'
            }
        })
        .catch((error) => {
            console.error("Error: ",error)
            alert("Hubo un error al intentar enviar el formulario.")
        });

});

document.querySelector('.view-password').addEventListener('click', function() {
    const passwordInput = document.getElementById('password');
    const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordInput.setAttribute('type', type);
});