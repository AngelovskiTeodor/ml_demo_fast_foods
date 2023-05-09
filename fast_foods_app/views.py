from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .prediction import train as train_model

from os import getcwd as pwd    # debugging

# Create your views here.
@csrf_exempt
def index(request):
    context = {}
    return render(request, "fast_foods/index.html", context)

def train(request):
    print(pwd())    # debugging
    model, mean_squared_error = train_model()
    context = {"mean_squared_error": mean_squared_error}
    return render(request, "fast_foods/train.html", context)

def predict(request):
    context = {}
    return render(request, "fast_foods/predict.html", context)

def result(request):
    context = {}
    return render(request, "fast_foods/result.html", context)