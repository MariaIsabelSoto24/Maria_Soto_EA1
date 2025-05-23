import json
import requests
import sys


class Actividad_1():
    def __init__(self):
        self.ruta_static="src/pda/static/"
        sys.stdout.reconfigure(encoding='utf-8')
        

    def leer_api(self, url):
        
        response = requests.get(url)
        return response.json()
    
    def escribir_json(self):
        pass

    #def escribir_txt(self,nombre_archivo="",datos=object):
    def escribir_txt(self,nombre_archivo="",datos=None): # "" '' """ """
        if nombre_archivo=="":
            nombre_archivo="datos.txt"
        if datos is None:
            datos = "No hay datos"
        ruta_txt = "{}/txt/{}".format(self.ruta_static,nombre_archivo)
        with open(ruta_txt, 'w', encoding='utf-8') as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
            f.write(str(datos))
        return True 

    def graficar_rectas(self,a, n,x):
        f = (a*x)**n
        print("funcion_calculo:",f)


ingestion = Actividad_1()
datos_json = ingestion.leer_api("https://www.amiiboapi.com/api/amiibo/?character=zelda&showusage")
print("datos json:",datos_json)
if ingestion.escribir_txt(nombre_archivo="entrega_actividad_1.txt",datos=datos_json):
    print("se creo el archivo txt")
for n in  range(0,10):
    ingestion.graficar_rectas(5, n, 5.4)