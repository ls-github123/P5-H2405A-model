### 1.CDN加速

~~~
CDN是构建在现有网络基础之上的智能虚拟网络，依靠部署在各地的边缘服务器，通过中心平台的负载均衡、内容分发、调度等功能模块，使用户就近获取所需内容，降低网络拥塞，提高用户访问响应速度和命中率。

CDN加速是指通过将资源缓存在网络边缘节点，减少传输时延、减轻源站压力，从而提高网站访问速度和用户体验的技术手段。相应的，CDN加速的应用场景主要有以下几个方面：

1、静态资源加速：如图片、视频、音频等静态资源，这些资源不随着用户请求发生变化且占据大量的带宽资源，放置在CDN节点上可以使得用户可以直接从最近的节点获取静态资源，加速用户访问。

2、动态内容加速：如动态页面中的HTML、CSS等内容，虽然每次请求内容都可能不同，但CDN节点可以缓存一些常用内容，降低源站压力以及加速用户访问。

3、文件下载加速：如客户端更新、软件包、文档等可以通过CDN进行加速，避免因为带宽限制或者访问量过大导致下载速度过慢问题。

4、视频直播加速：因为直播需要实时转发视频流，而一般源站带宽资源承载能力较差，所以可以将视频内容分发到CDN节点，提高转发效率和稳定性，保证用户观看体验。

CDN加速的应用场景非常广泛，可以为静态资源、动态内容、文件下载以及视频直播等多方面提供帮助。同时，CDN节点的位置、数量和稳定性等方面，都是决定CDN加速效果的关键因素，需要根据业务需求和用户群体特点进行选择和配置。

~~~

### 七牛云cdn配制

https://developer.qiniu.com/fusion/1228/fusion-quick-start

### 2.防盗链

<img src="http://www.jy.com/static/1.jpg" />

~~~
1.七牛云平台上添加公司所有的域名
2.打开视频地址判断，获取到视频对应referer，通过referer查找允许的列表，如果存在才会播放，如果不存在，无权查看

http标准协议中有专门的字段记录referer

1、他可以追溯到请求时从哪个网站链接过来的。

2、来对于资源文件，可以跟踪到包含显示他的网页地址是什么。因此所有防盗链方法都是基于这个Referer字段
~~~

https://developer.qiniu.com/fusion/3839/domain-name-hotlinking-prevention

### 3.大文件上传

10G文件网慢、断点续传

~~~
大文件
断点续传

分治算法
分
治
分治,即分而治之。这是一种将大规模问题分解为若干个规模较小的相同子问题,进而求得最终结果的一种策略思想。

1.vant中引入图片上传组件，before_upload方法中获取文件大小，定义每片上传大小，计算总片数
2.开始上传 splice(0,end),向服务器传递的参数 文件名，文件总大小，总片数，当前这一片的流，当前片数索引
3.服务器接收，保存在服务器上，在服务器上创建一个临时文件夹名字是文件名
4.获取文件夹总大小和文件的总大小对比，如果相同说明已经上传完成。合并操作，删除临时文件夹
5.上传成功合并的时候突然由于网络或服务器问题导致没有合并成功，将文件名和文件大小保存在redis中zset中，合并成功的直接删除，celery定时任务从redis读取文件名以及文件大小去服务器查询小文件总大小，如果小文件总大小和文件大小一致说明上传成功合并失败，合并的操作，删除小文件。如果大小不同把小文件直接删除



1。获取文件大小 
2.计算总片数  math.ceil(文件大小/每片大小)  1024*1024  2mb
3.上传（判断服务端返回200，代表全部完成，如果返回其他状态码递归调用自己再上传下一片）


接口：
1.接收文件流，存入 filename_0  filename_1  filename_2
2.合并 判断总片数和当前上前的片数相同，代码全部上传完毕。合并，把临时文件删除





分片上传
文件流

分治算法
大文件-》拆分单个处理-》合并
start :0 ,end 2*1024*1024
start 2*1024*1024  end  4*1024*1024
大文件 2*1024*1024-》单个上传-》返回结果-》全部成功合并

接口：单个上传接口
     获取流，创建文件夹以文件名 1   0  1  2  3  4
     合并接口 ：查询文件名下所有的文件，遍历文件写出到同一个文件，把文件夹删除
     
     
 vue slice文件切隔-》单个文件上传-》static/upload/
                                             2.mp4

~~~

vue代码

~~~
<template>
  <div>
  <van-form @submit="onSubmit">
  <van-field
    v-model="form.title"
    name="标题"
    label="标题"
    placeholder="标题"
    :rules="[{ required: true, message: '标题' }]"
  />
  <van-field
    v-model="form.content"
    name="内容"
    label="内容"
    placeholder="内容"
    :rules="[{ required: true, message: '内容' }]"
  />

  文件上传<van-uploader :after-read="afterRead" :before-read='beforeRead'/>
  <div>


  </div>

  <div style="margin: 16px;">
    <van-button round block type="info" native-type="submit">提交</van-button>
  </div>
