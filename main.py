import requests

def web_hook_triger(first, second, third):
    report = {}
    report["value1"] = first
    report["value2"] = second
    report["value3"] = third
    requests.post("https://maker.ifttt.com/trigger/data_entered/with/key/bauu9B0Ig2Rgp4fpi7qTc4", data=report)

while(True):
    web_hook_triger("a", "b", "c")