class UserDelegate:
    def english_data(self):
        return ""
    def user_id(self):
        return ""

class dict:
    def __init__(self):
        self.dict1 = {"a":1,"b":2}
    def translate(self,user:UserDelegate):
        translate_china = self.dict1[user.english_data()]
        return translate_china
