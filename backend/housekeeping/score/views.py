from housekeeping.globalFunc import js_ok, js_error
from order.models import Order
from service.models import Service
from user.models import User
from .models import Score

# Create your views here.
def myScore(request):
    """
    查看我写的全部评价信息
    请求方式：GET
    """
    username = request.session.get('username')
    user = User.objects.get(username = username)
    scoreList = Score.objects.filter(customer = user)
    context = []
    for score in scoreList:
        context.append({
            'serviceTitle': score.service.title,
            'timeScore': score.timeScore,
            'serviceScore': score.serviceScore,
            'description': score.description,
        })
    return js_ok(context)

def serviceScore(request, serviceId):
    """
    查看服务的评价
    请求方式：GET
    """
    username = request.session.get('username')
    user = User.objects.get(username=username)
    services = Service.objects.get(id = serviceId)
    if Score.objects.filter(customer=user,service=services)is not None:
        serviceList = Score.objects.filter(customer=user,service=services)
        context = []
        for service in serviceList:
            context.append({
                'serviceTitle': service.service.title,
                'timeScore': service.timeScore,
                'serviceScore': service.serviceScore,
                'description': service.description,
            })
        return js_ok(context)
    else:
        if Score.objects.filter(service=services)is not None:
            return js_error(401,'该评价未授权')
        else:
            return js_error(404, '该评价未找到')


def newScore(request, serviceId):
    """
    创建评价
    请求方式：GET、POST混合
    请求参数：serviceId、timeScore、serviceScore、description、images
    """
    username = request.session.get('username')
    user = User.objects.get(username=username)
    services = Service.objects.get(id=serviceId)
    if Score.objects.filter(customer=user,service=services)is None:
        if Order.objects.filter(customer=user,service=services)is not None:
            timeScore=request.POST.get('timeScore')
            serviceScore=request.POST.get('serviceScore')
            description=request.POST.get('description')

            Score.objects.create(service=services,customer=user,
                                 timeScore=timeScore,serviceScore=serviceScore,
                                 description=description)
            return js_ok('新建评价成功')
        else:
            js_error(401, '没有权限评价此服务')
    else:
        js_error(502, '该评价已存在')
