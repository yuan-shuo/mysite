from django.shortcuts import render, HttpResponse, redirect
from app01.models import onlyTitle, UserInfo

# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")

def tpl(request):

    # 数据分割不写','
    name = 'Y'
    arr = ['first', 'second', 'third']
    user_info = {'name': 'S', 'salary': 1000, 'role': 'CEO'},

    user_list = [
        {'name': "diyi", 'salary': 55000},
        {'name': "er", 'salary': 65000},
        {'name': "san", 'salary': 75000},
    ]

    return render(request, "tpl.html", {
        'name':name,
        'array':arr,
        'dic': user_info,
        'arrPlusDic': user_list,
        })


# 会根据注册顺序，依次从各个app的templates中寻找"userlist.html"

# 但如果是pycharm创建可能会在settings里DIR位置import os，此时从根目录先开始，否则：根目录中的无效

def userList(request):
    return render(request, "userlist.html")

def rdc(request):
    return redirect("https://www.baidu.com/?tn=15007414_pg")


def login(request):
    # request.GET就是通过url传过来的数据:url=www.xxx.com?name=yy&age=10
    if request.method == "GET":
        print(request.GET)
        return render(request, "login.html")
    
    # request.POST就是html通过post方式提交回来的数据
    elif request.method == "POST":
        # <QueryDict: {'csrfmiddlewaretoken': ['xxx(your_random_key)'], 'user': ['usename'], 'pwd': ['123456']}>
        print(request.POST)

        # 将POST获得的数据交给变量，以此来使用POST传过来的数据
        username = request.POST.get('user')
        password = request.POST.get('pwd')

        if username == 'root' and password == '1234':
            # return HttpResponse("登陆成功!")
            return redirect("https://www.baidu.com/?tn=15007414_pg")
        else:
            return render(request, 'login.html', {'error_msg': '登陆失败'})


def orm(request):

    # 创建
    # onlyTitle.objects.create(title="H1")
    # onlyTitle.objects.create(title="H2")
    # onlyTitle.objects.create(title="H3")

    # UserInfo.objects.create(name="yuan", password=456, age=12)

    # 全删
    # onlyTitle.objects.all().delete()
    # 删除id=3的数据
    # onlyTitle.objects.filter(id=3).delete()

    # 查询
    # data_list = [obj(1 row), obj(2 row)]
    # data_list = onlyTitle.objects.all()
    # for obj in data_list:
    #     print(obj.title)

    # data_firList = onlyTitle.objects.filter(id__gte = 1)
    # print (data_firList[0].title)

    # data_firObj = onlyTitle.objects.filter(id__gte = 1).first()
    # print (data_firObj.title)

    # 修改
    # onlyTitle.objects.all().update(title="H3")
    # onlyTitle.objects.filter(title="H3").update(title="H5")

    return HttpResponse("成功")

def show(request):
    dataList = UserInfo.objects.all()
    # print(dataList)

    return render(request, 'info_list.html', {'dataList': dataList})

def get(request):
    if request.method == 'GET':
        return render(request, 'input_list.html')
    
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")
    UserInfo.objects.create(name=user, password=pwd, age=age)
    return redirect('http://127.0.0.1:8000/info/show/')

def delete(request):
    if request.method == 'GET':
        nid = request.GET.get("nid")
        UserInfo.objects.filter(id=nid).delete()
        # return HttpResponse(f"提示：-id为{nid}的用户已被删除-")
        return redirect('/info/show/')