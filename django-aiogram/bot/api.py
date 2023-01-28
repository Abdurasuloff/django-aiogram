import requests
import json

BASE_URL = 'http://localhost:8000/api/v1'

def create_user(username, name, user_id):
    url = f"{BASE_URL}/bot-users"
    response = requests.get(url=url).text
    data = json.loads(response)
    user_exist = False
    for i in data:
        if i["user_id"] == str(user_id):
            user_exist = True
            break
    if user_exist == False:    
        requests.post(url=url, data={'username':username, "name":name, "user_id":user_id})
        return "Foydalanuchi yaratildi."
    else:
        return "Foydalnuvchi mavjud."
    



def create_feedback(user_id, body):
    url = f"{BASE_URL}/feedbacks"
    if body and user_id :
        post = requests.post(url=url, data = {
            "user_id":user_id,
            "body":body
        })
        return "Adminga jo'natildi. Fikringiz uchun tashakkur."
    else:
        return "Amal oxiriga yetmadi."    

print(create_feedback("455652665", ""))