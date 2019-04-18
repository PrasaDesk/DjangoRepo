import requests
import json

BASE_URL = "http://localhost:8000/"


# sample data for test which include right and wrong type of data
payload = [
    {"username": "prasad", "password": "yeole@123"},
    {"username": "prasad", "password": "yeole@12"},
    {"username": "uno1", "password": "uno@123"},
    {"username": "lion", "password": "lion@123"},
    {"username": "pras", "password": "yeole@123"},
    {"username": "prasad"},
    {},
    [],
    ()  # this is empty object
]

# test function


def test_login(payload):
    response = requests.post(BASE_URL + "login/", data=payload)

    return {"status ": response, "Pass": response.ok}

    # print("status : ", response)
    # print("Pass : ", response.ok)
    # print("response data : ", json.dumps(response.json(), indent=4))
    print('------------------------------------------------------------------')


total_test = 0
pass_test = 0
faild_test = 0
# passing data for test function
i = 0
for data in payload:
    print(total_test + 1, "| Data:", data, end="|:result ||| ")
    response = test_login(data)
    print(response)

    total_test = total_test + 1
    if(response['Pass'] == True):
        pass_test = pass_test + 1
    else:
        faild_test = faild_test + 1


print("\nTotal Test : ", total_test)
print("Pass test  : ", pass_test)
print("Faild test : ", faild_test)

print("\nALL test Done ....!!!\n")
