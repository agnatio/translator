from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator



def label_change():
    """
    This function is used to change the label text
    """
    src_lang = src_lang_combo.get()
    tgt_lang = tgt_lang_combo.get()
    src_lang_label.config(text=src_lang)
    tgt_lang_label.config(text=tgt_lang)
    root.after(1000, label_change)

def translate_now():
    """
    This function is used to translate the text"""
    try:
        src_text = src_text_box.get(1.0, END)
        src_lang = src_lang_combo.get()
        tgt_lang = tgt_lang_combo.get()
        if src_text:
            translator = GoogleTranslator(source=language[src_lang], target=language[tgt_lang])
            translated_text = translator.translate(src_text)
            tgt_text_box.delete(1.0, END)
            tgt_text_box.insert(1.0, translated_text)
    except Exception as e:
        messagebox.showerror("Error", e)
        print(e)


def change_languages():
    """
    This function is used to change the languages
    """
    src_lang = src_lang_combo.get()
    tgt_lang = tgt_lang_combo.get()
    src_lang_combo.set(tgt_lang)
    tgt_lang_combo.set(src_lang)

if __name__ == "__main__":

    root = Tk()
    root.title("Translator")
    root.geometry("1080x400")
    root.configure(bg="lightblue")

    arrow_image = PhotoImage(file="arrows1.png")
    image_label = Label(root, image=arrow_image, bg="lightblue")
    
    change_button = Button(root, image=arrow_image, compound="center", font=("Helvetica", 20), command=change_languages, fg="lightblue", borderwidth=0, activebackground="lightblue", relief="flat", bg="lightblue")
    change_button.place(x=485, y=130)


    language = GoogleTranslator().get_supported_languages(as_dict=True)
    languagesV = list(language.keys())

    src_lang_combo = ttk.Combobox(root, values=languagesV, font=("Roboto", 14), state='r')
    src_lang_combo.place(x=110, y=20)
    src_lang_combo.set("english")

    src_lang_label = Label(root, text="english", font=("segoe", 30, "bold"), width=15, bd=5, relief=GROOVE, bg="white")
    src_lang_label.place(x=15, y=50)

    src_text_frame = Frame(root, bd=5, bg="black")
    src_text_frame.place(x=10, y=118, width=440, height=210)

    src_text_box = Text(src_text_frame, font=("Robote", 20), bg="white", relief=GROOVE, wrap=WORD)
    src_text_box.place(x=0, y=0, width=430, height=200)

    src_text_scrollbar = Scrollbar(src_text_frame)
    src_text_scrollbar.pack(side=RIGHT, fill=Y)

    src_text_scrollbar.config(command=src_text_box.yview)
    src_text_box.config(yscrollcommand=src_text_scrollbar.set)

    tgt_lang_combo = ttk.Combobox(root, values=languagesV, font=("Roboto", 14), state='r')
    tgt_lang_combo.place(x=730, y=20)
    tgt_lang_combo.set("select language")

    tgt_lang_label = Label(root, text="select language", font=("segoe", 30, "bold"), width=15, bd=5, relief=GROOVE, bg="white")
    tgt_lang_label.place(x=620, y=50)

    tgt_text_frame = Frame(root, bd=5, bg="black")
    tgt_text_frame.place(x=620, y=118, width=440, height=210)

    tgt_text_box = Text(tgt_text_frame, font=("Robote", 20), bg="white", relief=GROOVE, wrap=WORD)
    tgt_text_box.place(x=0, y=0, width=430, height=200)

    tgt_text_scrollbar = Scrollbar(tgt_text_frame)
    tgt_text_scrollbar.pack(side=RIGHT, fill=Y)

    tgt_text_scrollbar.config(command=tgt_text_box.yview)
    tgt_text_box.config(yscrollcommand=tgt_text_scrollbar.set)

    # translate button
    translate_button = Button(root, text="Translate", font=("Roboto", 14), bg="white", relief=GROOVE, bd=5, command=translate_now)
    translate_button.place(x=475, y=250)

    label_change()

    root.mainloop()