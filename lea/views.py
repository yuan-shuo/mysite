from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .utils.archi import Archi
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        #  and request.POST.get("ckey") == "ys"
        data = json.loads(request.body)
        print(data)
        s_l = data['s_l']
        n_l = data['n_l']
        qu_b = data['qu_b']
        qd_b = data['qd_b']
        r_b = data['r_b']
        n_b = data['n_b']
        c_b = data['c_b']
        k = data['k']
        enterk = data['enterk']
        enterv = data['enterv']

        enter = dict(zip(enterk, enterv))
        # print(s_l, n_l, qu_b, qd_b, r_b, n_b, c_b, enter)
        archi = Archi(
            s_l=s_l, n_l=n_l,
            qu_b=qu_b, qd_b=qd_b, r_b=r_b, n_b=n_b, c_b=c_b,
            enter=enter,k=k
            )
        apiRes = {
            "len": archi.len_val(), #str*1
            "stair": archi.stair_enscape(), #list[str*3]
            "width": archi.width(), #list[str*2]
            "equip": archi.equ(), #list[str*4]
            "enter": archi.entrance() #list[list[n*str]*2]
        }
        return JsonResponse(apiRes, safe=False)
    return HttpResponse("none")