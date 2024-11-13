'''
@author: reinaqu
'''

def crear_dicc_titulos_anyos(bsos:list[tuple[str,int]])->dict[str, int]:
    '''
    Recibe:
    :param bsos: una lista de tuplas (titulo, año)
    :type: [(str, int)]
    Devuelve:
    :return: Un diccionario que tiene como clave los títulos y como valores los años
    :rtype: {str:int}
    '''
    res = {} #res = dict()
    for titulo, año in bsos:
        res[titulo] = año 
        # haciendo esto, en el caso de que dos titulo tuvieran dos fechas diferentes, solo estoy guardando la última en recorrerse
    return res

def crear_dicc_titulos_anyos2(bsos:list[tuple[str,int]])->dict[str, int]:
    '''
    Recibe:
    :param bsos: una lista de tuplas (titulo, año)
    :type: [(str, int)]
    Devuelve:
    :return: Un diccionario que tiene como clave los títulos y como valores los años
    :rtype: {str:int}
    '''
    #definir un diccionario por comprensión
    return {titulo:año for titulo, año in bsos}

def crear_dicc_anyos_conteo_titulos (bsos:list[tuple[str,int]])->dict[int, int]:
    '''
    Recibe:
    :param bsos: una lista de tuplas (titulo, año)
    :type: [(str, int)]
    Devuelve:
    :return: Un diccionario que tiene como clave los años y como valores el número de títulos
          de ese año
    :rtype: {int:int}
    '''
    res = {} #res = dict()
    #res = defaultdict(int)
    for titulo, año in bsos:
        if año not in res:        
            res[año] = 0
            #si pongo el defaultdict, no hace falta esto:if año not in res: res[año] = 0
        res[año] +=1
    return res
#es un algortimo tan habitual que python tiene un diccionario "de conteo", qu es lo simo pero esconde el bucle


from collections import Counter

def crear_dicc_anyos_conteo_titulos_COUNTER(bsos:list[tuple[str,int]])->dict[int, int]:
    return Counter(año for titulo, año in bsos)
#las claves son los años, y las contraseñas son el numero de veces que aparare el valor
   
    

def crear_dicc_anyos_lista_titulos (bsos:list[tuple[str,int]])->dict[int, list[str]]:
    '''
    Recibe:
    :param bsos: una lista de tuplas (titulo, año)
    :type: [(str, int)]
    Devuelve:
    :return: Un diccionario que tiene como clave los años y como valores una lista con los títulos
          de ese año
    :rtype:{int:[str]}
    '''
    res = {}
    for titulo, año in bsos:
        if año not in res: 
            res[año] = [] #list()
        res[año].append(titulo)
        

from collections import defaultdict

def crear_dicc_anyos_lista_titulos (bsos:list[tuple[str,int]])->dict[int, list[str]]:
    
    res = defaultdict(list) #¿De qué tipo son los valores? 
    #si alguien intenta accedeer a una clave que no existe, devuelve
    #lo el valor que le has dado por defecto, y ahora, el diccionario 
    # ya tiene una clave y su valor
    
    #tambien podemos aplicar esto a la primera funcion de conteo
    for titulo, año in bsos:
        res[año].append(titulo)

def obtener_clave_mayor(dicc_bso:dict[str,int])->str:
    '''
    Recibe:
    :param dicc_bso: Un diccionario que tiene como clave los títulos y como valores los años
    :type: {str:int}
    Devuelve:
    :return: La clave con valor mayor, segun el orden natural
    :rtype: str
    '''
    pass

def obtener_valor_mayor(dicc_bso:dict[str,int])->int:
    '''
    Recibe:
    :param dicc_bso: Un diccionario que tiene como clave los títulos y como valores los años
    :type: {str:int}
    Devuelve:
    :return: El valor mayor, que en este caso es el año más reciente.
    :rtype: int
    '''
    pass

def obtener_nombre_mas_largo(dicc_bso:dict[str,int])->str:
    '''
    Recibe:
    :param dicc_bso: Un diccionario que tiene como clave los títulos y como valores los años
    :type: {str:int}
    Devuelve:
    :return: El nombre de la canción con más caracteres
    :rtype: str
    '''
    pass