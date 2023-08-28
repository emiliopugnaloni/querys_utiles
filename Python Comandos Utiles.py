#####################
### LENGUAGE BASE ###
#####################

type(x)#Imprimir tipo de data
range(5) #crea un objeto que va de 0 a 4
range(10,20,3) #crea un rango de 10 a 19 que va de 3 en 3 
list(range(5)) #pasa ese objeto a lista
len(lista) #para acceder al tamaño de la lista
lista.copy() #para copiar lista
dir(variable) #devuelve lista de arubtos del objeto
help(variable) #biranda ayuda del objeto


Listas
    str.split(lista) #para separar en cadenas de teztoa  una lisa
    lista[5]
    lista.append(1) #agrega este elemento al final de la lista
    lista.insert(0,"hola") #inserta en la posicion 0 este elemento
    lista.copy() #para copiar lista

 
Diccionarios
    dicc1 = {'nombre':'Carlos','edad':20,'notas':[8,9,10]}
    dicc1['nombre'] #para acceder a 1 elemento del dicc1 por clave
    dicc1['nombre'][0] #para acceder al 1er valor del 1er elemento


Condicionales & Loops
    if x=1:
        print(x)
    elif x<1:
        print(-1)
    else:
        print(1)
    #--
    while i<3:
        print(i)
    #--
    for x in range(0,3):
        print(x)


Funciones
    def funcion (arg1,ag2):
        return arg1+arg2
        
Regular Expressions:
    [c**2 for c in range(10)]
    [f"title_{c}" for c in ['disney','amazon','hbo',.....]  #para generar un arreglo con ["title_disney", "title_amazon"
 
Clases de objetos
    class Rocket():
        def __init__(self):
            # Cada cohete tiene una posición (x,y).
            self.x = 0
            self.y = 0       
        def move_up(self):
            # Incremento la posicion y del cohete.
            self.y += 1

    cohete = Rocket() # Creo una instancia del objeto Rocket.
    print("Altura del cohete:", cohete.y)  #El cohete tiene atributos (x e y)
    cohete.move_up()  #Muevo el cohete para arriba . El cohete tiene el metodo move_up
    print("Altura del cohete:", cohete.y)


Otros...
    c='algo mas' ;  "escribo texto con {c}"  #para 

Fin .......



Siguientes.....



cols = ['is_practice_test_course', 'rating', 'num_published_lectures', 'num_published_practice_tests', 'bestseller', 'list_price', 'discount_price', 'title', 'headline', 'content_info_short',
 'dias_desde_actualiz_q1', 'dias_desde_actualiz_q2', 'dias_desde_actualiz_q3', 'dias_desde_actualiz_q4',
 'dias_desde_public_q1', 'dias_desde_public_q2', 'dias_desde_public_q3', 'dias_desde_public_q4', 
 'cant_cursos_del_instructor_q1', 'cant_cursos_del_instructor_q2', 'cant_cursos_del_instructor_q3', 'cant_cursos_del_instructor_q4',
 'subt_en_otro_idioma','subt_en_ingles']
df_train = df_train[cols]