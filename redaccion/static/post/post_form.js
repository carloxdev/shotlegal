/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

// OBJS
var formulario = null

/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {
    formulario = new TargetaFormulario() 
})



/*-----------------------------------------------*\
            OBJETO: TargetaFormulario
\*-----------------------------------------------*/

function TargetaFormulario() { 

    this.$contenido = $('#id_contenido')

    this.init_Components()
}
TargetaFormulario.prototype.init_Components = function () {


    this.$contenido.wysihtml5({
        toolbar: {
            "font-styles": true,
            "emphasis": true,
            "lists": true,
            "html": false,
            "link": false,
            "image": false,
            "color": false,
            "blockquote": false,
        }
    })
    
}
