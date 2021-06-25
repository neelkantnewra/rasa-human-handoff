
import requests
import tkinter
import ast


root=tkinter.Tk()
root.geometry("670x800")
root.title("ChatBot")
# root.resizable(0,0)
text = tkinter.StringVar()
conversation=["        Welcome for Assistant       \n".center(120)]
text.set("\n".join(conversation))

# scrollbar = tkinter.Scrollbar(root)
# scrollbar.pack( side = tkinter.RIGHT, fill = tkinter.Y )

#==================Server code===========================
import socket

s = socket.socket()
host = 'localhost'
print('server will be hosted on: ',host)
port = 1234
s.bind((host,port))
print('Server is bounded succesfully')
s.listen(1)
conn,addr = s.accept()
print(addr,"has connected")



label = tkinter.Label(root, textvariable=text,height=40,width=60,justify=tkinter.LEFT,
                     anchor='nw',font={"family":"Arial Black", "size":20})
                      # yscrollcommand = scrollbar.set)
label.grid(row=0,column=0)
# display=tkinter.Label(root,height=40,width=50)
# display.grid(row=0,column=0)
entry=tkinter.Entry(root,width=72)
entry.grid(row=5,column=0)


def ReadText():
    message=entry.get()
    conversation.append("User: "+message)
    text.set("\n".join(conversation))
    label.update()

    url = "WEB_HOOK_FOR_RASA_BOT"
    #  ##change rasablog with your app name
    # url = 'http://127.0.0.1:3000'
    myobj = {
        "message": message,
        "sender": "Prachi",
    }
    entry.delete(0, 'end')
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
    conversation.append("Neelkant: " + reply)

    if ast.literal_eval(x.text)[0]["text"] == "I am a bot, powered by Rasa.":
        entry.delete(0, 'end')
        conversation.append('Neelkant: Admin is connecting please wait for few minutes')
        conversation.append('Admin: Hello i am your admin. How can i help you')
        text.set("\n".join(conversation))
        label.update()
        button.configure(text = "Human send",command=Sendmessage)
        #my code 

    print([list(i.keys())[1] for i in ast.literal_eval(x.text)])
    if 'image' in [list(i.keys())[1] for i in ast.literal_eval(x.text)]:
        def OpenImage():
            import webbrowser
            webbrowser.open(ast.literal_eval(x.text)[1]["image"].replace("\\",""))
        conversation.append("Neelkant: " + ast.literal_eval(x.text)[1]["image"].replace("\\",""))
        b = tkinter.Button(root, text="Open Image",command=OpenImage).pack(...)
    text.set("\n".join(conversation))

def Sendmessage():
    message=entry.get()
    conversation.append("User: "+message)
    text.set("\n".join(conversation))
    label.update()
    message = message.encode()
    conn.send(message)
    entry.delete(0, 'end')
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    conversation.append("Admin: "+incoming_message)
    text.set("\n".join(conversation))
    label.update()
    entry.delete(0, 'end')


button=tkinter.Button(root,text="Send",command=ReadText)
button.grid(row=5,column=40)

root.configure(background='orange')
label.configure(background='orange')

root.mainloop()
