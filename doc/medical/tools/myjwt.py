from medical.settings import SECRET_KEY
import jwt

class MJwt():
    def __init__(self):
        self.secret = SECRET_KEY

    #加密
    def jwt_encode(self,data):
        return jwt.encode(data,self.secret,algorithm="HS256")

    #解密
    def jwt_decode(self,token):
        return jwt.decode(token,self.secret,algorithms="HS256")


mjwt = MJwt()
# import time
# user = {"id":1,'name':'234','exp':int(time.time())+3600}
# token = mjwt.jwt_encode(user)
# print(token)
# token = 'eyJ0eXAasfdOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwibmFtZSI6IjIzNCIsImV4cCI6MTcxOTkwNDk0OX0.9G5awjPX6FWGR22FYQDACSK0ZP3RfZPd5ZX1dFvYQxw'
# data = mjwt.jwt_decode(token)
# print(data)
   