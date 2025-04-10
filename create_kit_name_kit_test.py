import sender_stand_request
import data


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(kit_body):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_user(kit_body)
    assert kit_response.status_code == 201
