from django.shortcuts import render
from django.http import HttpResponse

# # Create your views here.
#
# # 1.hello world
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
#
# # 2.模板
# def index(request):
#     return render(request, 'login.html')
# def login(request):
#     # if request.method == 'GET':
#     #     name = request.POST.get('name')
#     #     pwd = request.POST.get('pwd')
#     #     context = {'name': name, 'pwd': pwd}
#     #     print(str(context))
#     #     return HttpResponse('登录成功')
#     # else:
#     #     name = request.POST.get('name')
#     #     pwd = request.POST.get('pwd')
#     #     context = {'name': name, 'pwd': pwd}
#     #     print(str(context))
#         return render(request, 'login.html')
#         # return redirect('https://360.com')
#
# # 3.加法计算器
# def add(request):
#     number1 = request.GET.get("number1", 0)
#     number2 = request.GET.get("number2", 0)
#     sum = 0
#     if number1 and number2:
#         sum = int(number1) + int(number2)
#     return render(request, "index.html", {"number1": number1, "number2": number2, "sum": sum})
#

# 4.第四章 模板定义


# def index(request):
# # return HttpResponse("<h1>hello world</h1>")
#     hello = "hi!"
#     name = "张三"
#     return render(request, "index.html", {"hello": hello, "name": name})


# 案例:显示用户列表中所有用户的详细信息
def index(request):
    userlist = [{"name": "zhangsan", "age": 15, "sex": "男"},
                {"name": "lili", "age": 17, "sex": "男"},
                {"name": "san", "age": 16, "sex": "女"},
                {"name": "zhang", "age": 15, "sex": "男"}]
    return render(request, "index.html", {"ulist": userlist})
