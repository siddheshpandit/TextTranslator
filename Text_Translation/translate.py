#importing necessary libraries
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from textblob import TextBlob

root=Tk()
root.geometry('500x400')
root.title("Translator")
root.configure()
lan_dict={'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

#Function for text translation
def text_translation():
    word=TextBlob(varname1.get())
    lan=word.detect_language()
    lang_todict= languages.get()
    lang_to= lan_dict[lang_todict]
    word=word.translate(from_lang=lan,to=lang_to)
    varname2.set(word)

#Function to exit translator
def exit():
    rr=messagebox.askyesnocancel('Notification','Do you want to exit')
    if rr==True:
        root.destroy()


languages=StringVar()
# Dropdown for languages
font_box=Combobox(root,width=10,textvariable=languages,state='readonly')
font_box['values']=[e for e in lan_dict.keys()]
font_box.current(37)
font_box.place(x=400,y=0)
###########
varname1=StringVar()

entry1=Entry(root,width=30,textvariable=varname1,font=('times',15,'italic bold'),relief='ridge')
entry1.place(x=140,y=40)
#Label for Entering word
label1=Label(root,text="Enter Words :",font=('times',15,'italic bold'))
label1.place(x=5,y=40)

varname2=StringVar()
entry2=Entry(root,width=30,textvariable=varname2,font=('times',15,'italic bold'),relief='ridge')
entry2.place(x=140,y=80)

# Label for Displaying meaning
label2=Label(root,text="Translated :",font=('times',15,'italic bold'))
label2.place(x=5,y=80)

#button for Translation
btn1=Button(root,text='Translate',bd=10,bg='yellow',activebackground='green',width=7,font=('times',15,'italic bold'),command=text_translation)
btn1.place(x=70,y=170)

#button for exit
btn2=Button(root,text='Exit',bd=10,bg='yellow',activebackground='red',width=7,font=('times',15,'italic bold'),command=exit)
btn2.place(x=240,y=170)
root.mainloop()