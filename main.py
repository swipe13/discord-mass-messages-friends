import discord
from colorama import Fore, Style
import os 
def Cls():
    os.system('cls')
message = input("Qual a menssagem que quer enviar ? :  ")

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



 Desenvolvido para o bem de todos :)
                                                                                    
{b+Fore.BLUE} > {Fore.RESET}MASS DM
{b+Fore.BLUE} > {Fore.RESET}Creator: Swipe

""")

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send(message)
      print(f"""{b+Fore.YELLOW} > {Fore.RESET} Mensagem Enviada para: {user.name}""")
    except:
       print(f"""{b+Fore.RED} > {Fore.RESET} Mensagem não enviada para:  {user.name}""")






client.run('YOUR TOKEN', bot=False)