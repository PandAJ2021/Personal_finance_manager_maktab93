import pickle

class Pickle_db:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def add_data(self , array):
        with open(self.file_name, 'ab') as myfile:
            pickle.dump(array, myfile)

    def load_data(self):
        objects = []
        with open(self.file_name, "rb") as openfile:
            while True:
                try:
                    objects.append(pickle.load(openfile))
                except EOFError:
                    break
        return objects

