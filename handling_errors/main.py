import logging

information = {
    "first_name": "gonzalo",
    "last_name": "canaza",
    "age": 30
}

#patron mas comun para una captura de error
try:
    print(information["first_name"])
except (ValueError, KeyError) as error:
    print(error)
    print("the key is not found")
except KeyError as err:
    print(err)
else:
    # solo se ejecuta si el try es verdadero
    print("I am in the else statement")
finally:
    # se ejecuta en cualquier caso, si deseas puedes colocarlo
    print("I am in the finally statement")

print("thank you for using this program")

print("-------------------------")

#esta mal colocarlo de esta manera, es la ultima forma de utilizarlo
#con Exception puedes capturar cualquier error, exception es la raiz de los errores
# con exception no vas a saber cual es el error
try:
    a = 1/0
except Exception as error:
    print(error)

#es importante colocar el tipo de error
#cuando queremos mapear muchos tipo de errores se hace Customs errors

print("-------------------------")

#los prints no los ve los usuarios, solo los que manejan backend, solo es util para probar de manera local
#es una mala practica utilizar los print, no debemos dejar un print en el codigo base de la empresa
#para no utilizar los prints se utiliza el logging
logging.basicConfig(level=logging.DEBUG)
#debug => el usuario hizo una solicitud => informativo
#info => informativo pero algo conciso, muestra mas detalle
#warning => algo que aparecio no hizo que el software se rompiera pero debes corregirlo
#erro => un error que está pasando
#critical => algo que debes corregirlo urgente

try:
    print(information["first_names"])
except (ValueError, KeyError) as error:
    print(error)
    #print("the key is not found")
    logging.warning("the key is not found")


logging.debug("thank you for using this program")
