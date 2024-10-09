import requests,json
class BDapi():
    def __init__(self) -> None:
        self.API_KEY = "tDGnh7BmUWauc0xocyfmG4qS"
        self.SECRET_KEY = "onMC9tZvQwrxdM2Dv1iEnTzeLsIC7ivS"
    def get_access_token(self):
        """
        使用 AK，SK 生成鉴权签名（Access Token）
        :return: access_token，或是None(如果错误)
        """
        url = "https://aip.baidubce.com/oauth/2.0/token"
        params = {"grant_type": "client_credentials", "client_id": self.API_KEY, "client_secret": self.SECRET_KEY}
        return str(requests.post(url, params=params).json().get("access_token"))
    
    def audit_mes(self,mes):
        url = "https://aip.baidubce.com/rest/2.0/solution/v1/text_censor/v2/user_defined?access_token=" + self.get_access_token()
        
        payload='text='+mes
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload)
        data = json.loads(response.text)
       
        if data['conclusion'] == '合规':
            return mes
        else:
            return "内容不合法"
        
bdapi = BDapi()
# mes = bdapi.audit_mes("我是中国人")
# print(mes)