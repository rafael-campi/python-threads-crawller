import time 
import requests

class TestLimitUrl:
    
    range_request=60 #per second
    my_url='' #url in test
    attempt_number=1 #numero de tentativas
    def __init__(self, my_url, attempt_number):
        self.my_url = my_url
        self.attempt_number = attempt_number
        
    def test_by_request(self,):
        r = requests.get(self.url,
                        #proxies={"http":"91.107.210.232:8080", "https":"91.107.210.232:8080"},
                        headers=headers, params=params)
    #def test_by_
 