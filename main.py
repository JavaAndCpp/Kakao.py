from kakaopy.client import Client
import json

class main(Client):
  async def onMessage(self, chat):
    print(chat.message)
    
    if chat.message == "power":
      await chat.reply("kakaopy is runnnnnnnnning~")
      
    if chat.message == "Hello":
      attachment = {'mentions': [{'user_id': chat.authorId, 'at': [1], 'len': 2}]}
      await chat.channel.sendChat("Hello~ " + "@태그",json.dumps(attachment),1) 
      
      #If you have open chat permission 
      if chat.message == ".hide":
        await.chat.hide()
        
