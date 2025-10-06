from django.shortcuts import render

def calculate_power(request):
    power = None
    error = None

    if request.method == 'POST':
        print("Request method is used")

        try:
            current = float(request.POST.get('current'))
            resistance = float(request.POST.get('resistance'))

            power = (current ** 2) * resistance

            print("Current:", current)
            print("Resistance:", resistance)
            print("Power:", power)

        except (TypeError, ValueError):
            error = "Please enter valid numeric values."
            print("Invalid input received.")

    return render(request, 'mathapp/math.html', {
        'power': power,
        'error': error
    })

