
def gd(login='rusal', getpdn='passport'):
    import json
    fileObject = open("data.json", "r")
    jsonContent = fileObject.read()
    ListOfItem = json.loads(jsonContent)
    result=''
    for item in ListOfItem:
        if str(item['login']).lower()==str(login).lower():
            result=item['data'][getpdn]
    print(result)
    return str(result)