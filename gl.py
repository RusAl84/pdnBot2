


def gl(login='rusal'):
    import json
    fileObject = open("data.json", "r")
    jsonContent = fileObject.read()
    ListOfItem = json.loads(jsonContent)

    result=''
    for item in ListOfItem:
        if str(item['login']).lower()==str(login).lower():
            dataDict=item['data']
            for key in dataDict:
                result+=" " + key
    print(result)
    return result