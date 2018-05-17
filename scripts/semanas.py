import pandas as pd
import datetime as dt
import pyautogui as gui, requests as rq
import time,csv,sys,os


start_time = time.time()
st = dt.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
st,a=st.split(" ")
path=r"C:\Users\vriosto\Desktop\calculo_semanal_"+st+".csv"

semana=pd.read_csv(r'file:\\CCO-T34\Users\gpacheco\Documents\REPORTES\COMPARTIDA\REVISION\indicadores\semana_1.csv', sep=',', dtype=object,encoding='utf-8')
semana_nuevo=pd.read_csv(r'file:\\CCO-T34\Users\gpacheco\Documents\REPORTES\FRONT\indicadores.csv', sep=',', dtype=object,encoding='iso-8859-1')
semana1=semana[['Clasificación','semana-clave']]
semana_nuevo1=semana_nuevo[['Clasificación','semana-clave']]
semana2=semana1[semana1['Clasificación']!="-"]
semana_nuevo2=semana_nuevo1[semana_nuevo1['Clasificación']!="-"]
# conteo=clasificaciones_series['Clasificación'].value_counts()
# print(conteo)
calculo_semanal= pd.merge(semana2,semana_nuevo2, how='outer',
	            left_on=['semana-clave','Clasificación'], 
	            right_on=['semana-clave','Clasificación'])
# calculo_semanal=calculo_semanal[calculo_semanal['Clasificación']!=""]
if not os.path.exists(path):
  calculo_semanal.to_csv(path_or_buf=path)
