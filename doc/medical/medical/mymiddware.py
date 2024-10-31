from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from tools.myjwt import mjwt
from tools.myredis import r
import time,json

class PermitionMiddleware(MiddlewareMixin):
    def process_request(self,request):
        #定义白名单
        wlist = ['/login/','/sendsms/']
        #获取token
        url = request.path
        if url not in wlist:
            #解析验证
            try:
                token = request.headers.get('Authorization')
                data = mjwt.jwt_decode(token)
                # if int(time.time())< int(data['data']['exp']):
                #     return JsonResponse({"code":401})
                plist = r.get_str('user1promition')
                if plist:
                    plist = json.loads(plist)
                    if url not in plist:
                        return JsonResponse({"code":402})
                else:
                     return JsonResponse({"code":403})
            except:
                return JsonResponse({"code":401})
            #是否过期
            #是否退出
            #是否有接口权限