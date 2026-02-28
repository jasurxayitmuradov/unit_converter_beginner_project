# converter/views.py
from django.shortcuts import render

# converter/views.py
def main_page(request):
    return render(request , 'converter/main')

def length_converter(request):
    result = None
    context = {}
    
    if request.method == "POST":
        value = float(request.POST.get('value'))
        from_u = request.POST.get('from_unit')
        to_u = request.POST.get('to_unit')

        factors = {
            'millimeter': 0.001, 'centimeter': 0.01, 'meter': 1.0, 
            'kilometer': 1000.0, 'inch': 0.0254, 'foot': 0.3048
        }

        # Calculation
        meters = value * factors[from_u]
        result = meters / factors[to_u]

        # Send data back to the template
        context = {
            'result': result,
            'original_value': value,
            'from_unit': from_u,
            'to_unit': to_u
        }

    return render(request, 'converter/length.html', context)


def weight_converter(request):
    result = None
    context = {}
    
    if request.method == "POST":
        value = float(request.POST.get('value'))
        from_u = request.POST.get('from_unit')
        to_u = request.POST.get('to_unit')

        # Factors relative to 1 Gram
        factors = {
            'milligram': 0.001,
            'gram': 1.0,
            'kilogram': 1000.0,
            'ounce': 28.3495,
            'pound': 453.592,
        }

        # Step 1: Convert to grams | Step 2: Convert to target
        grams = value * factors[from_u]
        result = grams / factors[to_u]

        context = {
            'result': result,
            'original_value': value,
            'from_unit': from_u,
            'to_unit': to_u
        }

    return render(request, 'converter/weight.html', context)

def temprature_converet(request):
    result = None
    context = {}

    if request.method == "POST":
        value = float(request.POST.get('value'))
        from_u = request.POST.get('from_unit')
        to_u = request.POST.get('to_unit')

        if from_u == 'Fahrenheit':
            celsius = (value-32)*(5/9)
        elif from_u == 'Kelvin':
            celsius = value - 273.15
        else:
            celsius = value
        
        if to_u == 'Fahrenheit':
            result = celsius*(9/5) + 32
        elif to_u == 'Kelvin':
            result = celsius + 273.15
        else:
            result = celsius

        context = {
            'result':result,
            'original_value':value,
            'from_unit': from_u,
            'to_unit': to_u
        }

    return render(request , 'converter/temperature.html' , context)

        