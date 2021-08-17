# import requests

# numbers=[6351795102,8140850582]

# def Send_OTP():
#     url = "https://www.fast2sms.com/dev/bulk"
#     api = "HU1ds79pyEkuKPLwBeVDlatr04f6GMbjqiRS2ZICAvg8NTJ5OzdvIHb8SYtz3iUFrmONPZ5QDRJfnA7l"
#     querystring = {"authorization": api, "sender_id": "FSTSMS", "message": "Hey happy indian independence day ",
#                    "language": "english", "route": "p", "numbers": 8140850582}
#     headers = {
#         'cache-control': "no-cache"
#     }
#     return requests.request("GET",url, headers=headers, params = querystring)

# Send_OTP()

import requests
url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=FSTSMS&message=Happy Independent Day&language=english&route=p&numbers=6351795102"
headers = {
'authorization': "HU1ds79pyEkuKPLwBeVDlatr04f6GMbjqiRS2ZICAvg8NTJ5OzdvIHb8SYtz3iUFrmONPZ5QDRJfnA7l",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)