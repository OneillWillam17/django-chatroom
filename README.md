# django-chatroom
Chatroom using the django framework and channels.

# How it works
The actual backend for the website runs off django's framework and takes advantage of their channels plugin that works similar to js websockets.
When a user connects to the site's chatroom it adds them to a channel group named 'chat'. The channel group contains the messages sent and allows them to send messages with the rest of the users. 

# Builiding the app
This was my first real time working with html/css/js and django. Pretty much 4 new languages / styles of development that I have no prior experience working with. So as expected I ran into a lot of problems getting started. The biggest issue was with the javascript, I didn't want to just copy paste someone else's code for my chatroom, I wanted to understand how each bit worked within it so that altering it / fixing it if need be would be easier in the future. The javascript is a simple websocket program, it takes some data that a user entered and posts it to a text area on the same page.

# HTML / CSS
Doing the HTML / CSS work for the site was actually pretty enjoyable, even though I had no idea how either languages worked, I picked up the key concepts after a few hours and quickly made progress organizing the site to how I envisioned. The only issues I ran into here were the amount of time, since I was constantly looking up how to do a specific things, like customizing HTML inputs to look a specific way on one page, but not on the others. 

# Images 
![imgur](https://i.imgur.com/vsEu1D1.png "Intro Page")

![imgur](https://i.imgur.com/X7ExyjC.png "Chatroom")
