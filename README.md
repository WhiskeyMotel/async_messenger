# What's it?

This is a simple messanger, that uses asynchrony and have a basic visual interface, which uses Qt libs.

It was created for... for looking for new experience, donnow.

# Requirements

Repo has the dedicated file, so if you use something like PyCharm, it will help you to install 'em. Otherwise, 
    
    pip install -r requirements.txt
    
# Functionality and working process

Basically, you need to run `server.py` at first, then you can run `app.py` and work. 

If you use client at different PC, you need to change server's IP at `async def start` method of class `MainWindow`.
At first, type `login:*your nickname*`, then you can type anything. Also, it will show you last 10 messages before the moment
you entered the chat.

# TODO

* Create window which will ask you for IP adress:port
* Something more...
