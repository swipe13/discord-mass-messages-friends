import discord
from colorama import Fore, Style
import os 
def Cls():
    os.system('cls')
message = input("What message do you want to send? :  ")

Cls() 

client = discord.Client()
b = Style.BRIGHT
print(f"""

{b+Fore.GREEN}
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |    _______   | || | _____  _____ | || |     _____    | || |   ______     | || |  _________   | |
| |   /  ___  |  | || ||_   _||_   _|| || |    |_   _|   | || |  |_   __ \   | || | |_   ___  |  | |
| |  |  (__ \_|  | || |  | | /\ | |  | || |      | |     | || |    | |__) |  | || |   | |_  \_|  | |
| |   '.___`-.   | || |  | |/  \| |  | || |      | |     | || |    |  ___/   | || |   |  _|  _   | |
| |  |`\____) |  | || |  |   /\   |  | || |     _| |_    | || |   _| |_      | || |  _| |___/ |  | |
| |  |_______.'  | || |  |__/  \__|  | || |    |_____|   | || |  |_____|     | || | |_________|  | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 



Developed for everyone's good :)
                                                                                    
{b+Fore.BLUE} > {Fore.RESET}MASS DM
{b+Fore.BLUE} > {Fore.RESET}Creator: Swipe

""")

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send(message)
      print(f"""{b+Fore.YELLOW} > {Fore.RESET} Message sent to: {user.name}""")
    except:
       print(f"""{b+Fore.RED} > {Fore.RESET} Message not sent to:  {user.name}""")

client.run("", bot=False)