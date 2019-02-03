import json 
from character import *

class jsonReader:
    def __init__(self):
        self._fileName = ''
        self._filePath = ''
        self._content = ''
        self._json = ''

    def setFileNameAndPath(self, fileName, path):
        self._fileName = fileName
        self._filePath = path

    def readFileContent(self):
        with  open(self._filePath + self._fileName, "r") as f:
            _content = f.read()
        print(_content)
        return _content

    def readFileJson(self):
        print(self._filePath + self._fileName)
        with  open(self._filePath + self._fileName, "r") as f:
            self._json = json.load(f)                  
        return self._json

    def getAllCharacters(self):
        self.readFileJson()
        charactersList=list()              
        for elem in self._json:
            ch = Character()  
            print(elem['first_name'])    
            ch.setCharacter(elem['first_name'],elem['last_name'], elem['pic'], elem['position'], elem['bio'])        
            charactersList.append(ch)
        return charactersList    