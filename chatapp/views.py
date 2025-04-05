import requests
from django.shortcuts import render
from .forms import ChatForm

# Replace with your Azure credentials
AZURE_API_KEY = '1HCq7pYRpd1b9OMpBQJYVGyYMfzgyPwNDA5whWSjh68HcS2FLBG5JQQJ99BDACHYHv6XJ3w3AAAAACOGLUBk'
AZURE_ENDPOINT = 'https://ai-moradiyanamra3583ai332823656432.openai.azure.com'
DEPLOYMENT_NAME = 'gpt-4'
API_VERSION = '2025-01-01-preview'

chat_history = []

def chat_view(request):
    global chat_history
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['message']
            chat_history.append({'role': 'user', 'content': user_message})

            headers = {
                'Content-Type': 'application/json',
                'api-key': AZURE_API_KEY,
            }

            data = {
                "messages": chat_history,
                "temperature": 0.7
            }

            url = f"{AZURE_ENDPOINT}/openai/deployments/{DEPLOYMENT_NAME}/chat/completions?api-version={API_VERSION}"

            try:
                response = requests.post(url, headers=headers, json=data)
                if response.status_code == 200:
                    result = response.json()
                    assistant_msg = result['choices'][0]['message']['content']
                    chat_history.append({'role': 'assistant', 'content': assistant_msg})
                else:
                    chat_history.append({'role': 'assistant', 'content': f"Error: {response.status_code} - {response.text}"})
            except Exception as e:
                chat_history.append({'role': 'assistant', 'content': f"Exception: {str(e)}"})
    else:
        form = ChatForm()

    return render(request, 'index.html', {'form': form, 'chat_history': chat_history})
