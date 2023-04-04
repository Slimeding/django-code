from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 1.hello world
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# 2.模板
def index(request):
    return render(request, 'login.html')
def login(request):
    if request.method == 'GET':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        context = {'name': name, 'pwd': pwd}
        print(str(context))
        return HttpResponse('登录成功')
    else:
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        context = {'name': name, 'pwd': pwd}
        print(str(context))
        return render(request, 'login.html')
        # return redirect('https://360.com')

