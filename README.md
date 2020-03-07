***
# Ace-Virtual-Assistant

##### A Modular Virtual Assistant with a Web,Terminal And Tkinter Interface

***

About
=====

Ace is a Virtual Assistant made in Python which has a modular architecture.
At the core is the VA's 'brain' which contains the chatbot model and all
the modules are then integrated within the apps brain

Each Module is independent from the chatbot modules query and have their own
invocation strings which let the VA know when to call the modules function

This VA was originally had a tkinter UI but that has been removed and for now can run as a flask web app with a "conversation" style interface
For terminal interface see future plans


Note: The App is still a W.I.P as in it doesnt have an exectuable version and to install it on your machine, see the dependecies section

Modules
=======
As of 7th March 2020

* (Core Chatbot and Flask Interface "Brain" App)
* News Feed Application
* Weather Application
* WolframAlpha Query Application

Chatbot
=======
The chatbot works on a Bag of words model using an intents file.
A trained model of the chatbot is available with the app


Dependencies
============
(Python 3.6  or above)

`pip install -r requirements.txt`

TODO
====

-[ ] Make Tkinter Interface
-[ ] TinyAce(Terminal Interface)
-[ ] More Modules

Authors
=======
Harvinder Singh\
Vatsal Mehta\
Saumil Padwal\
Siddarth Nair\
Parth Vora





