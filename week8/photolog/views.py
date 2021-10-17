from django.shortcuts import render, redirect
from .models import Potolog


def list(request):
    phtolog_all = Potolog.objects.all()
    context = {'phtolog_all': phtolog_all}
    return render(request, 'photolog/list.html', context)


def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        image = request.FILES['image']
        Potolog.objects.create(
            title=title,
            image=image
        )
        return redirect('photolog:list')
    else:
        return render(request, 'photolog/form.html')
