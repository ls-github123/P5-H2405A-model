# 请求地址：http://apis.juhe.cn/simpleWeather/query
# 请求参数：city=%E5%8C%97%E4%BA%AC&key=545cf0be******325cf6c4
# 请求方式：GET
# Header： 
#    Content-Type：application/x-www-form-urlencoded
import requests
res = requests.get('http://apis.juhe.cn/simpleWeather/query',params={"city":'北京',"key":"545cf0bec2b0682dcc2c8f68325cf6c4"},headers={"Content-Type":"application/x-www-form-urlencoded"})
print(res.text)