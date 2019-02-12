class fileIO:
    
    def __init__(self, filename):
        self.lines = list()
        self.no = 1
        self.filename = filename
        self.load("", self.lines)

    def load(self, filename, lines):       
        
        try:
            self.file = open(self.filename, "r")
            print("\n\n\n\n<<<<File contents begin here!>>>>\n\n\n\n")
            for ln in self.file:
                print(ln)
                lines.append(ln)
                self.no += 1
            print("\n\n\n\n<<<< contents of " + self.filename + " end here! >>>>\n\n\n\nRead " + str(self.no + 1) + " lines.")
            self.file.close()
            self.file.open(self.filename, "w")
        except FileNotFoundError:
            print("File not found. Creating now")
            self.file = open(self.filename, "w")

    def refresh(self, new):
        self.lines = list()
        self.filename = new
        self.file.close()

    def rmLineByIndex(self, index):
        self.lines.pop(index)

    def rmLine(self, toRm):
        self.lines.remove(toRm)

    def getByIndex(self, index):
        return self.lines[index]

    def searchForLineNumber(self, searchStr):
        b = 0
        while (b < self.no):
            if self.lines[b].strip() == searchStr.strip():
                break
        if b < self.no:
            return b + 1
        else:
            return -1

    def addXMLTag(self, name, closing, indentLev):
        if closing:
            self.lines.append("\n"+self.indent(indentLev) + "</" + name + ">")
        else:
            self.lines.append("\n"+self.indent(indentLev) + "<" + name + ">")

    
    def addLine(self, str):
        self.lines.append("\n" + str)
    
    def addLineAtIndex(self, str, index):
        self.lines.insert(index, str)

    def getNo(self):
        return self.no

    def toStr(self, ls):
        str = ""
        for l in ls:
            str += l + "\n"
        return str

    def indent(self, num):
        str = ""
        i = 0
        while (i<num):
            str += " "
            i += 1
        return str

    def contentsAsStr(self):
        return self.toStr(self.lines)

    def close(self):
        self.file.write(self.toStr(self.lines))
        self.file.close()
