/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/


// OBJS
var form = null


/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

   form = new Formulario()
})



/*-----------------------------------------------*\
            OBJETO: Tarjeta filtros
\*-----------------------------------------------*/

function Formulario() {

   this.$imagen = $('#id_imagen')
   this.$imagen_preview = $('#img_preview')

   this.init_Components()
   this.init_Events()
}
Formulario.prototype.init_Components = function () {
    
}
Formulario.prototype.init_Events = function () {

   this.$imagen.on("change",this, this.set_PreviewImagen)
}
Formulario.prototype.set_PreviewImagen = function (e) {

    if (this.files && this.files[0]) {
        
        var reader = new FileReader()

        reader.onload = function (e) {
            form.$imagen_preview.attr('src', e.target.result)
        }

        reader.readAsDataURL(this.files[0])

    }
}
