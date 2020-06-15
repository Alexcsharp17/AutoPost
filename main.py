import requests
from bs4 import BeautifulSoup
def web_hook_triger(first, second, third):
    report = {}
    report["value1"] = first
    report["value2"] = second
    report["value3"] = third
    requests.post("https://maker.ifttt.com/trigger/data_entered/with/key/bauu9B0Ig2Rgp4fpi7qTc4", data=report)


web_hook_triger("a", "b", "c")

class SitePars:
    searString= 'https://www.anekdot.ru/release/anekdot/day/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.125'}

    def GetData(self):
        full_page = requests.get(self.SearString, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        anecdotes=soup.findAll('div',{'class':'text'})[0].text
        web_hook_triger(anecdotes,'test','test')
def Main():
   s= SitePars()
   s.GetData()
Main()