#!/usr/bin/python2
import sys
from pprint import pprint
import time
import threading
import random
import telepot
import random

#VARIABLES
global spamschutz
global bows
bows = 0
spamschutz= 0

#BOT Token
TOKEN = "BOT TOKEN"


def on_chat_message(msg):
	global bows #VARIABLE BOWS
	content_type, chat_type, chat_id = telepot.glance(msg) #?????????
	print 'Chat:', content_type, chat_type, chat_id #?????????
	if content_type != 'text':
		return
#----------------------------------------USER GUI INTERACTION----------------------------------------
	if "/help" in msg['text']:  
		bot.sendMessage(chat_id, helpFunction())
	elif "/joke" in msg['text']:
		bot.sendMessage(chat_id, jokeFunction())
	elif "/bow" in msg['text']: 
		bot.sendMessage(chat_id, bowFunction())
	elif "cute" in msg['text']: 
		bot.sendMessage(chat_id, cuteFunction())
	elif "neet" in msg['text']:
		bot.sendMessage(chat_id, neetFunction())
	elif "weeaboo" in msg['text']:
		bot.sendMessage(chat_id, weeabooFunction())
	elif "kitties" in msg['text']: 
		bot.sendMessage(chat_id, kittiesFunction())
	elif "makefood" in msg['text']:
		bot.sendMessage(chat_id, makefoodFunction())
	elif "makedrink" in msg['text']: 
		bot.sendMessage(chat_id, makedrinkFunction())	
	else:
		bot.sendMessage(chat_id, elseFunction())


#----------------------------------------FUNKTIONS----------------------------------------

def helpFunction():
	message ="/help /cute /bow /joke /makedrink /makefood /neet /weeaboo /kitties"
	return (message)
	
def Rule34Function():
	message ="/Gimme me an input"
	return (imagedata)	

def jokeFunction():
	randomNumber=int(random.randint(0,9))
	jokeArray = ['What do you call an white guy on a cotton plantage?  --  Master',
				'Pajeet stinks like curry',
				'What do you call a hot Indian girl?  --  Bomb Bae',
				'I saw an Indian asleep on the train, noticed the little red dot on his forehead, and thought: Is he on standby?',
				'Having just seen half the staff, I now understand why they call it Currys.',
				'Failed my Politics exam. The question was "Describe the role that India plays in the modern world".  --  Apparently "Tech Support" is not the correct answer.',
				'Why do black people only have nightmares?  --  Because we killed the only one that had a dream. ',
				'Whats the diference between a nigga and a nickel?  --  The nickel is worth something',
				'What do you call 1000 Jews on a train?  --  Anything you want, they are never coming back',
				'Why are the niggas so fast?  --  Cuz the slow ones are in prison']
	message = jokeArray[randomNumber]
	return (message)

def bowFunction():
	bows + 1
	if bows <= 4:
		randomNumber=int(random.randint(0,9))
		bowArray = ['*Bowed*',
					'*Bowed hardly*',
					'*Bowed in kindness*',
					'*Bowed thankfully*',
					'*Bowed angry*',
					'*Bowed emotionless*',
					'*Tried to bow but then facepalmed*',
					'*Bowed to the wrong person*',
					'*Bowed into the wrong direction*'
					]
		message = bowArray[randomNumber]
		return message
	elif bows == 5:
		randomNumber=int(random.randint(0,2))
		bowsecondArray = ['Bahh my back hurts',
					'Outch',
					'asdkalsdj'
					]
		message = bowsecondArray[randomNumber]
		return message

def cuteFunction():
	randomNumber=int(random.randint(0,3))
	cuteArray = ['*Blushed*',
				'D:',
				';-;',
				'this is a little distressing'
				]
	message = cuteArray[randomNumber]
	return message

def neetFunction():
	randomNumber=int(random.randint(0,9))
	neetArray = ['Do you want to eat ramen again tonight ? c:',
				'2D is best!',
				'Am i your waifu? :3',
				'??',
				'??',
				'??',
				'??',
				'??',
				'??',
				'??'
				]
				
	message = neetArray[randomNumber]
	return message
	
def weeabooFunction():
	randomNumber=int(random.randint(0,9))
	weeabooArray = ['*She does a curtsy in a maid dress.*',
				'*You hear humming of "Cruel Angels Thesis".*',
				'Ill try not to hog the kotatsu.',
				'*She offers the other end of a pocky stick in her mouth*',
				'"No, i am not a loli!"',
				'??',
				'??',
				'??',
				'??',
				'??'
				]
				
	message = weeabooArray[randomNumber]
	return message
	
def kittiesFunction():
	randomNumber=int(random.randint(0,9))
	kittiesArray = ['miau',
				'??',
				'??',
				'??',
				'??',
				'??',
				'??',
				'??',
				'??',
				'??'
				]

	message = kittiesArray[randomNumber]
	return message

def makefoodFunction():
	randomNumber=int(random.randint(0,9))
	foodArray = ['A meaty breakfast sizzles as she hums slightly louder then the cooking din.',
				'??',
				'??',
				'??',
				'??',
				'??',
				'??',
				'??',
				'??',
				'??'
				]

	message = foodArray[randomNumber]
	return message

def makedrinkFunction():
	randomNumber=int(random.randint(0,9))
	teaArray = ['A meaty breakfast sizzles as she hums slightly louder then the cooking din.',
				'??',
				'??',
				'??',
				'??',
				'??',
				'??',
				'??',
				'??',
				'??'
				]
				
	message = teaArray[randomNumber]
	return message
	
def elseFunction():
	message = "S-sorry, that i cant help you with that."
	return message
	
#----------------------------------------FUNKTIONS----------------------------------------

#BOT VARIABLEN ????
bot = telepot.Bot(TOKEN)
answerer = telepot.helper.Answerer(bot)
bot.message_loop({'chat': on_chat_message})

#CONSOLEN PRINT BEIM START
print 'Starting to listening ...'

#KEEPING THE PROGRAM ALIVE && WAIT 10 SECONDS AFTER SHE HAS ENDE
while 1:
    time.sleep(10)
    if bows>=6:
      bows = 0
    print bows
'''   
 if spamschutz>=10:
      spamschutz = 0
    print 'Spamschutz' , spamschutz
'''
