import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from decision_tree.start_tree import *

class Firebase_settings:
    def __init__(self, key_path, database_name, database_link) -> None:
        self.key_path = key_path
        self.database_name = database_name
        self.database_link = database_link
        return
    
    def init_firebase(self):
        self.authentication = credentials.Certificate(self.key_path)
        firebase_admin.initialize_app(self.authentication, {"databaseURL": self.database_link})
        return
    
    def create_bd(self, data_name):
        ref = db.reference(self.database_name)
        ref.child(data_name)
        return

    def set_data(self, data_name, data):
        ref = db.reference(self.database_name)
        data_ref = ref.child(data_name)
        data_ref.set(data)
        return

    def get_data(self, data_name):
        ref = db.reference(self.database_name)
        data_ref = ref.child(data_name)
        return data_ref.get()



def train_decision_tree():
    data_settings = Firebase_settings("staticfiles/settings/natalnet-c5775-firebase-adminsdk-kf4ue-07da72522e.json", "py/", "https://natalnet-c5775-default-rtdb.firebaseio.com")
    data_settings.init_firebase()
    data = data_settings.get_data("patients")
    tree = train_tree(list(data))
    return tree
