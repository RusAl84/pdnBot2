import json
ListOfItems=[]
item1={}
item1['login']="rusal"
item1['pass']="12345"
item1['FIO']='Aleksey'
pdnItem={}
pdnItem['passport']='4208836132'
pdnItem['INN']='78438745875487'
pdnItem['SNILS']='143-434-122-80'
item1['data']=pdnItem
ListOfItems.append(item1)
item2={}
item2['login']="misha"
item2['pass']="12345"
item2['FIO']='Masha'
pdnItem={}
pdnItem['passport']='434343554'
pdnItem['INN']='65435454656565'
pdnItem['SNILS']='888-222-132-30'
item2['data']=pdnItem
ListOfItems.append(item2)


jsonString = json.dumps(ListOfItems)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()