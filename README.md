# Rasa Human handoff using Socket Programming and API

**Note:** For this code your Bot must be deployed somewhere, you can use Heroku-it's free

Sorry For Tkinter 😊

![Human Handoff (2)](https://user-images.githubusercontent.com/63470232/155241877-91460b64-8c6d-4075-802c-1874b20fa1c6.png)

For Clarification

**User &#8594; Customer\
Admin &#8594; Customer Care\
Bot &#8594; RASA Bot**

There are many ways to Handle or  make connection between User and Admin some are:
- Using Rasa Action Server
- Using custom backend and frontend for your chat Interface
- Rasa Action Server + Frontend Command Change or Button change

In this Repository we have opted for second option

![User](https://user-images.githubusercontent.com/63470232/155243688-5432607f-fc3c-404c-aa2d-5638dc15b5f0.png)

## Task happen

- connection is stablised between User and Bot-server.
- User asked for Human intervention.
- We create a  Intent for recognizing Wheather User is asking for Human Handoff.
- A custom action is attached to that intent and that can be our Trigger message.
- or if you are looking for third option then We can handled it using a `custom message` and `CoversationPaused()` using Action Server, here custom message can be Trigger message.
- Don't worry about conversation paused, as we will be not forwarding any message to bot server after the Trigger message.
- After trigger we can stablised connection between User and Admin.

```python
if ast.literal_eval(x.text)[0]["text"] == "Human Handoff":
        conversation.append('Bot: Admin is connecting please wait for few minutes')
        conversation.append('Admin: Hello i am your admin. How can i help you')
        text.set("\n".join(conversation))
        label.update()
        func()
        sendmessagebutton.configure(text = "Human send",command=sendmessage)
```
Here `Human Handoff` is our trigger message, when our user interface recevied this message it will throw response and change the function related to the button. You can do it using flag also.

- Now a connection is stablised between Admin and User, and there is no intervention of Bot as we are not forwarding any message to it.
- Now Admin and User can have a Normal Chat.
- We have created a list of the previous message that can be send as form of packet, so that Admin can know the previous chat with Bot and User.

## To run the file

`python Bot-server.py`\
`python Admin server.py`

## Task yet to be done
 - [ ] Send a notification to Admin, "Hey! user want to interact with you"
 - [ ] Implement using flask, for Web App

**Note:- The code are edited and comment are added, removed unnecessary code.**
