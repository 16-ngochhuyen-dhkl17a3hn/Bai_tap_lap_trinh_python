import json
class JsonReader:
    def __init__(self,file_path):
        self.file_path= file_path
        self.data= None
    def read_json(self):
        with open(self.file_path,'r') as file:
            self.data = json.load(file)
    def display_data(self):
        if self.data:
            for user in self.data:
                print(f"Name: {user['name']}, Age: {user['age']}, Address: {user['address']}")

path = 'D:/16.Ngọc Huyền - DHKL17A3HN - 23174600139/Lab1/DATA/user.json'
reader = JsonReader(path)
reader.read_json()
reader.display_data()