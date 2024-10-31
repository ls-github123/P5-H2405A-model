from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serilizers import *

# Create your views here.

class TestView(APIView):
    def get(self,request):
        pass
        # roles = TestRole.objects.all()
        # ser = TestRoleSer(roles,many=True)
       
        # return Response({"code":200,'mes':ser.data})
    def post(self,request):
        ser = TestRoleSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"code":200,'mes':'添加成功'})
        else:
            print(ser.errors)
            return Response({"code":200,'mes':ser.errors})
        
class ResourseView(APIView):
    def post(self,request):
        data = request.data
        ser = ResourceSer(data=data)
        if ser.is_valid():
            ser.save()
            return Response({"code":200,'mes':''})
        else:
            return Response({"code":10010,'mes':ser.errors})
    def get(self,request):
        pass
        
from django.core.paginator import Paginator   
        
class RolesView(APIView):
    def post(self,request):
        data = request.data
        ser = ResourceSer(data=data)
        if ser.is_valid():
            ser.save()
            return Response({"code":200,'mes':''})
        else:
            return Response({"code":10010,'mes':ser.errors})
    def get(self,request):
        #获取角色列表、搜索、分页
        sname = request.GET.get('sname')
        page_size = int(request.GET.get('page_size',1))
        page = int(request.GET.get('page',1))
        #查询
        if sname:
            roles = Roles.objects.filter(name=sname).all()
        else:
            roles = Roles.objects.all()
           
        pag = Paginator(roles,page_size)
        #获取当前页的数据
        rdata = pag.page(page)
        ser = RolesSer(rdata,many=True)
        #引入分页类处理
        #返回数据
        return Response({"code":200,'rlist':ser.data,'total':pag.count})
        
#获取资源列表及此角色对应的所有资源
class RolesResourseView(APIView):
    def get(self,request):
        #获取roleid
        roleid = request.GET.get('roleid')
        #获取所有资源pid_id >0
        res = Resource.objects.filter(pid_id__gt=0).all()
        #数组重组  key label
        reslist = [{"key":i.id,'label':i.name} for i in res]
        #获取角色
        role = Roles.objects.filter(id=roleid).first()
        #获取角色对应的资源
        values1 = list(role.resource.values('id'))
        print(values1)
        resource = role.resource.all()
        values = [i.id for i in resource]
        #返回资源id列表
        return Response({"code":200,'reslist':reslist,'values':values})
    
    def post(self,request):
        #位运算优化代码
        # #获取角色id
        # roleid = request.data.get("roleid")
        # #返回的是权限表中的promition
        # values = request.data.get("values")
        
        # allpromition = 0
        # #定义新配制的权限
        # promition = 0
        # #定义权限列表，为了查询互斥表
        # alllist=[]
        # #遍历权限，获取获取|值
        # for i in values:
        #     alllist.append(i)
        #     promition = promition | i
            
        # allpromition = allpromition | promition
        # #资源的互斥
        # roles = Roles.objects.filter(id=roleid).first()
        # parent = roles.pid.promition
        # resource = Resouce.objects.filter(pid_id__gt=0).values('promition')
        # for i in resource:
        #     if i & parent >0:
        #         alllist.append(i['promition'])
            
       
        # #查询互斥表
        # testabc = Testabc.objects.filter(res1__in=alllist).values('res2')
        # for i in testabc:
        #     if i.res2 & allpromition>0:
        #         return Response({"code":10010})
            
        # roles.promition = promition
        # roles.save()
        
        #获取角色id
        roleid = request.data.get("roleid")
        #获取选中的资源列表[1,2,3]
        values = request.data.get("values")
        #根据id查询角色
        role = Roles.objects.filter(id=roleid).first()
        # 获取此角色继承的父类的资源列表
        res2 = role.pid.resource.all()
        
        idlist = values
        for i in res2:
            idlist.append(i.id)
        
        # 获取到此角色配制的资源列表
        # 生成一个列表，放入所有资源id
        #要配制的资源
        # 查询互斥表 用in查询 新的互斥id [{"res2":1}]
        tests = TestAbc.objects.filter(res1__in=idlist).values('res2')
        #互斥资源
        tlist = [i['res2'] for i in tests]
        # 遍历获取到所有互斥id列表
        # 取资源列表和互斥列表的交集，如果大于0说明有互斥，提示不能配制
        # # 将列表转换为集合  
        set1 = set(idlist)  
        set2 = set(tlist)  
        
        # 交集（intersection）  
        intersection = set1.intersection(set2)  
        if len(intersection)>0:
            return Response({"code":10010,'mes':'存在互斥资源，不能配制'})
       
        #删除此角色对应的所有权限
        role.resource.clear()
        #添加新的权限
        role.resource.add(*values)
        return Response({"code":200,'mes':'添加成功'})
        
