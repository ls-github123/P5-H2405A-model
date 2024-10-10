import redis
from redis import ConnectionPool
class Mredis():
    def __init__(self) -> None:
        pool = ConnectionPool()
        self.r = redis.Redis(connection_pool=pool)
        
        
    #list add  del  find pop len  rpoplpush
    def list_add(self,key,value):
        return self.r.rpush(key,value)
    
    def list_pop(self,key):
        return self.r.rpop(key)
    
    def list_lrange(self,key,min,max):
        return self.r.lrange(key,min,max)
    
    def list_llen(self,key):
        return self.r.llen(key)
    
    def list_lrem(self,key,value):
        return self.r.lrem(key,-1,value)
    
    def list_rpoplush(self,list1,list2):
        return self.r.rpoplpush(list1,list2)
    
    
mredis = Mredis()
# mredis.list_add('bdlist1','1001')
# mredis.list_add('bdlist1','1002')
# mredis.list_add('bdlist1','1003')
# mredis.list_lrem('bdlist1','1001')
# list = mredis.list_lrange('bdlist1',0,-1)
# print(list)