import socket 
import time 
import threading
import tkinter
root = tkinter.Tk()
root.title("Admin Chat")
root.geometry("430x500")
root.config(bg="white")
conversation=["\n".center(120)]

def func():
    t = threading.Thread(target=recv)
    t.start()

def recv():
    listensocket = socket.socket()
    port = 3000
    host= 'localhost'
    maxconnection = 2
    listensocket.bind((host, port))
    listensocket.listen(maxconnection)
    (clientsocket,address) = listensocket.accept()

    while True:
        sendermessage =clientsocket.recv(1024).decode() 
        if not sendermessage == "":
            time.sleep(5)
            conversation.append("Client: "+sendermessage)
            text.set("\n".join(conversation))
            label.update()

xr = 0
s = socket.socket()
def sendmessage():
    global xr # send
    if xr==0:
        hostname = 'localhost'
        port = 4000
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

buttons = tkinter.Button(root,text="start",command=func,borderwidth=0)
buttons.place(x=200,y=10)

message = tkinter.StringVar()
messagebox = tkinter.Entry(root,textvariable=message,font=('calibre',10,'normal'),border=2,width=42)
messagebox.place(x=10,y=444)

sendmessagebutton = tkinter.Button(root,text="send",command=threadsendmsg,borderwidth=0)
sendmessagebutton.place(x=350,y=444)
text = tkinter.StringVar()

label = tkinter.Label(root, textvariable=text,height=20,width=43,justify=tkinter.LEFT,
                     anchor='nw',font={"family":"Arial Black", "size":20})
label.place(x=15,y=80)

# lstbx = tkinter.Listbox(root,height=20,width=43)
# lstbx.place(x=15,y=80)

root.mainloop()
