from .. models import Documento

def guardar_documento_logic(tipo, ruta, identificacion):
    documento = Documento(identificacion=identificacion, tipo=tipo, ruta=ruta)
    documento.save()
    return documento