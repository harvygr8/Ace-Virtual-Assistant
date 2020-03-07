import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import tflearn
import tensorflow   
import json
import random 
import pickle
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import requests, json


#importing VA modules
from NewsFeedApp import *
from WeatherApp import *
from WolframApp import *

from flask import Flask, render_template, request


stemmer=LancasterStemmer()
with open("intents.json") as file:
    data=json.load(file)

print(data['intents'])



try:
    x
    with open("data.pickle","rb") as f:
        words,labels,training,output=pickle.load(f) 


except:
    words=[]
    labels=[]
    ignored_words=['!','#','_','?','*','&','@']
    docs_x=[]
    docs_y=[]

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds=nltk.word_tokenize(pattern)
            words.extend(wrds)  #since already a list just extend the list and add words to it
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if(intent["tag"] not in labels):
            labels.append(intent["tag"])


    words=[stemmer.stem(w.lower()) for w in words if w != ignored_words]
    words=sorted(list(set(words)))

    labels=sorted(labels)

    training=[]
    output=[]

    out_empty=[0 for _ in range(len(labels))]


    #creating a OneHotEncoded Bag of words model
    for x,doc in enumerate(docs_x):
        bag=[]
        wrds=[stemmer.stem(w) for w in doc]            #stemming for docs list , for words list already done  
        
        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)
        
        output_row=out_empty[:]
        output_row[labels.index(docs_y[x])]=1

        training.append(bag)
        output.append(output_row)


    training=np.array(training)
    output=np.array(output)

    with open("data.pickle","wb") as f:
        pickle.dump((words,labels,training,output),f) 



tensorflow.reset_default_graph()            #reset previous settings

net=tflearn.input_data(shape=[None,len(training[0])])
net=tflearn.fully_connected(net,8)          #hidden layer 1 with 8 neurons
net=tflearn.fully_connected(net,8)          #hidden layer 2 with 8 neurons
net=tflearn.fully_connected(net,len(output[0]),activation="softmax")
net=tflearn.regression(net)

model=tflearn.DNN(net)


model.load("AceBotModel.tflearn")
#model.fit(training,output,n_epoch=1000,batch_size=8,show_metric=True)
#model.save("AceBotModel.tflearn")
    

def bag_of_words(s,words):
    bag=[0 for _ in range(len(words))]
    s_words=nltk.word_tokenize(s)
    s_words=[stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i,w in enumerate(words):
           if w==se:
                bag[i]=1
    return np.array(bag)


def getNews():
    #self.clear()
    ns=NewsFeedApp.shownews()
    i=0
    for news in ns:
        print(str(news.title.text))
        i=i+1
        if(i==5):
            break

def test():
    s='news'
    return s


#class ConversationApp:

def start_chat(inp):
    while True:
        if inp.lower=="quit":
            break

        results=model.predict([bag_of_words(inp,words)])
        results_index=np.argmax(results)
        tag=labels[results_index]
        print(tag)
        
        for tg in data['intents']:
            if tg['tag']==tag:
                responses=tg['responses']
                print(tg)

        res=random.choice(responses)
        return res


app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    if userText in NewsFeedApp.news_keys:
        ns=NewsFeedApp.shownews()
        i=0
        nl=[]
        for news in ns:
            nl.append(str(news.title.text))
            i=i+1
            if(i==5):
                break
        return (str(nl))

    elif userText in WeatherApp.weather_keys:
            return(str('Looks like '+WeatherApp.fetchWeatherLabel()+'°C'))

    if str('question') in userText:
            print(userText)
            a=WolframApp.WolframQuery(userText[8:])
            print(a)
            return str(a)

       
        #NewsFeedApp.test()

    else:
        ans=start_chat(str(userText))
        return ans


if __name__ == "__main__":
    app.run()
       

    
