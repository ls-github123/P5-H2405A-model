
from redis import Redis, ConnectionPool

class Mredis():
    def __init__(self):
        self.pool = ConnectionPool(host='localhost', port=6379, db=0)
        self.r = Redis(connection_pool=self.pool)
        # self.r = Redis(host='124.71.227.70',port=6379)

    #字符串 添加  获取  删除  自增  自减 
    def set_str(self,key,value):
        return self.r.set(key,value)

    #times单位为秒
    def setex_str(self,key,times,value):
        return self.r.setex(key,times,value)
    
    def setnx_str(self,key,value):
        return self.r.setnx(key,value)
    
    def str_incr(self,key,value):
        return self.r.incr(key,value)

    def get_str(self,key):
        value = self.r.get(key)
        if value:
            value = value.decode()
        return value


    #加
    def incr_str(self,key,count):
        return self.r.incr(key,count)

    def decr_str(self,key,count):
        return self.r.decr(key,count)
    def str_del(self,key):
        return self.r.delete(key)


    #hash,添加
    def hash_add(self,key,field,value):
        return self.r.hset(key,field,value)

    #获取对象的所有属性
    def hash_getall(self,key):
        return self.r.hgetall(key)
    #获取对象的某个属性的值
    def hash_getone(self,key,field):
        return self.r.hget(key,field)
    #删除对象的某个属性
    def hash_hdel(self,key,field):
        return self.r.hdel(key,field)
    #模糊查询
    def get_key(self,key):
        return self.r.keys(key)

    #list
    def list_push(self,key,value):
        return self.r.lpush(key,value)

    def list_pop(self,key):
        return self.r.rpop(key)

    def list_lrange(self,key,min,max):
        return self.r.lrange(key,min,max)

    def list_len(self,key):
        return self.r.llen(key)

    def list_del(self,key,field):
        return self.r.lrem(key,-1,field)

    def list_rpoplpush(self,list1,list2):
        return self.r.rpoplpush(list1,list2)

    #zset
    def zset_zadd(self,key,score,value):
        map={value:score}
        return self.r.zadd(key,mapping=map)

    def zset_zrem(self,key,value):
        return self.r.zrem(key,value)

    def zset_zrangebyscore(self,key,min,max):
        return self.r.zrangebyscore(key,min,max)


    #原子性操作的方法
# import time
r = Mredis()
# r.hash_add('doctor1user1','name','zs')
# r.hash_add('doctor1user1','id','1')
# r.hash_add('doctor1user2','name','lishi')
# r.hash_add('doctor1user2','id','2')
# list = r.get_key('doctor1*')
# reslist = []
# for i in list:
#     key = i.decode()
#     values = r.hash_getall(key)
#     # print(values)
#     # {b'name': b'lishi', b'id': b'2'}
#     dict ={}
#     for k,v in values.items():
#         sk = k.decode()
#         sv = v.decode()
#         dict[sk] = sv
#     reslist.append(dict)
# print(reslist)       
# r.zset_zadd('cancleorder',int(time.time()),'1001')
# r.zset_zadd('cancleorder',int(time.time()),'1002')
# r.zset_zadd('cancleorder',int(time.time()),'1003')
# r.zset_zrem('cancleorder','1001')
# time.sleep(1)
# print(r.zset_zrangebyscore('cancleorder',0,int(time.time())))


# r.setnx_str('storecount',20)
# r.str_incr('storecount',-1)
# r.decr_str('storecount',20)
# print(r.get_str('storecount'))

# r.set_str('a','b')
# print(r.get_str('a'))
# times = int(time.time())
# r.zset_zadd('orderscancel1',times,'1001')
# r.zset_zadd('orderscancel1',times,'1002')
# r.zset_zadd('orderscancel1',times,'1003')
# r.zset_zrem('orderscancel1',1003)
# print(r.zset_zrangebyscore('orderscancel1',0,int(time.time())))

# r.list_push('setdockertest',1001)
# r.list_push('setdockertest',1002)
# print(r.list_lrange('setdockertest',0,-1))

# r.list_lpushrpop('setdockertest','setdockertest1')
# print(r.list_lrange('setdockertest',0,-1))
# print(r.list_lrange('setdockertest1',0,-1))

# print(r.list_pop('setdockertest'))
# print(r.list_lrange('setdockertest',0,-1))
#分配业务处理

# r.hash_add('user1course1','name','java课程')
# r.hash_add('user1course1','is_check','true')
# r.hash_add('user1course1','price','10')

# r.hash_add('user1course2','name','python课程')
# r.hash_add('user1course2','is_check','false')
# r.hash_add('user1course2','price','100')

# r.hash_hdel('user1course1','name')
# print(r.hash_getall('user1course1'))

# print(r.get_key('user1*'))
# r.set_str('name','xiaom')
# r.set_str('age',10)
# r.incr_str('age',2)
# print(r.get_str('age'))