import random
from django.http.response import HttpResponse

from django.shortcuts import render


def index(request):
    # lotto_number = [1, 2, 3, 4]
    # return HttpResponse(lotto_number)
    lotto_number = random.sample(range(1, 46), 7)
    return render(request, 'lotto.html', {'number': lotto_number})

    # context = {
    #     'lotto_number': lotto_number,
    # }
    # return render(request, 'lotto.html', context)
