from django.shortcuts import render
from .monkeyFunc import monkey_writting
from django.http import JsonResponse
import json

# Create your views here.

def index_view(request):
    return render(request, 'index.html', {})
def loading_view(request):
    return render(request, 'results.html')

def return_monkey_metrics(request, stri):

    # Verificar string:
    if stri is None:
        return JsonResponse({'message': 'error', 'error': 'Campo faltantes'}, status=400)

    # Procesar y devolver:
    iters, duration = monkey_writting(str(stri))
    if iters != 'Error' and duration != 'Error':
        data = {'iters': f'{iters:,}', 'duration': round(duration, 2)}
        return JsonResponse({'message': 'success', 'data': data})
    else:
        return JsonResponse({'message': 'error', 'error': 'Caracteres inválidos'}, status=400)