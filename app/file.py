from werkzeug.utils import secure_filename
import os

class File():
    def __init__(self,file):
        self.file = file


    def read_file(self):
        file_name = secure_filename(self.file.filename)
        if file_name == '':
            return False
        else:
            self.file.save(os.path.join("app", "static", file_name))
            with open(f"app/static/{file_name}") as f:
                email_list = f.read().splitlines()
                return email_list

