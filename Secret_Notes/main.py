import base64
import binascii
import tkinter
from tkinter import *
from tkinter import messagebox

from cryptography.fernet import Fernet

FONT = ('Arial', 11, 'bold')


# Tkinter penceresini oluşturma
window = Tk()
window.title("Secret Notes")
window.geometry("500x750")

# görsel ekleme işlemi
photo = PhotoImage(file="cryptography.png")
photo_label = Label(image=photo)
photo_label.pack(pady=30)

# başlık
enter_title_label = Label(text="Enter your title", font=FONT)
enter_title_label.pack()
enter_title_entry = Entry(width=30, font=FONT)
enter_title_entry.focus()
enter_title_entry.pack(pady=10)

# Gizli metin girişi için metin kutusu
enter_secret_label = Label(text="Enter your secret", font=FONT)
enter_secret_label.pack(pady=15)
enter_secret_text = Text(width=40, height=20)
enter_secret_text.pack()

# Anahtar girişi için giriş alanı
enter_secret_label = Label(text="Enter master key", font=FONT)
enter_secret_label.pack(pady=10)
enter_key_entry = Entry(width=30, font=FONT)
enter_key_entry.pack()


# Şifreleme işlevi
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# Şifre çözme işlevi
def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


# Notları dosyaya yazma işlevi
def write_to_txt(title, message):
    try:
        with open("mysecret.txt", "a") as file:
            file.write("\n"+title + "\n" + message + "\n")
    except FileNotFoundError:
        with open("mysecret.txt","w") as file:
            file.write(f"\n{title}\n{message}\n")
    finally:
        enter_title_entry.delete(0, END)
        enter_secret_text.delete("1.0", END)
        enter_key_entry.delete(0, END)


# "Save & Encrypt" butonuna tıklama işlevi
def save_clicked():
    title = enter_title_entry.get()
    message = enter_secret_text.get("1.0", "end-1c")
    key = enter_key_entry.get()

    if len(title) == 0 or len(message) == 0 or len(key) == 0:
        messagebox.showinfo(title="Error!", message="Please enter all info.")
    else:
        message_encrypted = encode(key, message)
        write_to_txt(title, message_encrypted)


# "Save & Encrypt" düğmesi oluşturma ve işlevi bağlama
save_button = Button(text="Save & Encrypt", command=save_clicked, font=FONT, fg="white", background="green")
save_button.pack(pady=10)


# Şifre çözme işlevi
def decrypt_clicked():
    message_encrypted = enter_secret_text.get("1.0", END)
    key = enter_key_entry.get()

    if len(message_encrypted) == 0 or len(key) == 0:
        messagebox.showinfo(title="Error!", message="Please enter all information.")
    else:
        try:
            decrypted_message = decode(key, message_encrypted)
            enter_secret_text.delete("1.0", END)
            enter_secret_text.insert("1.0", decrypted_message)
        except binascii.Error:
            messagebox.showinfo(title="Error!", message="Please make sure of encrypted info.")


# "Decrypt" butonu oluşturma ve işlevi bağlama
decrypt_button = Button(text="Decrypt", command=decrypt_clicked,font=FONT,fg="white",background="red")
decrypt_button.pack()


window.mainloop()