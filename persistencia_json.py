import json
def store (variable, file) :
    json.dump(json.dumps(variable), open(file, "w"))

def retrieve (file) :
    variable = json.loads(json.load(open(file, "r")))
    return variable