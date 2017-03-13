import json

def openJSON(inFile):
    with open(inFile) as json_data:
        data = json.load(json_data)
    return data

def saveJSON(data, ouFile):
    with open(ouFile, 'w') as outfile:
        json.dump(data, outfile)

def replaceDataset(data, oldTableName, newTableName):
    data = json.loads(json.dumps(data).replace(oldTableName, newTableName))
        return data

def openFileReplaceDatasetSave(inFile, ouFile, oldTableName, newTableName):
    data = replaceDataset(openJSON(inFile), oldTableName, newTableName)
    saveJSON(data, ouFile)
    return data
