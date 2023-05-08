from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def index(request):
    context = {}
    return render(request, "fast_foods/index.html", context)

def train(request):
    accuracy = 0
    context = {"accuracy": accuracy}
    return render(request, "fast_foods/train.html", context)

def predict(request):
    context = {}
    return render(request, "fast_foods/predict.html", context)

def result(request):
    context = {}
    return render(request, "fast_foods/result.html", context)