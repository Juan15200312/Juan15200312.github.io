document.getElementById('reset-form').addEventListener('submit', function (event){
   event.preventDefault();

   let email = document.getElementById('email').value;

   if (email===''){
       alert('Rellene el campo de correo electronico. ')
       return
   }

   const datosResetPasswordCorreo = {
       email: email
   }

   const option = {
       method: 'POST',
       headers: {
           'Content-Type': 'application/json'
       },
       body: JSON.stringify(datosResetPasswordCorreo)
   }

   let url = '/resetPasswordCorreo'

    fetch(url, option)
        .then(response => {
           if (!response.ok){
               throw new Error('Error en la respuesta del servidor. ')
           }
           return response.json()
        })
        .then(datosResetPasswordCorreo => {
            alert(datosResetPasswordCorreo.mensaje);
            document.getElementById('reset-form').reset();
            let resultado = datosResetPasswordCorreo.resultado
            if (resultado){
                window.location.href = 'http://192.168.1.25:7550/login.html'
            }
        })
        .catch((error)=> {
            console.error('Error: ', error)
            alert('Hubo un error al intentar enviar el formulario. ')
        });

});

document.querySelector('.view-password').addEventListener('click', function() {
    const passwordInput = document.getElementById('password');
    const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordInput.setAttribute('type', type);
});