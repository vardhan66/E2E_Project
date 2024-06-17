from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from chatbot.chatbot_model.main import message

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '').strip().lower()
        if not user_message:
            return JsonResponse({'response': "Sorry, I didn't understand that."})

        response = message(user_message)
        return JsonResponse({'response': response})

    return JsonResponse({'response': "Invalid request method."})