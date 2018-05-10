import time
import pandas as pd
import datetime as dt
import os
import pyautogui as gui, requests as rq
import sys  
import openpyxl
import csv
import time
import navicat as nav


start_time = time.time()
st = dt.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
st,a=st.split(" ")

halloween2016 = dt.datetime(2018, 5, 10, 8, 30, 0)
while dt.datetime.now() < halloween2016:
    print("please waiting")
    time.sleep(360)
# os.path.isfile(r'\\CCO-T34\Users\gpacheco\Documents\REPORTES\COMPARTIDA\REVISION\indicadores\indicadores.csv'))
while not (os.path.isfile(r'\\CCO-T34\Users\gpacheco\Documents\REPORTES\FRONT\indicadores.csv')):
	print("searching")
	# print(os.path.isfile(r'file:\\CCO-T34\Users\gpacheco\Documents\REPORTES\COMPARTIDA\REVISION\indicadores\indicadores.csv'))
	time.sleep(600)



path=r"C:\Users\vriosto\Desktop\new_indicadores"+st+".csv"

EST=pd.read_csv(r'C:\Users\vriosto\Desktop\EST.csv', encoding='iso-8859-1',sep=',', dtype=object)
INDI=pd.read_csv(r'file:\\CCO-T34\Users\gpacheco\Documents\REPORTES\FRONT\indicadores.csv', sep=',', dtype=object,encoding='iso-8859-1')


# wb = openpyxl.load_workbook(r'C:\Users\vriosto\Desktop\indicadores.xlsx')
# sh = wb['Detalle']
# with open(r'C:\Users\vriosto\Desktop\test.csv', 'wb') as f:  # open('test.csv', 'w', newline="") for python 3
#     c = csv.writer(f)
#     for r in sh.rows:
#         c.writerow([cell.value for cell in r])
EST['id_us'].str.strip()
INDI['Clave materia'].str.strip()
print(EST.head())
print(INDI.head())
new_indi= pd.merge(INDI,EST , how='outer',
	            left_on=['Clave materia','Matricula'], 
	            right_on=['id_us','usuario'])
# print(new_indi.tail())
# print(new_indi.info())
new_indi.rename(columns={
                            'Matricula': 'alumno_id',
                            'grupo': 'Grupo de estrategias',
                            'Grupo': 'grupo',
                            'Asignaturas': 'nombre_materia',
                            'Tutor': 'tutor',
                            'Examen semanal Quincenal': 'frecuencia_examen',                            'clave': 'Clave',
                            'Ultimo acceso General': 'acceso_general',
                            'Estado General': 'estado_general',
                            'Acceso por materia': 'acceso_materia',
                            ' Modalidad de evaluación': 'forma_evaluacion',
                            'calificacion':'Calif',
                            'Cal final': 'calificacion',
                            'Status': 'status',
                            'id_us':'id usuario est',
                            'Clave materia':'id_us',
                            
                            'Mensaje':'mensaje',
                            }, inplace=True)
new_indi.to_csv(path_or_buf=path,encoding='utf-8')
nav.navicat_auto()

print("--- %s seconds ---" % (time.time() - start_time))