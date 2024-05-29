from Functions import clean_text
import requests
import json

# Function to send text to the Flask server for prediction
def request_text(text):
    clean_text(text)
    url = 'http://127.0.0.1:5000/predict'
    headers = {'Content-Type': 'application/json'}

    data = {
        'text' : [text]  # Actual Dialect: SD
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print('\n\n' + '-'*65 + '')
        print('\t\t' + 'Prediction:\t\t', response.json()['prediction'])
        print('' + '-'*65 + '\n')
        print('\t\t' + "Classes:       'EG'  'LB'  'LY'  'MA'  'SD'")
        print('\t\t' + 'Probability:', response.json()['probability'])
        print('\n' + '-'*65 + '\n\n' )
    else:
        print('Error:', response.status_code, response.text)

        
# Creating GUI for user to either enter dialect or type something to exit
print('\n\n' + '-'*50 + '\n')
print('\t\t' + 'Welcome to Dialect Identifier')
print('\n' + '-'*50 + '\n\n')

while True:
    text = input('Enter Arabic text or type "exit" or "خروج" to quit: ')
    if text.lower() == 'exit' or text == 'خروج':
        break
    else:
        request_text(text)

    