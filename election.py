import PySimpleGUI as sg
from FileIO import fileIO

def main():
    while True:
        filename = sg.PopupGetText("Please input filename without extension: ", "DB name? ")
        if (filename != None) and (filename != ""):
            go(filename)
            break
        else:
            continue

def go(filename):
    sg.Popup("Will work on file " + filename + ".xml")
    f = fileIO(filename+".xml")
    f.close()



main()