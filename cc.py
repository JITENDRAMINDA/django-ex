from pyrogram import Client, Filters
app = Client('890398475:AAFKe-e5H2owXvzoB-AlIpy3ELE-0f7OoNs')
@app.on_message(Filters.chat(-1001369162545) & Filters.text)
def forawrd(client, message):
    file = open("text.txt" , "r")
    lines = file.readlines()
    file.close()
    for line in lines:
      if not line == "closed":
         client.forward_messages(-1001297100007,-1001369162545, [message.message_id], 'bool = None ', 'bool = True' , 'bool = True' )
@app.on_message(Filters.command('status'))
def main(client, message) :
    if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
      file = open("text.txt" , "r")
      lines = file.readlines()
      file.close()
      for line in lines:
        if line == "started":
           message.reply("line is on ! ")
        if line == "closed":
           message.reply("line is stopped ! ")
    if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
      file = open("text.txt" , "r")
      lines = file.readlines()
      file.close()
      for line in lines:
        if line == "started":
           message.reply("line is on ! ")
        if line == "closed":
           message.reply("line is stopped ! ")        
@app.on_message(Filters. private)
def ran( client, message) :
  client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
@app.on_message(Filters.command('offline'))
def main(client, message) :
   if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
    file = open("text.txt" , "w")
    file.write("closed")
