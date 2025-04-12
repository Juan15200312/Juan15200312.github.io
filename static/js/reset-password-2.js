document.getElementById('reset-form').addEventListener('submit' ,function (event){
   event.preventDefault();

   let email = document.getElementById('email').value;
   let password = document.getElementById('password').value;

   if (email==='' || password===''){
       alert('Rellene el campo de correo electronico. ')
       return
   }
   const datosResetPassword = {
       email: email,
       password: password
   }
   const options = {
       method: 'POST',
       headers: {
           'Content-Type': 'application/json'
       },
       body: JSON.stringify(datosResetPassword)
   }
   let url = '/resetPassword'

   fetch(url, options)
       .then(response => {
           if (!response.ok){
               throw new Error ('Error en la respuesta del servidor')
           }
           return response.json()
       })
       .then(datosResetPassword => {
           alert(datosResetPassword.mensaje)
           document.getElementById('reset-form').reset();
           let resultado = datosResetPassword.resultado
            if (resultado){
                window.location.href = 'http://192.168.1.25:7550/login.html'
            }
       })
       .catch(error => {
           console.error('Error: ',error)
           alert('OCurrio un error al intentar enviar el formulario. ')
       })

});

document.querySelector('.view-password').addEventListener('click', function() {
    const passwordInput = document.getElementById('password');
    const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordInput.setAttribute('type', type);
});