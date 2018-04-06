#from selenium.webdriver.common.by import By
import time
import pandas as pd
import openpyxl as xl
from openpyxl import load_workbook
start_time = time.time()
wb = load_workbook(filename = r'C:\Users\vriosto\Downloads\Reporte\Asignacion.xlsx')
#sheet_ranges = wb['range names']

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
Acceso_status=Acceso_status[['status plataforma','status','matricula','nombre','apellidos','grupo','asignatura','ultimo acceso m','ultimo acceso auvi','clave']]
Modalidad_eval=Modalidad_eval[['matricula','modalidad','asignatura']]
Calificacion_examen=Calificacion_examen[['matricula','asignatura','actividad','requerido','calificacion','intento']]
Calificacion_final=Calificacion_final[['matricula','asignatura','calificacion','ultimo acceso']]
#nombre=pd.concat.(frames)
#Modalidad_eval['matricula'].add(0)
print(Modalidad_eval.head(1))
print("*******************************")

print(Calificacion_examen.head(1))
print("*******************************")
print(Calificacion_final.head(1))
print("*******************************")
print(Acceso_status.head(1))
#nombre=Acceso_status[['nombre','apellidos']]
#Modalidad_eval.fillna("Sin modalidad")
#print(Modalidad_eval['modalidad'].value_counts())
nombre=Acceso_status['nombre']+" "+Acceso_status['apellidos']
#Acceso_status.insert(3,column="Nombre",value=nombre)

print(nombre)

print("--- %s seconds ---" % (time.time() - start_time))