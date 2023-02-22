import json

defaultValues = {
    "width":{
        "default":800,
        "type":int
    },
    "height":{
        "default":600,
        "type":int
    },
    "title":{
        "default":"TKCraft",
        "type":str
    },
}

configFile = "config.json"

def config():
    load = open(configFile,"r")
    load = json.load(load)
    for _,property in enumerate(defaultValues):
        try:
            if(type(load[property]) != defaultValues[property]["type"]):
                raise Exception("Type Mismatch")
        except:
            load[property] = defaultValues[property]["default"]
    return load