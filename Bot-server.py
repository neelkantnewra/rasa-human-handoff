import socket 
import threading
import tkinter
import requests
import ast

# Tkinter window
root = tkinter.Tk()
root.geometry("430x500")
root.config(bg="white")
root.title("User chat")
conversation=["\n".center(120)]

# threading recv function
def func():
    t = threading.Thread(target=recv)
    t.start()

# receive message from Admin 
def recv():
    listensocket = socket.socket()
    port = 4000
    host= 'localhost'
    maxconnection = 2
    listensocket.bind((host, port))
    listensocket.listen(maxconnection)
    (clientsocket,address) = listensocket.accept()

    while True:
        sendermessage =clientsocket.recv(1024).decode() 
        if not sendermessage == "":
            conversation.append("Admin: "+sendermessage)
            text.set("\n".join(conversation))
            label.update()

xr = 0
s = socket.socket()

# sending message to Admin
def sendmessage():
    global xr # send
    if xr==0:
        hostname = 'localhost'
        port = 3000
        s.connect((hostname,port))
        msg = messagebox.get()
        conversation.append("You: "+msg)
        text.set("\n".join(conversation))
        label.update()
        messagebox.delete(0,'end')
        s.send(msg.encode())
        xr = xr + 1 
    else:
        msg = messagebox.get()
        conversation.append("You: "+msg)
        text.set("\n".join(conversation))
        label.update()
        messagebox.delete(0,'end')
        s.send(msg.encode())
    
# threading the sendmessage function
def threadsendmsg():
    th = threading.Thread(target = sendmessage)
    th.start()

#*****---------- Bot Interaction with User -------******#


def ReadText():
    message=messagebox.get() # Reading message in text-field
    conversation.append("Client: "+message)
    text.set("\n".join(conversation))
    label.update()
    messagebox.delete(0, 'end')

    #------------ CHANGE THIS BEFORE RUNNING ----------#
    url = 'ENTER YOUR BOT WEBHOOK' 
    ###################################################
    
   # creating diconary of message with sender name, You can change sender name if you want
    myobj = {
        "message": message,
        "sender": "Prachi",
    }
    
    # posting the message to our api to get bot response
    x = requests.post(url, json=myobj)
    ast.literal_eval(x.text)
    
    # Bot response is displayed in the display field
    reply=""
    if len(ast.literal_eval(x.text)[0]["text"].split(" ")) >9:
        for i in range(len(ast.literal_eval(x.text)[0]["text"].split(" "))//9 +1):
            reply+=" ".join(ast.literal_eval(x.text)[0]["text"].split(" ")[9 * (i - 1):9 * (i - 1) + 9]) + "\n"
    else:
        reply=ast.literal_eval(x.text)[0]["text"]
    conversation.append("Bot: "+reply)
    text.set("\n".join(conversation))
    label.update()
    
    # if received response from bot is "Human Handoff"
    if ast.literal_eval(x.text)[0]["text"] == "Human Handoff":
        conversation.append('Bot: Admin is connecting please wait for few minutes')
        conversation.append('Admin: Hello i am your admin. How can i help you')
        text.set("\n".join(conversation))
        label.update()
        func()
        sendmessagebutton.configure(text = "Human send",command=sendmessage)

# Text-field
message = tkinter.StringVar()
messagebox = tkinter.Entry(root,textvariable=message,font=('calibre',10,'normal'),border=2,width=42)
messagebox.place(x=10,y=444)

# Display field
text = tkinter.StringVar()
label = tkinter.Label(root, textvariable=text,height=20,width=43,justify=tkinter.LEFT,
                     anchor='nw',font={"family":"Arial Black", "size":20})
label.place(x=15,y=80)

# Button initially with ReadText command
sendmessagebutton = tkinter.Button(root,text="send",command=ReadText,borderwidth=0)
sendmessagebutton.place(x=350,y=444)

root.mainloop()
