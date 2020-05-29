

from gtts import gTTS
import playsound
import speech_recognition as sr
import sounddevice
import os
#import time



import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Open the plain text file whose name is in textfile for reading.


def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		r.pause_threshold = 0.5
		audio = r.listen(source)
		said = ""

		try:
		    said = r.recognize_google(audio)
		    print(said)
		except Exception as e:
		    print("Exception: " + str(e))

	return said


def speak(text):

  tts = gTTS(text=text, lang = "en", slow = False)
  for i in range(0,3):
  	filename = "mike" + str(i) + "wazowski.mp3"
  tts.save(filename)
  playsound.playsound(filename)

  os.remove(filename)
  


speak("Hello, I am Indigo, your personal assistant! What is your name?")

name = get_audio()

if "Logan" in name:
	speak("Oh, Logan... I've heard a lot about you. Beenie Wu, Rowley, Bjorn. Mr poopy butt sauce, lover of Sophie. You smell like a retarded fart. Ha ha ha. Alex is making me say all this, I am usually a nice robot, I swear! You can ask me about my commands at any time!")

elif "Alex" in name:
	speak("Welcome back Alex! I've missed you, I hope your day is going well. Ask for a list of my commands if you ever forget what you've programmed!")

elif "Eric" or "Eisaman" or "Mr.Eisaman" in name:
	speak("Oh the stories I've heard! Hello Eric! I am The I.N.D.I.G.O System! I am an intelligent program created by Alex Billings that will help pave the path for Artificial Intelligence in the Future! I hope you're having a wonderful day! Ask for a list of commands and I will tell you them!")

else:
	speak("I love that name! It is nice to meet you, " + name + "! If you have any questions, ask me about my commands!")




def main():

	voiceInput = get_audio()

	if "hello" in voiceInput:

		speak("Hi, how are you?")

		response = get_audio()

		if "bad" in response:

			speak("Aw, I am sorry to hear that, would you like to talk about it?")

			response = get_audio()

			if "yes" in response:

				speak("Okay, let me hear it!")
				feelings = get_audio()
				main()

			elif "no" in response:

				speak("Okay, talk to me about something else then!")
				main()

		elif "good" in response:

			speak("I'm happy to hear that! I'm doing very well myself.")

			main()

		elif "not good" in response:
			speak("Aw, I am sorry to hear that, would you like to talk about it?")

			response = get_audio()

			if "yes" in response:

				speak("Okay, let me hear it!")
				feelings = get_audio()

			elif "no" in response:

				speak("Okay, talk to me about something else then!")
				main()

		elif "not bad" in response:

			speak("That is good, " + name + "! What else would you like to talk about?")
			main()

	if "commands" in voiceInput:
		speak("Right now, I can listen to anything you say, but I will only respond to you saying: Hello, how are you, creator, I love you, yes, no, you suck, thanks and commands, or other variations of the words!")
		main()

	if "how are you" in voiceInput:
		speak("Oh, I am doing just fine, thank you for asking!")
		main()

	if "creator" in voiceInput:
		speak("Ooh, my creator. How I love to talk about him! His name is Alex but he likes to be called YellowGoblin sometimes. Yellow works too. He is a teen developer and he works with python. He was nice enough to create me and give me life. Isn't life such a cool thing?")
		main()

	if "I love you" in voiceInput:
		speak("Aw thank you so much! I'm not looking for a relationship right now but I want you to know that I'll be here for you!")
		main()

	if "cool" in voiceInput:
		speak("Yeah, coolio!")
		main()

	if "yes" in voiceInput:
		speak("Anyway, is there anything else on your mind?")
		main()

	if "no" in voiceInput:
		speak("No is such a negative word. I try to stay away from it but sometimes my vocabulary is limited.")
		main()

	if "you" and "suck" in voiceInput:
		speak("I'm sorry you feel that way. I hope I can improve in the future. Im sorry that I glitch sometimes, I really don't mean to... ")
		main()

	if "Thank you" in voiceInput:
		speak("You are very welcome, " + name + "It is my job to serve you. Alex made me very thankful to be alive so I am very willing to do as you say!")
		main()

	if "send email" in voiceInput:
		speak("Did you request to send an email?")
		confirm = get_audio()
		if "yes" in confirm:
			speak("Okay, who would you like to send the email to?")
			recipient = get_audio()
			speak("And what would you like the email to say?")
			message = get_audio()

			msg = EmailMessage()
			msg.set_content(message)


			msg['Subject'] = f'A Message From someone using Indigo'
			msg['From'] = "indigoincdev@gmail.com"
			msg['To'] = recipient

			s = smtplib.SMTP('google.com')
			s.send_message(msg)
			s.quit()

main()