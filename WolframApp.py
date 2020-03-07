import requests



class WolframApp:
    invoke_key=["question"]
    def WolframQuery(question):
        res=requests.get('http://api.wolframalpha.com/v1/spoken?appid=Y9G82Q-48GA78V7R9&i='+question)
        #return(res.content)
        return(res.text)


if __name__=='__main__':
    #testing query
    print(WolframApp.WolframQuery("Henry Ford"))

