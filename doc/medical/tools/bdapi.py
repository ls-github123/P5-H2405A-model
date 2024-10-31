
import requests,json
class BaiduApi():
    def __init__(self):
        self.API_KEY = "pUuuJK4QPnSL3JJHLVB1aRZ5"
        self.SECRET_KEY = "rv6oVtOXgjbNioRQSRJWk5dF9CbzZotV"


    def get_access_token(self):
        """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
        url = "https://aip.baidubce.com/oauth/2.0/token"
        params = {"grant_type": "client_credentials", "client_id": self.API_KEY, "client_secret": self.SECRET_KEY}
        return str(requests.post(url, params=params).json().get("access_token"))

    #身份证验证
    def idcard(self,picurl):
        
        url = "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard?access_token=" + self.get_access_token()
    
        # image 可以通过 get_file_content_as_base64("C:\fakepath\1.png",True) 方法获取
        payload='id_card_side=front&url=%s&detect_ps=false&detect_risk=false&detect_quality=false&detect_photo=false&detect_card=false&detect_direction=false'%(picurl)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response

    #文字识别
    def fontmessage(self,picurl):
        url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=" + self.get_access_token()
    
        payload='url=%s&detect_direction=false&paragraph=false&probability=false'%(picurl)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        data = json.loads(response.text)
        name = data['words_result'][0]['words']
        code = data['words_result'][1]['words']
        return {"name":name,'code':code}

bdapi = BaiduApi()
# data = bdapi.fontmessage("http://shfc1pnzg.hb-bkt.clouddn.com/1.png")
# print(data)
    



