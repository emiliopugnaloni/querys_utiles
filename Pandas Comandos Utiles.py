
## AYUDAS ##
dir(df1) #para mostrar los metodos/atributos
Shift+TAB (2 veces) en Jupyter para INFO
TAB luego de poner '.' (o sin nada segun) en JUpyter para ver los metodos, elemntos, funciones que se pueden hacer en cada objeto (tambien para autocompletar?)

Cargar/guardar tablas
    pd.read_csv('file.csv', index_col = 'col1' #para poner esta col como index)  #cargar csv como Df.
    pd.read_csv('file.csv', parse_date = ["fecha"]) #para que ponga en formato fecha cuando se carga
    dataframe.to_csv("archivo.csv", index=False, columns =['Gender', 'Ethnicity',...]) #para guardar especif columnas y sin index
    dataframe.to_csv("archivo.csv", index=False, encoding='utf-8')  #se puede usar este encoding para aumentar la lista de caracteres aptos
    
Info 
    df1.head() #para 1ros datos del df/serie
    df1.tail() #para ultimos datos del df/serie
    df1.dtypes #para saber el tipo de datos de la columns
    df1.info() #nos da info del dataframe /serie
    type(s) #nos da el tipo de datos de la serie

Estructura de DF/Serie
    df1.values #para obtener los valores como arreglos numpy multidim del df
    s.values #los mismo pero para series (ahora es 1 arreglo de 1 dim)
    df1.index #para tener los indices del df /serie
    df1.columns #para tener las columnas
    df.set_index(keys=['col1'], inplace=True) #para establecer la col 1 como indice
    serie.to_frame() #para pasar a data frame desde serie
    serie.tolist() #para pasar a lista

Index
    df.set_index( keys = ["col1","col2"], inplace=True) #para poner columnas como indices rows
    df.sort_index( inpalce=True) #para ordenar el index
    df.sort_index( ascending = [True, False], inplace =True) #para ordenarlo si hay multiindex
    df.index.get_level_values("col1") #nos permite obtener los valores de 1 index cuando tenemos multiindex (por ej si pusimos la col1 y col2 como index)
    df.index.set_names (names = ['Col1','Col2'], inplace=True) #para cambiar el nombre de los index
    df.index.set_names (names= {'col1':'Col1', 'col2':'Col2'}, inplace=True) #otra forma de hacerlo
    df.loc[ 'value_index1' ] #para buscar valor por index
    df.loc [ ('value_index1', 'value_index2'), 'col 1' ) #para busca cuando hay multindex
    

Valores Faltantes/Nulos
    s.hasnans #devuelve true/false segun si la serie tiene nans
    df1.dropna() #elimina la fila si aparece algun nulo (no modifica el df)
    df1.dropna(inplace=True) #el inplace va si queremos que el df se guarde (como que lo sobrescribe)
    df1.dropna(how='all') #elimina la fila si es nula en todas las columnas
    df1.dropna( subset= ['col1','col2'] ) #la elimina si es nulo en estas columnas
    df1.isna().sum() #para saber cuantos nulos en cada columna
    df['col1'].fillna(0, inplace=True) #llena con 0s los nulos en la col1 y lo guarda
    df1['col1'].isnull() #devuelve True cuando es nulo (es 1 filtro)
    df1['col1'].notnull() #devuelve True cuando no es nulo (es 1 filtro)
    
Valores Duplicados
    df["First Name"].duplicated() #marca como True los duplicados (el 1ro lo marca como False. Ver argumentos)
    ~df["First Name"].duplicated() #marca como False los duplicados. Esto es mas facil para filtrar despues
    df.drop_duplicates() #devuelve los no duplicados. Considera duplicado cuando todo es duplicado
    df.drop_duplicates(subset=["Gender", "First Name"], keep="last", inplace=False) #aca devuelve no duplicados, considerando estas col. Se queda con el ult.
    
    df['Col1'].unique() #devuelve valores unicos
    df['Team'].nunique() #devuelve la cantidad dist. No cuenta el NaN, usar dropna=False
    

Operaciones Matematicas
    df.sum() #suma los valores por columnas
    df.sum(axis=1) #suma los valores por filas

Seleccionar Columnas
    df1['col1']    #para seleccionar 1 columna
    df1.col1       #lo mismo
    df1[ ['col1','col2']  ]  #para selecc +1col. Se pasa 1 lista con las columnas de interes 
    
Seleccionar Fila y Columnas (con Loc y Iloc)
    df.loc['indice de fila 1'] #seleccionamos la fila por el index de las filas. LOC : para buscar por "label". ILOC: para buscar por "index label" (numero)
    df.loc['indice 1' : 'indice 10']  #seleccioamos un rango de filas. Es inclusivo
    df.iloc[0]     #seleccionamos la fila en la pos 0
    df.iloc[0 : 10] #es exclusivo
    
    df.loc['indice fila 1', 'col 1' ] #seleccionamos filas y columnas
    df.iloc[0, 1] #seleccionamos el 1er valor de la 2da columna

Agregar Columna
    df1['nueva_col'] = ....
    df1.insert(loc=3 , column = 'nueva_col' , vaulue = ...) #para insertar columna en 1 posicion determinada (aca la 3). Desplaza las otras col

Filtrar Filas
    filtro = df["Gender"] == "Male" #es conveniente crear variables con filtro
    filtro2 = df["Team"] != "Marketing"
    filtro3 = df["Date"]< "1990-01-01"
    df[filtro & (filtro2 | filtro3)]
    
    filtro = df["Team"].isin(["t1","t2","t3"]) #devuelve true/false dependiendo si en la fila esta alguno de estos 3
    filtro = ddf["Salary"].between(60000,70000) #devuelve true/false. Es inclusivo. Tambien para fechas sirve
    

Contar Filas Distintas
    df['col1'].value_counts()  #cuenta filas distintas en col1
    df['col1'].value_counts(normalize=True)  #con el normalize=True da %

Tipos de Datos
    df1['col1'].astype('int') #cambia el tipo de datos a int (hay que sobrescibir, no hay inplace). 
        #Despues bool (para boleanoos True/False), category (para categorias ej HOmbre, Mujer)
    pd.to_datetime(df["fecha"])  #para pasar a formato fecha-hora
             

Ordenar Dataframe
    df1.sort_values( by=['col1','col2'], ascending=True) #para ordenar por col1 y col2 en orden asc
    df1.sort_values( by=['col1','col2'], ascending=[True,False]) #para ordenar por col1 en orde Asc y col2 en orden Desc
    df1.sort_values(by='col1', inplace=True)  #hay que poner inplace para que quede guardado. Si no sobrescibirlo manualmente
    df.reset_index( drop=True , inplace=True) #para reiniciar el indice luego de ordenar (los indices no habian cambiado)
    df.sort_index() #para ordenar por el indice
    df['col1'].rank(ascending=False) #para asociar cada valor de col1 con la posicion en un ranking ordenado
    

Cambiar valores de Df
    df.loc[ df.nombre=="Emilio", "Apellido"] = 'Pugnaloni' #con esto cambiamos el df original
    df.Apellido[df.nombre=="Emilio"] = 'Pugnaloni' #con este estamos haciendo una copia del df original. Hay que tener cuidado. Usar copy() por las dudas cuando se quiera copiar
    df.col1.str.replace('$',"") #para remplazar en una columna un caracter, valor
    
    
Renombrar Columnas
    df.rename( columns = {'NombreViejo':'NombreNuevo', 'NombreViejo2':'NombreNuevo2'} ) #se necesita un diccionario en columnas
    df.columns = ['col1', 'col2', 'col3' ,..]
    
Eliminar Filas/Columnas
    df.drop(['indice fila 1', 'indice fila 2' ], inplace=True) #eliminamos fila por el indice de la fila (el label)
    df.drop ( ['col1', 'col2' ] , axis='columns', inplace=True) #eliminamos la columna
    
    
Crear Sample de el DF
    df.sample(n=5) #nos quedamos con 5 filas aleatorias
    df.sample(frac=0.5) #nos quedamos con el 50% del df
    
Valor mas altos/bajos
    df.nsmallest(n=3, columns='col5') #devuelve los 3 valores mas bajos por la columna 5
    df.nlargest(n=3, columns='col5') #devuelve los 3 valores mas alto por la columna 5
  
  
Funciones por fila (apply, ..)
    def funcion(row):
        ....
        return x
       
    df.apply(funcion, axis='columns') #aplica funcion a cada una de las filas (la funcion tiene que tener alguna fila de arg). El 'columns' es medio raro pero es asi
   
Formato Long / Wide
   df.melt( id_vars = 'Producto', value_name = 'cantidad', var_name = 'Mes' ) #pasa de wide a long. Todas las columnas que no sean 'Producto' ni 'Cantidad' van a pasar a una que se llama 'Mes' como valores 
   df.pivot ( index = 'Año', columns = 'Vendedor', value = 'cantidad') #pasa de long a wide. Pone a los 'Vendedor' en columnas
    
Agrupar Filas
 df.pivot_table ( values= 'cantidad', index = ['Genero', 'Nacionalidad'], columns='marca', aggfunc=['mean','sum'] #funciona como un group by. Pero devuelve una tabla. Aca se agrupa 'values' por estos index (en filas) y columnas
 agrupado_1 = df.groupby('Pais') #esta variable es del tipo DataFrameGroupBy Object. No es 1 df. Tien de longitud la # de Paises en el df original
 agrupado_1.groups #es un diccionario con las filas del df original que le corresponden a cada Pais
 agrupado_1.get_group('Argentina') #nos devuelve todas las filas que corresponden a Argentina como pais. Si se tiene que hacer para muchos paises, es mas rapido que, porque ya esta todo agrupado por paises No hay que volver a agrupar
 agrupado_2 = df.groupby(['Pais', 'Provincia']) #agrupas de a 2 col
 agrupado_2.mean() , sum() , .. #pesto si nos da un resultado. Las columnas se suman segun la agrupacion
 agrupado_2.agg( {'Habitantes': ['sum','mean'], 'PBI':'mean' } #para agrupar segun determinadas columnas y con determinadas funciones
 agrupado_2.agg( ['sum','mean','size']) #si se quiere agrupar todas por todo esto


Joins y concatenar tablas
 pd.concat( objs = [tabla1,tabla2], ignore_index=True, keys=['Tabla1', 'Tabla2']) #junta estas dos tabla (una abajo de otra). El Keys hace que se agrege una index, sirve para identif de donde vino cada fila
 pd.concat( objs = [tabla1,tabla2], ignore_index=True, axis='columns') #junta estas dos tabla (una al lado de la otra)
 tabla1.merge(tabla2, how= 'inner', 'full' o 'left' , on ='ID' , suffixes=('_tabla1', '_tabla2') # para hacer joins. El On es por la columna que se hace (tiene que ser igual en ambas tablas) y el suffixes hace que a las columnas de cada tabla se le agregue un sufijo
 tabla1.merge(tabla2, how= 'inner', on =['ID','Food_ID']) # se puede hacer joins por +1 columna
 tabla1.merge(tabla2, how'left', left_on='ID', right_on = 'id') # para hacer joins cuando los ID se llaman distintos entre tablas
 tabla1.merge(tabla2, how'left', left_on='ID', right_index = True) # el right_index sirve cuando el ID esta en el index en la tabla de la dercha
 
 
Fechas y Horas
    import datetime as dt #es el modulo de tiempo/hora en python. No es una libreria aarte, es una parte de la libreria base de python
    dia1 = dt.date(2016, 1, 20) #para crear una fecha. Es un objteto 'datetime'
    dia1.year / dia1.month / dia1.day #para obtener algun componente de la fecha
    diahora1 = dt.date(2016, 1, 20, 10, 3, 40) #tambien se puede hasta nivel de segundo. Es un objeto 'datetime' tambien. Con .seconds / .minutes / .hours se puede seleccionar el elemento
    str(diahora1) #para que se muestre mejor al imprimirlo
    
    dia2 = pd.Timestamp("2010-03-08 08:35:15") #este es un objeto "timestamp", es la version datetime de pandas. Es mejor porque acepta una varierdad de inputs, lo anterior se puede haber puesto como: "2015-03-31", "2015/03/31", "2013, 11, 04", "2021-03-08 08:35:15 PM" y lo reconoce a todos y +
    dia2 = pd.Timestamp(dt.datetime(2000,2,3,21,35,22)) #se puede poner un datetime de index tmbn
    dia2.month_name() #para obtener el month_name. Hay otros atributos/funciones como .month, is_month_end, ... (con apretar el TAB luego del . apareceria la lista de cosas...)
    
    dtIndex= pd.DatetimeIndex( ["2016-01-02", "2016-04-12", "2009-09-07"] ) #es un datetime index, un indice de fechas. Se toma un strign en este caso, y lo convierte a formato fecha (cada elemento en un 1 timestamp xq es pandas)
    dtIndex2 = pd.to_datetime(['2001-09-04', '2020/09/30', 'July 4th, 1998']) #sirve para convertir una lista/serie de stings (o otra cosa?) en un objeto DatetimeIndex. Se puede poner como argunmento, errors='corce' para que si hay algo que no es fecha que le ponga NaT (not a time)
    dtIndex3 = pd.to_datetime([1349720105, 1349806505], unit='s')  #para pasar unixtimesatmp (cant de segundos desde 1 enero 1970) a formato hora
    
    rangoFechas1 = pd.date_range(start="2016-01-01", end='2016-01-10', freq='d') #para crear rango de fechas como objeto DatetimeIndex. La freq dice en que intervalo. d=dia, 24d = 24 dias, b=dias laborables, w = 1 dia por semana (x defaul el ultimo, si no w-fri para especificar friday u otro), 6h = para rangos de 6 horas, ...
    rangoFechas2 = pd.date_range(start="2016-01-01", periods=3, freq='d') #otra forma de crear rangos es con el periodo
    
    serieFechas = pd.Series(pd.date_range(start = "2000-01-01", end="2010-12-31", freq="24D"))
    serieFechas.dt.day #con el .dt (es un accessor estilo .str en strings) se puede aceder luego a los elementos del dia.
    serieFechas.dt.day_name() #hay un monton, este es para que diga el nombre del dia de c/u de los elementos de la serie
    
    serieFechas.loc[pd.Timestamp('2020-12-31')] #para seleccionar una fecha por el index. Es recomendable ponerlo en formato timestamp
    serieFechas.loc[[pd.Timestamp('2020-12-31'), pd.Timestamp('2020-12-31')]]
    serieFechas.loc[pd.to_datetime(['2020-12-31', '2020-12-31'])] #esto tambien funciona como el de arriba
    
    dia2 + pd.DateOffset(days=5) #para agregarle dias (o otras cosas) a una fecha
    serieFechas.index + pd.DateOffset(years=1, months=3, weeks=5, days=-3, hours=6, minutes=-20, seconds=30) #lo mismo para  serie que tienen fechas (en este caso las fechas estan en elindice)
    
    dia2 + pd.Timedelta(days=1) #ptra alternativa para agregar dias/fechas. EL time delta es un tipo de dato:  pd.Timestamp("2020-03-31 04:35:16PM")- pd.Timestamp("2020-03-20 02:15:23PM") # esto tiene fomrato TimeDelta
    dia2 + pd.Timedelta( weeks=8, days=3, hours=12, minutes=45, seconds=20)
    serieFechas.index + pd.TimeDelta( ....) #tambien sirve para timedelta
    
    
# OTROS PARA LIMPIEZA DATOS
df[["col1","col2","col3",..]]= df["instructors"].str.split(",", expand=True) #para separar los datos que vienen en comas en dist df
df["col1"].str.lower().str.contains("linux") #para ver si una columna tiene en los valores determinados datos
pd.qcut(df["num_published_lectures"], q=4, labels=['cat1', 'cat2', 'cat3', 'cat4']) #con esto pasmos 1 variable numerica en categorica, haciendo 4 categorias, segun los 4 cortes en este caso. A los levels se los puedo sacar si quiero q me tire 1,2,3,4
pd.cut(df["num_published_lectures"], bins=[0, 50, 100, 500, 1000], labels=['cat1', 'cat2', 'cat3', 'cat4']) #tambien, para pasar numericas en categoricas. Aca podemos especificar los bins
pd.get_dummies(df, columns=['cat1', 'cat2']) # , dummy_na=True #para tener dummies
df["captions"].map({"es_ES": 1, "es_MX": 2}) #para pasar categoricas en numericas. si no está pone NaN // cambia tipo de dato
(df["col1"] - df["col1"].min()) / (df["col1"].max() - df["col"].min())  #normalizacion (
(df["col1"] - df["col1"].mean()) / df["col1"].std()  #estandarizacion (le resto la media y lo divido por el desvio)