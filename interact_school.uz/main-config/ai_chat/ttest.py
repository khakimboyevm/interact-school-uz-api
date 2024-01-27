import requests

url = 'http://127.0.0.1:8000/chatai/'
api_key = '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'
headers = {'Content-Type': 'application/json', 'Authorization': f'Token {api_key}'}
data = {'user_input': 'Sen kimsan'}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print('So\'rov muvaffaqiyatli amalga oshmadi. Xatolik kodi:', response.status_code)