</van-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      count:0,
      tcount:0,
      filename:'',
      file:'',
     form:{'cateid':1,'imgurl':'1.jpg','title':'','content':'','userid':1},
     lang: 'zh',
      searchword: '',
    };
  },
  methods: {
    onSubmit(values) {
      this.axios.post("adminuser/publishVedio",this.form).then(res=>{

      })
    },
    beforeRead(file){
      this.file = file
      this.filename = file.name
      //计算文件总片数
      this.tcount = Math.ceil(file.size/(1024*1024))
      return true
    },
    async uploadf(data){
       await this.axios.post('fileupload/',data).then(res=>{
           alert("22")
        })
    },
    afterRead(file){
        var data = new FormData()
        var start = this.count *(1024*1024)
        var end= (this.count+1)*(1024*1024)
        // 0  1024*1024
        // 1024*1024  2*1024*1024
        //当前上传的文件流
        data.append("file",this.file.slice(start,end))
        //文件名
        data.append("filename",this.filename)
        //一共有多少片
        data.append("tcount",this.tcount)
        //当前上传的索引
        data.append("count",this.count)
       
        this.uploadf(data)
       
        if(this.count == this.tcount-1){
            alert('上传成功')
        }else{
            this.count++
            this.afterRead(file)
        }
    },
    
  },
};
</script>

<style>

</style>
~~~



django代码

配制

~~~python
STATIC_URL = '/static/'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
#定义上传文件夹的路径
UPLOAD_ROOT = os.path.join(BASE_DIR,'static/upload')
~~~



~~~python
from .views import *
from django.urls import path,re_path
from videoadmin.settings import UPLOAD_ROOT
#导入文件路由库
from django.views.static import serve


urlpatterns = [
    path('geturl', Wb.as_view()),
    path('user/weiboCallback/',WbCallback.as_view()),
    re_path('^upload/(?P<path>.*)$',serve,{'document_root':UPLOAD_ROOT}), 
    path('fileupload',fileupload),
    # path('wsconn/<int:id>',websocketLink),
    # path('sendsms',websocketSendsms),
    path('recommend_movies',recommend_movies)
]
~~~



~~~python
import os   
from videoadmin import settings  
#文件上传
def fileupload(request):
    #获取参数
    data = request.POST
    img = request.FILES.get('file')
    filename = data['filename']
    tcount = int(data['tcount'])
    count = int(data['count'])
    import os   
import shutil
 
def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                size = os.path.getsize(fp)
                total_size += size
            except OSError:
                pass  # Ignore files that can't be accessed
    return total_size
import uuid
#文件上传
def fileupload(request):
    #获取参数
    data = request.POST
    img = request.FILES.get('file')
    filename = data['filename']
    tcount = int(data['tcount'])
    count = int(data['count'])
    size = int(data['size'])
    fname = uuid.uuid1().hex
    #上传代码 os.rename() uuid.uuid().hex
    arr = filename.split('.')
    filepath = f'./static/upload/{filename}'
    if not os.path.exists(filepath):
        os.mkdir(f'./static/upload/{filename}')
    
    with open(f'./static/upload/{filename}/{count}', 'wb') as f:
        for chunk in img.chunks():
            f.write(chunk)
            # f.close()
    fsize = get_folder_size(filepath)
    if size == fsize:
        #合并
        with open(f'./static/upload/{fname}.{arr[1]}', 'wb') as f:
            for i in range(tcount):
                with open(f'./static/upload/{filename}/{i}', 'rb') as chunk:
                    f.write(chunk.read())
        #删除文件夹
        # if os.path.exists(filepath):
        #     shutil.rmtree(filepath)
         #os.remove(f'./static/upload/{filename}/{i}')
        return JsonResponse({"code":200})
    else:
         return JsonResponse({"code":10010})
~~~

### 文件上传失败

~~~
一共5片，上传成功3片
第一片上传的时候把文件名和大小存入zset中   uploadfilelist  1232  asfsdd.mp4
合并成功后从zset中删除
celery定时

~~~



话术总结

~~~
近期我的是一个短视频社区，我主要负责的是发布模块，输入标题选择分类发布视频。目前总会员数10万，活跃用户5万左右，每天新增3万条。mysql超过1000万性能会急速下降，业界标准500-600万分一张表。所以我们分了3张表。采用的水平分表，水平分表有唯一id的问题，采用的雪花算法。uuid的优点是在内存中生成速度快，缺点是无序唯一串。字段串长查询效率低，只是一个唯一的串，没有实际意义。mysql自增ID单独维护一张表，并且表的存储有限制，当数据量到达一定程序给id再分表，增加项目的复杂度。redis内存型数据库，原子性保证唯一，持久化机试弱，可能导致数据丢失。雪花算法是由64位构成的，每一位是符号位，41位时间搓精确到毫秒级，还有5位机器码5位服务码，12位随机码构成。每秒生成百万个不重复的id.单体应用下唯一。分布式环境下有可能导致时钟回拨的问题。解决方案把最新生成的存入到redis中，下一次生成对比，如果小于等于上一次生成的说明发生了时钟回拨，需要重新生成。如果大于，进行业务操作。把当前生成的覆盖redis.在视频上传中，我采用的是分治算法对文件进行分片上传，前端上传前获取文件大小除以每片大小获取到总算数，上传的过程传递单片文件流，文件名，文件总片数和当前片数。接口获取到数据用文件名创建一个临时文件夹，把每一片都放到临时文件夹下。如果当前片数和总片数相同代码文件上传完成，执行合并操作。遍历读取临时文件夹下的所有文件写出。删除临时文件和文件夹
~~~

~~~
淘宝
商户：  名字、二级域名

http://www.taobao.com/<str:id>/
http://www.taobao.com/2/
~~~

