from rest_framework.decorators import api_view
from rest_framework.response import Response
import openai

openai.api_key = "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"

@api_view(['POST'])
def chat_view(request):
    if request.method == 'POST' and 'user_input' in request.data:
        user_input = request.data['user_input']

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Interact Ai"},
                {"role": "user", "content": user_input},
            ],
            temperature=0.5,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            n=1,
            stop=["\nUser:"],
        )

        bot_response = response["choices"][0]["message"]["content"]
        return Response({'response': bot_response})

    return Response({'error': 'Invalid request'})
