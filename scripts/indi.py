#from selenium.webdriver.common.by import By
import time
import pandas as pd
import datetime
#import openpyxl as xl
#from openpyxl import load_workbook

''' se realiza la carga del modulo
de tiempo para medir la duracion de ejecucion.'''
start_time = time.time()
st = datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
st,a=st.split(" ")
#wb = load_workbook(filename = r'C:\Users\vriosto\Downloads\Reporte\Asignacion.xlsx')
#sheet_ranges = wb['range names']
'''Se cargan los archivos necesarios para generar el reporte
y se concatenan para disminuir el numero'''
path=r"C:\Users\vriosto\Desktop\indicadores"+st+".csv"
ACSA=pd.read_csv(r'C:\Users\vriosto\Downloads\Reporte\ACSA.csv', sep=',', dtype=object)
ACSA0=pd.read_csv(r'C:\Users\vriosto\Downloads\Reporte\ACSA0.csv', sep=',', dtype=object)
CFA=pd.read_csv(r'C:\Users\vriosto\Downloads\Reporte\CFA.csv', sep=',', dtype=object)
CFA0=pd.read_csv(r'C:\Users\vriosto\Downloads\Reporte\CFA0.csv', sep=',', dtype=object)
CEAB=pd.read_csv(r'C:\Users\vriosto\Downloads\Reporte\CEAB.csv', sep=',', dtype=object)
CEAP=pd.read_csv(r'C:\Users\vriosto\Downloads\Reporte\CEAP.csv', sep=',', dtype=object)
MEAB=pd.read_csv(r'C:\Users\vriosto\Downloads\Reporte\MEAB.csv', sep=',', dtype=object)
MEAC=pd.read_csv(r'C:\Users\vriosto\Downloads\Reporte\MEAC.csv', sep=',', dtype=object)
frames=[MEAB,MEAC]
Modalidad_eval=pd.concat(frames)
frames1=[ACSA,ACSA0]
Acceso_status=pd.concat(frames1)
frames2=[CFA,CFA0]
Calificacion_final=pd.concat(frames2)
frames3=[CEAB,CEAP]
Calificacion_examen=pd.concat(frames3)
#print(Modalidad_eval.head(1))
#print(Calificacion_final.head(1))
#print(Acceso_status.head(1))
#print(Calificacion_examen.head(1))
#print(Modalidad_eval.head(1))
#print(Modalidad_eval['ultimo acceso auvi'])
#print(Modalidad_eval['apellidos'])
#frames=[Acceso_status['nombre'],Acceso_status['apellidos']]
'''se eliminan columnas innecesarias'''
Acceso_status=Acceso_status[['status plataforma','status','matricula','nombre','apellidos','grupo','asignatura','ultimo acceso m','ultimo acceso auvi','clave']]
Modalidad_eval=Modalidad_eval[['status plataforma','status','matricula','modalidad','asignatura']]
Calificacion_examen=Calificacion_examen[['matricula','asignatura','actividad','requerido','calificacion','intento']]
Calificacion_final=Calificacion_final[['status plataforma','status','matricula','asignatura','calificacion','ultimo acceso']]
#nombre=pd.concat.(frames)
#Modalidad_eval['matricula'].add(0)
'''se filtran alumnos por status plataforma y status marcados 
como activos.'''
activo1=Acceso_status['status plataforma'] == "Activo"
activo2=Acceso_status['status'] == "Activo"
#Acceso_status[activo2 & activo1]
Acceso_status=Acceso_status[activo1 & activo2]
activo1=Modalidad_eval['status plataforma'] == "Activo"
activo2=Modalidad_eval['status'] == "Activo"
Modalidad_eval=Modalidad_eval[activo1 & activo2]
activo1=Calificacion_final['status plataforma'] == "Activo"
activo2=Calificacion_final['status'] == "Activo"
Calificacion_final=Calificacion_final[activo1 & activo2]



#print(Modalidad_eval.head(1))
#print("*******************************")
#print(Calificacion_examen.head(1))
#print("*******************************")
#print(Calificacion_final.head(1))
#print("*******************************")
#print(Acceso_status.head(1))
#print("*******************************")

#nombre=Acceso_status[['nombre','apellidos']]
#Modalidad_eval.fillna("Sin modalidad")
#print(Modalidad_eval['modalidad'].value_counts())
nombre=Acceso_status['nombre']+" "+Acceso_status['apellidos']
Acceso_status.insert(3,column="Nombre",value=nombre)
Acceso_status= pd.merge(Acceso_status,Modalidad_eval , how='outer',
               left_on=['matricula','asignatura'], 
               right_on=['matricula','asignatura'])
Calificacion_final= pd.merge(Calificacion_examen,Calificacion_final, how='outer',
               left_on=['matricula','asignatura'], 
               right_on=['matricula','asignatura'])
indicadores= pd.merge(Acceso_status,Calificacion_final, how='outer',
               left_on=['matricula','asignatura'], 
               right_on=['matricula','asignatura'])
indicadores.drop("status plataforma_x",axis=1,inplace=True)
indicadores.drop("status plataforma_y",axis=1,inplace=True)
indicadores.drop("status_x",axis=1,inplace=True)
indicadores.drop("status_y",axis=1,inplace=True)
indicadores.drop("nombre",axis=1,inplace=True)
indicadores.drop("apellidos",axis=1,inplace=True)
activo1=indicadores['status plataforma'] == "Activo"
activo2=indicadores['status'] == "Activo"
#Acceso_status[activo2 & activo1]
indicadores=indicadores[activo1 & activo2]
#print(nombre)
#print(Acceso_status.head())
#print("*******************************")
#print(Calificacion_final.head())
indicadores.drop("status",axis=1,inplace=True)
indicadores.drop("status plataforma",axis=1,inplace=True)
indicadores["actividad"].fillna("Sin Modalidad",inplace=True)
indicadores["requerido"].fillna("Sin Intento",inplace=True)
indicadores["calificacion_x"].fillna(0,inplace=True)
indicadores["intento"].fillna("Sin Intento",inplace=True)
indicadores["calificacion_y"].fillna(0,inplace=True)
indicadores["asignatura"]=indicadores["asignatura"].astype("category")
indicadores["grupo"]=indicadores["grupo"].astype("category")
indicadores["modalidad"]=indicadores["modalidad"].astype("category")




#print(indicadores.head())
#print(indicadores.info())
#print(indicadores["asignatura"].nunique())
#
#print(indicadores["intento"].nunique())
#print(indicadores.info())
#print(path)
indicadores["Nombre"]=indicadores["Nombre"].str.title()
indicadores.insert(7,column="Estado General", value=indicadores["clave"].str.split("_").str.get(2))
indicadores.rename(columns={
                            'matricula': 'Matrícula',
                            'grupo': 'Grupo',
                            'ultimo acceso m': 'Último Acceso Materia',
                            'ultimo acceso auvi': 'Último Acceso Aula Virtual',
                            'requerido': 'Tiempo Requerido',
                            'asignatura': 'Nombre de Materia',
                            'clave': 'Clave',
                            'modalidad': 'Modalidad',
                            'calificacion_x': 'Calificación de Actividad/Examen',
                            'calificacion_y': 'Calificación Final',
                            'ultimo acceso': 'Último Acceso a Plataforma',
                            'intento': 'Número de Intentos',
                            'actividad': 'Actividad',
                            }, inplace=True)
print(indicadores.head())
indicadores.to_csv(path_or_buf=path)

print("--- %s seconds ---" % (time.time() - start_time))
