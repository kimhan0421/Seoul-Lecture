from django.shortcuts import render


def index(request):
    formula = request.GET.get('formula')
    if formula:
        result = eval(formula)
    else:
        result = None
    context = {
        'result': result
    }
    return render(request, 'calculator.html', context)
