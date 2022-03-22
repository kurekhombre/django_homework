from django.shortcuts import render

import calculator

# Create your views here.
def calc(request):
    context = {

    }
    return render(request, 'calculator/calculator.html')

def add(request, value1, value2):
    sum = value1 + value2
    context = {
        "value1": value1,
        "value2": value2,
        "sum": sum
    }
    return render(request, 'calculator/add.html',context=context)

def substract(request, value1, value2):
    sum = value1 - value2
    context = {
        "value1": value1,
        "value2": value2,
        "sum": sum
    }
    return render(request, 'calculator/substract.html',context=context)

def multiply(request, value1, value2):
    sum = value1 * value2
    context = {
        "value1": value1,
        "value2": value2,
        "sum": sum
    }
    return render(request, 'calculator/multiply.html',context=context)

def divide(request, value1, value2):
    try:
        sum = value1 / value2
    except ZeroDivisionError: 
        sum = "Operation not allowed!"
    context = {
        "value1": value1,
        "value2": value2,
        "sum": sum
    }
    return render(request, 'calculator/divide.html',context=context)