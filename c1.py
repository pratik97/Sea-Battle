#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter as tk
import _pickle as cPickle
from tkinter import *
global square1, square2
def receive():
	global buttonArray,boats,data
	"""Handles receiving of messages."""
	'''while True:
	try:
		msg = client_socket.recv(BUFSIZ).decode("utf8")
		msg_list.insert(tkinter.END, msg)
		except OSError:  # Possibly client has left the chat.
			break'''
	while True:
		try:
			print('receiving')
			data = client_socket.recv(4096).decode("utf8")
			# print(data)
			
		except OSError:
			break
    	
    	

def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    '''msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()'''
    print('In Here')


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    #my_msg.set("{quit}")
    send()
def showPosEvent(event):
    print ('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))

def onRightClick(event):
    print ('Got right mouse button click:', 
    showPosEvent(event))
	
def onReadyClick(event):
	print('sending the board to socket') 
	global data, button_dict2
	data_string = str(buttonArray)
	client_socket.send(bytes(data_string,'utf8'))
	print('sent. Now you can play.')
	for i in range(10):
		for j in range(10):
			if data[i*10+j]==1:
				button_dict2[i*10+j].boat = 1
	for i in range(10):
		for j in range(10):
			print(str(button_dict2[i*10+j].boat) + " ")
		print('\n')
def destroyIfBoat(event):
	global data,button_dict2
	
	
	kill = event.widget
	print(str(kill.boat))
	if kill.boat ==1:
		kill.config(bg = 'RED')
	else:
		kill.config(bg = 'BLUE')

def onClick(event):
	global counter,sq1l,sq1f,sq2f,sq2l,square1,square2,k ,messageArray,var
	global button_dict
	#print('Got left mouse button click:', showPosEvent(event))
	if k<9:
		
		button = event.widget
		
		counter += 1
		print(counter)
		if counter == 1:
			square1 = button. buttonNo
			# print(square1)
			sq1l = int(square1) % 10
			sq1f = int((int(square1)/10))%10
			if k >= 6:
				k+=1

		if counter == 2:
			print("k="+str(k))
			if k <6:
				square2 = button.buttonNo
				print(square2)
				sq2l = int(square2) % 10
				sq2f = int((int(square2)/10))%10
				# if x is same 
				if sq1f == sq2f:
					# print("It's Possible")
					print(abs(int(square2)-int(square1))+1)
					if abs(int(square2)-int(square1)+1) == messageArray[k] :
						# print('save it.')
						right = sq1l
						while right != sq2l:
							button_dict[sq1f*10+right].config(bg='RED')
							right+=1
						var.set('Select a block of size %s' % messageArray[k+1])
						k+=1
					else:
						print('Please select block of size %s' % messageArray[k])
				# if y is same
				elif sq1l == sq2l:
					# print("It's Possible")
					print(abs(int(square2)-int(square1))+1)
						# if y is same
					if abs(int(sq1f)-int(sq2f))+1 == messageArray[k]:
						# print('save it.')
						left = sq1f
						while left != sq2f:
							button_dict[left*10 + sq1l].config(bg= 'RED')
							left+=1
						var.set('Select a block of size %s' % messageArray[k+1])
						k+=1

					else:
						print('Please select block of size %s' % messageArray[k])
				else:
					print("Diagonally selection of the blocks is not allowed.")

			if counter % 2 ==0 :
				counter = 0
		caller = event.widget
		if caller.cget('bg') != 'RED':
			caller.config(bg = 'RED')
		else:
			caller.config(bg = 'SystemButtonFace')
	else:
		send()
top = tk.Tk()
top.geometry('1000x880+0+0')
class Board:
	def __init__(self):
		self.name =  'name'
	global player1Buttons,player2Buttons
	player1Buttons = []
	player2Buttons = []
	mainFrame = Frame(top)
	global var,k,messageArray
	var = StringVar()
	mainLabel = Label(top,textvariable=var, relief=RAISED)
	messageArray = [4,3,3,2,2,2,1,1,1,1]
	k=0
	var.set("Select starting position for %s length block."% messageArray[k])
	
	mainLabel.pack(side = TOP)
	mainFrame.pack(side = LEFT)
	player1Frame = Frame(top)
	player2Frame = Frame(top)
	global button_dict,buttonArray,button_dict2
	button_dict = {}
	buttonArray = [[0 for x in range(100)] for y in range(100)]
	global x,y, counter , square1, square2
	square2 = 0
	square1 = 0
	x = 0
	y=0
	w=40
	counter = 0
	for i in range(10):
		temp_buttons = []
		for j in range(10):
			button_dict[i*10+j] = tk.Button(player1Frame,text=" ",height=2, width=3,padx=8,pady=8)
			button_dict[i*10+j].bind('<Button-3>',  onRightClick)
			button_dict[i*10+j].bind('<Button-1>',onClick)
			button_dict[i*10+j].buttonNo = str("%02d" % ((i)*10+j))
			
			#print(b.buttonNo)
			button_dict[i*10+j].grid(row=x, column=y)
			temp_buttons.append(button_dict[i*10+j])
			y = y + w
		x=x+w
		y=0
		player1Buttons.append(temp_buttons)

	player1Frame.pack(side = LEFT)
	x=0
	y=0
	button_dict2 = {}
	for x in range(10):
		temp_buttons = []
		for y in range(10):
			button_dict2[i*10+j] = tk.Button(player2Frame,text=" ",height=2, width=3,padx=8,pady=8)
			button_dict2[i*10+j].bind('<Button-3>',  onRightClick)
			button_dict2[i*10+j].bind('<Button-1>',destroyIfBoat)
			button_dict2[i*10+j].buttonNo = str("%02d" % ((i)*10+j))
			button_dict2[i*10+j].grid(row=x, column=y)
			button_dict2[i*10+j].boat = 0
			# button_dict2[i*10+j],isBoat()
			temp_buttons.append(button_dict2[i*10+j])
			y=y+w
		x=x+w
		y=0
		player2Buttons.append(button_dict2[i*10+j])
	player2Frame.pack(side = RIGHT)	

    
	#getting board ready
	ready = Button(top,text='Ready',height = 7, width = 15,padx= 8,pady=8)
	ready.bind('<Button-1>',onReadyClick)
	ready.pack()

	top.title('Sea Battle')

'''messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("Type your messages here.")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)'''


#----Now comes the sockets part----
HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tk.mainloop()  # Starts GUI execution.