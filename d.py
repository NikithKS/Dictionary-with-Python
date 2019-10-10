import json
from tkinter import *
from difflib import get_close_matches
data=json.load(open('data.json'))
flag=0

def getin():
	word=ent.get()
	reset()
	if(chkword(word)==1):
		showmean(word,0)
	else:
		placedym(word)

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


def reset():
	rescount=0
	for ch in wind.winfo_children():
		if(rescount>1):
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
	return get_close_matches(word, data.keys(), n=3)




def chkword(w):
	if(w in data.keys()):
		return 1
	else:
		return 0


def getword(w):
	return data[w]

def uprecent(word):
	nl=[]
	d=open('recent.txt','r')
	l=d.readlines()
	l=l[0].split()
	nl.append(word)
	nl.append(l[0])
	nl.append(l[1])
	with open('recent.txt', 'w') as f:
	        for item in nl:
        	        f.write("%s " % item)




def recent():
	d=open('recent.txt','r')
	l=d.readlines()
	l=l[0].split()
	rlab=Label(text='Recent searches:')
	rlab.pack()
	b1=Button(wind,width=450,text=l[0],command=lambda:showmean(l[0],1))
	b2=Button(wind,width=450,text=l[1],command=lambda:showmean(l[1],1))
	b3=Button(wind,width=450,text=l[2],command=lambda:showmean(l[2],1))
	b1.pack()
	b2.pack()
	b3.pack()

def niks():
	from tkinter import messagebox
	messagebox.showinfo("__","Built by:NiKS")



wind=Tk()
flag=0
wind.title('DBMS')
wind.geometry('450x450')

cred=Button(text='Dictionary',bg='#000029',fg='white',command=lambda:niks())
cred.pack(side=TOP)


top=Frame(wind,bg='grey',width=450,height=75)
top.pack()
top.pack_propagate(0)

com=Label(top,text='Enter word to search:',bg='gray')
com.pack()

ent=Entry(top)
ent.pack()
src=Button(top,text='Search',command= lambda:getin())
src.pack(side=RIGHT)

recent()

wind.mainloop()
