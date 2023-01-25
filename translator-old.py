from tkinter import *
from tkinter import ttk, messagebox

from deep_translator import GoogleTranslator

root = Tk()
root.title("Translator")
root.geometry("1080x400")
root.configure(bg="lightblue")


def label_change():
    """
    This function is used to change the label text"""
    c = combo1.get()
    c1 = combo2.get()
    label1.config(text=c)
    label2.config(text=c1)
    root.after(1000, label_change)

def translate_now():

    global language
    try:
        src_text = text1.get(1.0, END)
        src_lang = combo1.get()
        tgt_lang = combo2.get()
        if src_text:
            translator = GoogleTranslator(source=language[src_lang], target=language[tgt_lang])
            source_language = language[src_lang]
            target_language = language[tgt_lang]
            translated_text = translator.translate(src_text)
            text2.delete(1.0, END)
            text2.insert(1.0, translated_text)
    except Exception as e:
        messagebox.showerror("Error", e)
        print(e)

                

arrow_image = PhotoImage(file="arrows1.png")
image_label = Label(root, image=arrow_image, bg="lightblue")
image_label.place(x=480, y=130)

language = GoogleTranslator().get_supported_languages(as_dict=True)
languagesV = list(language.keys())

lang1 = language.keys()

combo1 = ttk.Combobox(root, values=languagesV, font=("Roboto", 14), state='r')
combo1.place(x=110, y=20)
combo1.set("english")

label1 = Label(root, text="english", font=("segoe", 30, "bold"), width=15, bd=5, relief=GROOVE, bg="white")
label1.place(x=15, y=50)

f=Frame(root, bd=5, bg="black")
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font=("Robote", 20), bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side=RIGHT, fill=Y)

scrollbar1.config(command=text1.yview)
text1.config(yscrollcommand=scrollbar1.set)

combo2 = ttk.Combobox(root, values=languagesV, font=("Roboto", 14), state='r')
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text="SELECT LANGUAGE", font=("segoe", 30, "bold"), width=15, bd=5, relief=GROOVE, bg="white")
label2.place(x=620, y=50)

f1=Frame(root, bd=5, bg="black")
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font=("Robote", 20), bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side=RIGHT, fill=Y)

scrollbar2.config(command=text2.yview)
text2.config(yscrollcommand=scrollbar2.set)

# translate button
translate = Button(root, text="Translate", font=("Roboto", 14), bg="white", relief=GROOVE, bd=5, command=translate_now)
translate.place(x=480, y=250)

label_change()


root.mainloop()

# from deep_translator import GoogleTranslator
# output = GoogleTranslator(source='auto', target='it')

# output = output.translate("keep it up, you are awesome") 
# print(output)

# languages = GoogleTranslator().get_supported_languages(as_dict=True)

# src_lang = combo1.get()
# tgt_lang = combo2.get()

# print(src_lang, tgt_lang)


# print(languages)