# 定义两个列表  
# list1 = [1, 2, 3, 4, 5]  
# list2 = [4, 5, 6, 7, 8]  
  
# # 将列表转换为集合  
# set1 = set(list1)  
# set2 = set(list2)  
  
# # 交集（intersection）  
# intersection = set1.intersection(set2)  
  
# # 差集（difference），即存在于第一个集合但不在第二个集合中的元素  
# difference_set1 = set1.difference(set2)  
  
# # 反向差集（difference），即存在于第二个集合但不在第一个集合中的元素  
# difference_set2 = set2.difference(set1)  
  
# # 差交集（symmetric difference），即只存在于一个集合中的元素  
# symmetric_difference = set1.symmetric_difference(set2)  
   

from tools.myjwt import mjwt
from tools.myredis import r
import time,json
#登录接口
class Login(APIView):
    def post(self,request):
        #根据userid获取role，获取资源到资源，把资源列表返回给vue
        name = 'zs'
        users = AdminUser.objects.filter(name=name).first()
        if users:
            #位运算开始-----
            #此角色现有权限 用户角色表  userid  roleid  
            # promition1 = users.role.promition
            # promition2 = users.role.pid.promition
            # promition = promition1 | promition2
            # #查询所有资源不包括菜单
            # resource = Resource.objects.filter(pid_id__gt=0).all()
            # prolist = []
            # for i in resource:
            #    if  i.promition & promition >0:
            #        prolist.append({"id":i.id,'name':i.name,'url':i.url,'pid':i.pid.id,'pname':i.pid.name})
            #位运算结束-----
            #用户对应的所有资源列表
            userres1 = list(users.role.resource.all())
            userres2 = list(users.role.pid.resource.all())
            userres =userres1 +userres2
            #定义返回的列表
            reslist=[]
            #把父id存入，去重
            idslist =[]
            #接口权限
            interface=[]
            menulist = []
            #遍历列表，获取所有父类,获取资源表中的菜单
            for i in userres:
                menulist.append(i.url)
                #资源对应的接口权限
                interdata = i.interface.all()
                for inter in interdata:
                    interface.append(inter.url)
                #获取资源的父id
                pid = i.pid.id
                if pid not in idslist:
                    reslist.append({"id":pid,'name':i.pid.name,'son':[]})
                    idslist.append(pid)
                    
            #遍历所有资源
            for j in userres:
                #遍历菜单
                for index,s in enumerate(reslist):
                    #当前资源属于哪个菜单，放到哪个菜单下
                    if j.pid.id == s['id']:
                        reslist[index]['son'].append({"id":j.id,'name':j.name,'url':j.url})
           
            #遍历列表，判断当前子类属于哪个父类写到哪个父类的son中
            token = mjwt.jwt_encode({"data":{"userid":1,'exp':int(time.time())}})
            #获取接口权限
            r.set_str('user1promition',json.dumps(interface))
            return Response({"code":200,'menulist':reslist,'mpromition':menulist,'token':token})
        else:
            return Response({"code":10010})
        
    def get(self,request):
        roles = Roles.objects.filter(id=1).first()
        res1 = roles.resource.all()
        res2 = roles.pid.resource.all()
        res = list(res1) +list(res2)
       
        for i in res:
            print(i.id,i.name,i.pid)
        return Response({"code":200})
    
