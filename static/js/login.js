document.getElementById('login-form').addEventListener('submit', function(event){
    event.preventDefault();

    let email = document.getElementById("correo").value;
    let password = document.getElementById("password").value;

    if (email==="" || password===""){
        alert("Rellene todos los campos.")
        return
    }

    const datosVerificarUser= {
        email: email,
        password: password
    }

    const options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(datosVerificarUser)
    };

    let url= "/verificarCuenta";

    fetch(url, options)
        .then(response => {
            if (!response.ok) {
                throw new Error('Error en la respuesta del servidor');
            }
            return response.json();
        })
        .then(datosVerificarUser =>{
            alert(datosVerificarUser.mensaje)
            document.getElementById("login-form").reset();
            let resultado = datosVerificarUser.resultado
            if (resultado){
                window.location.href = 'http://192.168.1.25:7550/index.html'
            }
        })
        .catch((error) => {
            console.error("Error: ",error);
            alert("Hubo un error al intentar enviar el formulario.")
        });

});

document.querySelector('.view-password').addEventListener('click', function() {
    const passwordInput = document.getElementById('password');
    const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordInput.setAttribute('type', type);
});