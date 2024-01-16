import request


#Абдрахманов Азиз, 12-ая когорта "Финальный проект, инженер по тестированию плюс"
# Тест проверки создания заказа
def test_order_creation():
    creation_response = request.post_new_order()
    track_id = creation_response.json().get('track', None)