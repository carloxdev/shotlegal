
class Validador(object):

    @staticmethod
    def get_UrlImagen(_imagen):
        imagen = ""
        if _imagen:
            imagen = _imagen.url

        return imagen
