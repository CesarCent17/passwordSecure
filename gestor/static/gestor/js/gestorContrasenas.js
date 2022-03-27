const btnsEliminacion = document.querySelectorAll(".BtnEliminar");

(function (){
    btnsEliminacion.forEach(btn =>{
        btn.addEventListener('click', function (e){
            let confirmacion = confirm("Confirma la eliminacion de la contrasena?");
            if (!confirmacion){
                e.preventDefault();
            }
        });
    });
});