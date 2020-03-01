class File():
    def __init__(self,file):
        self.file = file

    def readFile(self):
       with open(self.file, "rb") as file:
           data = file.read()
           for line in data:
               print(line)

# TODO how to read a file on server
# GIT
#