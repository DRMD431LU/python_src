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

about_me=["1","5","5","charming"]
s=pd.Series(about_me)
# print(s.values)
print(s.index)