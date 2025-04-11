import sender_stand_request
import data

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def get_new_user_token():
    user_body = data.user_body
    resp_user = sender_stand_request.post_new_user(user_body)
    return resp_user.json()["authToken"]

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400
    assert response.json()["name"] == kit_body["name"]

def test_numero_permitido_de_caracteres_1():
    positive_assert(data.test_1)

def test_numero_permitido_de_caracteres_511():
    positive_assert(data.test_2)

def test_numero_permitido_de_caracteres_0():
    negative_assert_400(data.test_3)

def test_numero_permitido_de_caracteres_512():
    negative_assert_400(data.test_4)

def test_numero_caracteres_especiales_permitidos():
    positive_assert(data.test_5)

def test_espacios_permitidos():
    positive_assert(data.test_6)

def test_numeros_permitidos():
    positive_assert(data.test_7)

def test_parametro_vacio():
    negative_assert_400(data.test_8)

def test_parametro_diferente():
    negative_assert_400(data.test_9)