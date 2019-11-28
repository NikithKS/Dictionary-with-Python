import json
import os
import pandas
from tkinter import *
from difflib import get_close_matches
import sqlite3

ddata=json.load(open('data.json'))
flag=0
con=sqlite3.connect('dbms.db')
cur=con.cursor()

def showmean(word,f):
	reset()
	res=getword(word)
	wrd=word+":"
	wlab=Label(wind,text=wrd)
	wlab.pack()
	lab=Text(wind,width=450,bg='#09FFD8',font=('bold',14))
	for i in res:
		lab.insert(END,'->'+i+'\n\n\n')
	lab.pack()
	if(f==0):
		uprecent(word)


def reset(fix=2):
	rescount=0
	for ch in wind.winfo_children():
		if(rescount>=fix):
			ch.destroy()
		else:
			rescount=rescount+1

def placedym(word):
	reset()
	dym=Label(wind,text="Word not found..!\nDid you mean:",font=('bold'))
	dym.pack()
	cls=fndcls(word)
	b1=Button(wind,width=450,text=cls[0],command=lambda:showmean(cls[0],0))
	b2=Button(wind,width=450,text=cls[1],command=lambda:showmean(cls[1],0))
	b3=Button(wind,width=450,text=cls[2],command=lambda:showmean(cls[2],0))
	b1.pack()
	b2.pack()
	b3.pack()

def fndcls(word):
	return get_close_matches(word, ddata.keys(), n=3)




def chkword(w):
	if(w in ddata.keys()):
		return 1
	else:
		return 0


def getword(w):
	return ddata[w]

def uprecent(word):
	global user
	w="'"+ word
	w=w+"'"
	up("word1",w)

	w="'"+ data[2]
	w=w+"'"
	up("word2",w)

	w="'"+ data[3]
	w=w+"'"
	up("word3",w)

def up(wrdp,wrd):
	nameid="'"+uid
	nameid=nameid+"'"
	upc="update data set "+wrdp+"="+wrd+" where name="+nameid
	print(upc)
	cur.execute(upc)
	con.commit()


def takein():
	reset(1)
	top=Frame(wind,bg='grey',width=450,height=75)
	top.pack()
	top.pack_propagate(0)


	com=Label(top,text='Enter word to search:',bg='gray')
	com.pack()


	ent=Entry(top)
	ent.pack()
	src=Button(top,text='Search',command= lambda:getin(ent))
	src.pack(side=RIGHT)
	recent()

def getin(ent):
        word=ent.get()
        reset()
        if(chkword(word)==1):
                showmean(word,0)
        else:
                placedym(word)



def recent():
	b1=Button(wind,width=450,text=data[2],command=lambda:showmean(data[2],1))
	b2=Button(wind,width=450,text=data[3],command=lambda:showmean(data[3],1))
	b3=Button(wind,width=450,text=data[4],command=lambda:showmean(data[4],1))
	b1.pack()
	b2.pack()
	b3.pack()

def niks():
	from tkinter import messagebox
	messagebox.showinfo("__","Built by:NiKS")
	os.execl(sys.executable, sys.executable, *sys.argv)

def login():
	global uid,data
	uid=ident.get()
	passw=passent.get()
	cmd="select * from data where name='"+uid+"'"
	cur.execute(cmd)
	op=cur.fetchall()
	op=str(op).split("'")
	data=[]
	for i in range(len(op)):
        	if(i%2!=0):
                	data.append(op[i])
	if(data[1]==passw):
		takein()
	else:
		wrong()



def wrong():
	fail=Label(text='Wrong ID or password',fg='red')
	fail.pack(side=TOP)

uid=""
wind=Tk()
flag=0
wind.title('DBMS')
wind.geometry('450x450')

cred=Button(text='Dictionary',bg='#000029',fg='white',command=lambda:niks())
cred.pack(side=TOP)

line1=Frame(bg='grey',width=450,height=15)
line1.pack()
line1.pack_propagate(0)

id=Label(text='Username:',font=('bold',12))
id.pack(anchor=NW)

ident=Entry()
ident.pack(side=TOP)

passw=Label(text="Password:",font=('bold',12))
passw.pack(anchor=NW)

passent=Entry(show='*')
passent.pack(side=TOP)

log=Button(text='LOG IN',command=lambda:login())
log.pack(side=TOP)


wind.mainloop()
