from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from MasterGPT.core.Key import *
from MasterGPT.core.Chat import Chat as ChatGPT

chatgpt = ChatGPT()

def chat(request):
    chats = Chat.objects.all()
    return render(request, 'chat.html', {
        'chats': chats,
    })

@csrf_exempt
def Ajax(request):
    # Check if request is Ajax
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':

        text = request.POST.get('text')

        chatgpt.append_history(chatgpt.set_message("user", text))
        response = chatgpt.get_reply(chatgpt.chat(chatgpt.get_history()))

        chat = Chat.objects.create(
            text = text,
            gpt = response
        )

        return JsonResponse({'data': response,})
    return JsonResponse({})
