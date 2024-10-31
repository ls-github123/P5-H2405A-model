#发短信
from ronglian_sms_sdk import SmsSDK
import  json
accId = '8a216da878005a800178a251439d39da'
accToken = 'dc4fd2e2a23e45a68474dbc6d1233eda'
appId = '8a216da878005a800178a251449839e1'

def send_message(mobile,code):
    sdk = SmsSDK(accId, accToken, appId)
    tid = '1'
    mobile = mobile
    datas = (code,)
    resp = sdk.sendMessage(tid, mobile, datas)
    data = json.loads(resp)
    if data['statusCode'] == '000000':
        return True
    return False


from .pay import AliPay
def get_alipay():
    # 初始化支付实例
   
    #公共参数
    # 沙箱环境地址：https://openhome.alipay.com/platform/appDaily.htm?tab=info
    app_id = "9021000136628093"  #  APPID （沙箱应用）

    # 支付完成后，支付偷偷向这里地址发送一个post请求，识别公网IP,如果是 192.168.20.13局域网IP ,支付宝找不到，def page2() 接收不到这个请求
    notify_url = "http://localhost:8000/alipaycallback/"

    # 支付完成后，跳转的地址。
    return_url = "http://localhost:8000/alipaycallback/"

    merchant_private_key_path = "keys/private.txt" # 应用私钥
    alipay_public_key_path = "keys/public.txt"  # 支付宝公钥

    alipay = AliPay(
        appid=app_id,
        app_notify_url=notify_url,
        return_url=return_url,
        app_private_key_path=merchant_private_key_path,
        alipay_public_key_path=alipay_public_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥
        debug=True,  # 默认False,
    )
    return alipay
