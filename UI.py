import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtWidgets import QApplication, QLabel
from PySide2.QtGui import QPixmap, QPicture, QIcon
from character import *
from jsonReader import *

def listItemSelected(listElement):
    #print(listElement.data())    
    for character in allCharactersList:
        fullName = character.firstName + ' ' + character.lastName
        if fullName == listElement.data():
            labelCharacterFirstLastName.setText(fullName)
            labelFamilyPosition.setText(character.position)
            labelImage.setPixmap(QPixmap("./data" + character.pic[1:]))
            labelBio.setText(character.bio)
            labelBio.show()
    
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
windowDetails= QtWidgets.QWidget()
layout = QtWidgets.QHBoxLayout(window)
layoutDetails = QtWidgets.QVBoxLayout(windowDetails)
myListWidget = QtWidgets.QListWidget()
myListWidget.clicked.connect(listItemSelected)
myListWidget.setAlternatingRowColors(True)
myListWidget.setDragDropMode( QtWidgets.QAbstractItemView.InternalMove )

# generate all characters from json
charactersFromJson = jsonReader()
fileName = 'characters.json'
filePath = './data/'
charactersFromJson.setFileNameAndPath('characters.json', './data/')
allCharactersList = charactersFromJson.getAllCharacters()

# add list items
for elem in allCharactersList:
    #print(elem._firstName)
    item = QtWidgets.QListWidgetItem('counter', myListWidget)    
    item.setText(elem._firstName + ' ' + elem._lastName)    
    item.setIcon(QIcon("./data" + elem.pic[1:]))
   

layout.addWidget(myListWidget)
layout.addWidget(windowDetails)

labelCharacterFirstLastName = QLabel('Please select character.')
labelFamilyPosition = QLabel()
labelImage = QLabel()
labelBio = QtWidgets.QTextEdit()
labelBio.hide()
layoutDetails.addWidget(labelCharacterFirstLastName)
layoutDetails.addWidget(labelImage)
layoutDetails.addWidget(labelFamilyPosition)
layoutDetails.addWidget(labelBio)
window.show()
sys.exit(app.exec_())