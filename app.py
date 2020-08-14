# Manages the DocBot Flask application

from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
import threading
import time

import chat
import autoopen

# Create the flask object
app = Flask(__name__, template_folder = "templates", static_folder = "static")

conversations = []
status = "Online"

# Function to add a message to conversations
def add_msg (message, mtype) :
	timemsg = datetime.now().strftime("%H:%M | %B %d")
	response = [mtype, message, timemsg]
	conversations.append(response)

# Function to initialize the conversation
def start_conversing() :
	add_msg("Hello! I am DocBot, a digitally trained medical consultant", 0)
	add_msg("To finish this consultation, enter 'stop'", 0)

# Function to get a reply from the bot
def respond (message) :
	time.sleep(1)
	global status
	status = "Online"
	answer = chat.reply(message)
	add_msg(answer, 0)

# Binds the base URL to the 'consult' function
@app.route('/', methods = ['POST', 'GET'])
def consult() :
	if request.method == 'POST' :
		try :
			message = request.form['message']
			if message == "" :
				pass
			elif message.lower() == "stop" :
				time.sleep(1)
				conversations.clear()
				start_conversing()
			else :
				add_msg(message, 1)
				global status
				status = "Typing ..."
				t = threading.Thread(target = respond, args = (message, ))
				t.start()
			return redirect('/#chat')
		except :
			return "There was an error reaching DocBot"
	else :
		return render_template('consult.html', conv = conversations, status = status)

# Main method
if __name__ == "__main__" :
	start_conversing()
	timer = threading.Timer(2, autoopen.flaskopen)
	timer.start() 
	app.run()
