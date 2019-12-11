from django.shortcuts import render

# Create your views here.
def main(request):
    context = {'like':'Django 很棒'}
    return render(request, 'main/main.html', context)