from FileIO import fileIO

def main():
    while True:
        filename = input("Please input filename: ")
        if (filename != None) and (filename != ""):
            break
        else:
            continue
            
    file = fileIO(filename)
    if file.contentsAsStr() != repeat(file.getNo(), "\n"):
        file.addXMLTag("html", False, 0)
        file.addXMLTag("head", False, 4)
        file.addLine(file.indent(8)+"<title> Test </title>")
        file.addXMLTag("head", True, 4)
        
        file.addXMLTag("body", False, 4)
        file.addLine("Easy way to demonstrate the fileIO.py class by creating an HTML document. This class can also be used to store and retrieve data in an XML-like language (no compatibility with actual XML guaranteed), which will be the primary use-case.")
        file.addLine("\nTest line that will be removed the second time you run the program")
        file.addXMLTag("body", True, 4)
        
        file.addXMLTag("html", True, 0)
    else:
        a = file.searchForLineNumber("<body>")
        print("Line number of <body> is " + a)
        file.rmLineByIndex(a + 1)
        print("Removed test line")
        a = file.searchForLineNumber("<body>")
        file.addLineAtIndex("Replacement test line: ", a + 2)

    file.close()

def repeat(a, b):
    i = 0
    str = ""
    while (i < a):
        str += b
        i += 1
    return str
main()
