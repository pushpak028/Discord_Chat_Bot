from discord import Intents , Client 
from discord.ext import commands
import load_json
import response
from importlib import reload
reload(response)


def run_bot(token):
    intents = Intents.default()
    intents.message_content = True
    client = Client(intents = intents)
    kb:dict = load_json.load1("intents.json")

    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
        channel_id = "enter your discord channel_id"
        channel = client.get_channel(channel_id)
        if channel:
            tags = [i["tag"] for i in kb["intents"]]
            k = "enter anything from below tags:"
            await channel.send(k)
            await channel.send(tags)
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 
 
        if message.content:
            print(f'({message.channel}) ({message.author}):"({message.content})"')
            result = response.chatbot(str(message.content))
            if result:
                await message.channel.send(result)
            else:
                k = "please try again macha"
                await message.channel.send(k)
    
    client.run(token=token)

if __name__ == "__main__":
    run_bot('enter your bot token')