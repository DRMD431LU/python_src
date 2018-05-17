import pandas as pd
# "a series of strings"
# ice_cream=["chocolate","vanilla","strawberry","rum raisin"]
# print(pd.Series(ice_cream))
# "a series of inegers"
# lottery=[4,8,15,16,23,42]
# print(pd.Series(lottery))
# "a series of booleans"
# registrations=[True,False,True,False]
# print(pd.Series(registrations))
# '''a series from a dictionary, the keys
# works as indexes :O'''
# webster={"Aardvark": "An animal", 
# "Banana":"A fruit",
# "Cyan":"A color"}

# print(pd.Series(webster))

# about_me=["1","5","5","charming"]
# s=pd.Series(about_me)
# print(s.values)
# print(s.index)
# print(s.dtype)
# prices=[2.99,4.45,1.36]
# s=pd.Series(prices)
# print(s)
# print(s.sum())
# print(s.product())
# print(s.mean())
# fruits=["Apple","Orange","Plum","Grape","Blueberry","Watermelon"]
# weekdays=["Monday","Tuesday","Wednesday","Thursday","Friday","Monday"]
# print(pd.Series(fruits,weekdays))
# print(pd.Series(data=fruits,index=weekdays))
# print(pd.Series(fruits,index=weekdays))
pokemon=pd.read_csv("pokemon.csv", usecols=["Pokemon"],squeeze=True)
# print(s)
google=pd.read_csv("google_stock_price.csv",squeeze=True)
# print(google)
# pokemon.head()
# print(len(pokemon))
# google.sort_values(ascending=False, inplace=True)
# print(google)
# if ("05">"5"):
# 	print("05 es mayor")
# elif("5">"05"):
# 	print("5 es mayor")
# else:
# 	print("son iguales")
print(pokemon[500])