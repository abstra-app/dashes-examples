import requests

postal_code = ""
address = ""
state = ""
weight = 0
urgency = 0
discount = False

south_states = ["PR", "SC", "RS", "MG", "ES", "RJ", "SP"]
center_states = ["MS", "MT", "GO", "DF", "MA", "PI", "CE", "RN", "PB", "PE", "AL", "SE", "BA"]
north_states = ["RO", "AC", "AM", "RR", "PA", "AP", "TO"]

def get_address(zip):
    global address
    global state
    if zip == "":
        return None, None
    try:
        response = requests.get("https://viacep.com.br/ws/" + zip + "/json/")
        response = response.json()
        if not response:
            return
        address = response.get("logradouro", "") + ", " + response.get("bairro", "") + ", " + response.get("localidade", "")
        state = response.get("uf", "")
    except:
        address = "Please add a valid postal code"

def get_regional_price(uf):
    if state in south_states:
        return 10
    elif state in center_states:
        return 20
    elif state in north_states:
        return 30
    return 0

def final_price():
    if discount == True:
        return get_regional_price(state) + weight + urgency - 10
    else:
        return get_regional_price(state) + weight + urgency