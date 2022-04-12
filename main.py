
from tkinter import *
import discord
from discord.ext import commands

root = Tk()

print('если не вставляется токен, попробуйте вставить его по частям (без спец символов(тире, точек и т д), а их вставьте вручную)')
def get_botiks():
    tokenv = token.get()
    activ = activit.get()
    chn = channel.get()
    em = embed1.get()
    emb = embed2.get()
    clr1 = color1.get()
    clr2 = color2.get()
    clr3 = color3.get()
    url = activiturl.get()
    client = commands.Bot(command_prefix='!')
    @client.event
    async def on_ready():
        print('ready')
        await client.change_presence(status=discord.Status.idle, activity=discord.Streaming(name=str(activ), url=str(url)))
        channel = client.get_channel(id=int(chn))
        embed = discord.Embed(title=str(em), description=emb, colour = discord.Colour.from_rgb(int(clr1),int(clr2),int(clr3)))
        await channel.send(embed=embed)


    client.run(str(tokenv))

    

root['bg'] = '#fafafa'
root.title('DiscordBot GUI')
#root.wm_attributes('-alpha', 0.7)

root.geometry('500x500')

root.resizable(width=False, height=False)



root.iconbitmap('icon.ico')


title= Label(root, text='Графический интерфейс Discord бота', bg='white', font=40)
title.pack()

l1 = Label(root, text='Введите токен бота', bg='white')
l1.pack()
token = Entry(root, bg='white')
token.pack()

l2 = Label(root, text='Введите активность бота, пустая если не указана', bg='white')
l2.pack()
activit = 'Активность не указана'
activit = Entry(root, bg='white')
activit.pack()

l9 = Label(root, text='Введите ссылку на активность (может быть любая)', bg='white')
l9.pack()
activiturl = Entry(root, bg='white')
activiturl.pack()

l2 = Label(root, text='Введите айди канала отправки', bg='white')
l2.pack()
channel = Entry(root, bg='white')
channel.pack()

l3 = Label(root, text='Введите заголовок эмбеда', bg='white')
l3.pack()
embed1 = Entry(root, bg='white')
embed1.pack()

l4 = Label(root, text='Введите текст эмбеда', bg='white')
l4.pack()
embed2 = Entry(root, bg='white')
embed2.pack()



title1= Label(root, text='Введите цвета в RGB', bg='white', font=40)
title1.pack()
color1 = Entry(root, bg="white")
color1.pack()
color2 = Entry(root, bg="white")
color2.pack()
color3 = Entry(root, bg="white")
color3.pack()




btn = Button(root, text='Отправить сообщение', bg='white', command=get_botiks)
btn.pack()



#



root.mainloop()