import socket 
import time 
import threading
import tkinter
root = tkinter.Tk()
import requests
import ast
root.geometry("430x500")
root.config(bg="white")
root.title("User chat")
conversation=["\n".center(120)]

def func():
    t = threading.Thread(target=recv)
    t.start()

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
            time.sleep(5)
            # lstbx.insert(0,"Admin: "+sendermessage)
            conversation.append("Admin: "+sendermessage)
            text.set("\n".join(conversation))
            label.update()

xr = 0
s = socket.socket()
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
    

def threadsendmsg():
    th = threading.Thread(target = sendmessage)
    th.start()

def ReadText():
    message=messagebox.get()
    conversation.append("Client: "+message)
    text.set("\n".join(conversation))
    label.update()
    messagebox.delete(0, 'end')

    url = 'http://innovate-yourself.herokuapp.com/webhooks/rest/webhook' 
    #  ##change rasablog with your app name
    # url = 'http://127.0.0.1:3000'
    myobj = {
        "message": message,
        "sender": "Prachi",
    }
    
    x = requests.post(url, json=myobj)
    ast.literal_eval(x.text)
    print(ast.literal_eval(x.text))
    # conversation.append("Innovate: "+"\n".join([ast.literal_eval(x.text)[0]["text"].split(" ")[3*(i-1):3*(i-1)+3] if len(ast.literal_eval(x.text)[0]["text"].split(" "))//10 >10 else ast.literal_eval(x.text)[0]["text"] for i in range(len(ast.literal_eval(x.text)[0]["text"].split(" "))//10)]))

    reply=""
    if len(ast.literal_eval(x.text)[0]["text"].split(" ")) >9:
        for i in range(len(ast.literal_eval(x.text)[0]["text"].split(" "))//9 +1):
            reply+=" ".join(ast.literal_eval(x.text)[0]["text"].split(" ")[9 * (i - 1):9 * (i - 1) + 9]) + "\n"
    else:
        reply=ast.literal_eval(x.text)[0]["text"]
    # lstbx.insert(0,"Bot: "+reply)
    conversation.append("Bot: "+reply)
    text.set("\n".join(conversation))
    label.update()

    if ast.literal_eval(x.text)[0]["text"] == "I am a bot, powered by Rasa.":
        conversation.append('Bot: Admin is connecting please wait for few minutes')
        conversation.append('Admin: Hello i am your admin. How can i help you')
        text.set("\n".join(conversation))
        label.update()
        func()
        sendmessagebutton.configure(text = "Human send",command=sendmessage)
        #my code 

    print([list(i.keys())[1] for i in ast.literal_eval(x.text)])
    # if 'image' in [list(i.keys())[1] for i in ast.literal_eval(x.text)]:
    #     def OpenImage():
    #         import webbrowser
    #         webbrowser.open(ast.literal_eval(x.text)[1]["image"].replace("\\",""))
    #     conversation.append("Neelkant: " + ast.literal_eval(x.text)[1]["image"].replace("\\",""))
    #     b = tkinter.Button(root, text="Open Image",command=OpenImage).pack(...)
    # text.set("\n".join(conversation))
# buttons = tkinter.Button(root,text="start",command=func,borderwidth=0)
# buttons.place(x=200,y=10)

message = tkinter.StringVar()
messagebox = tkinter.Entry(root,textvariable=message,font=('calibre',10,'normal'),border=2,width=42)
messagebox.place(x=10,y=444)

text = tkinter.StringVar()
label = tkinter.Label(root, textvariable=text,height=20,width=43,justify=tkinter.LEFT,
                     anchor='nw',font={"family":"Arial Black", "size":20})
label.place(x=15,y=80)


sendmessagebutton = tkinter.Button(root,text="send",command=ReadText,borderwidth=0)
sendmessagebutton.place(x=350,y=444)

# lstbx = tkinter.Listbox(root,height=20,width=43)
# lstbx.place(x=15,y=80)

root.mainloop()
