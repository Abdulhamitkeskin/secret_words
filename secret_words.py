import tkinter
from PIL import Image, ImageTk
from cryptography.fernet import Fernet
from tkinter import messagebox

window = tkinter.Tk()
window.title("Secret File Program")
window.minsize(450, 600)
text_list=[]
password_list = []
key = Fernet.generate_key()
fernet = Fernet(key)
password_text=None

def process_function():
    filename = entry_filename.get()
    password = entry_password.get()
    text = secret_text.get("1.0", tkinter.END)
    global password_text

    global text_list
    if not filename or not password or not text:
        messagebox.showerror("Error", "Please enter all data!")
    else:
        with open("important!!!.txt", mode="a") as appendfile:


            appendfile.write(entry_filename.get()+"\n")


            password_list.append(entry_password.get())


            entry_filename.delete(0, tkinter.END)

            # Metni şifreleme
            secret = secret_text.get("1.0", tkinter.END)
            secret_text.delete("1.0", tkinter.END)
            password_text = fernet.encrypt(secret.encode())

            appendfile.write(str(password_text)+"\n")
            text_list.append(password_text)

            entry_password.delete(0, tkinter.END)
            messagebox.showinfo("Information", "Registered successfully")


def solution():
    global password_text
    global text_list

    if not password_list:
        messagebox.showerror("Error", "No password text available!")

    else:
        password = entry_password.get()
        text = secret_text.get("1.0", tkinter.END).strip()
        found=False

        if not password or not text:
            messagebox.showerror("Error", "Please enter password and text!")
        else:
            global password_text

            for i in range(len(password_list)):

                if password==password_list[i]  and str(text)==str(text_list[i]):

                    secret_text.delete("1.0", tkinter.END)
                    entry_password.delete(0, tkinter.END)

                    solved_text = fernet.decrypt(text_list[i])
                    decode=solved_text.decode()

                    secret_text.insert(tkinter.END,decode)
                    found=True

            else:
                if found==False:
                    messagebox.showerror("Eror","Password or text error")


# Image
image_file = "photo.jpg"
img = Image.open(image_file)
img = img.resize((200, 150))

photo = ImageTk.PhotoImage(img)

filelabel = tkinter.Label(window, image=photo)
filelabel.image = photo

# entry
entry_filename = tkinter.Entry(font=15)
entry_password = tkinter.Entry(font=15)

# label
label_filename = tkinter.Label(text="Enter your title")
label_textname = tkinter.Label(text="Enter your secret")
label_password = tkinter.Label(text="Enter your password")

# text
secret_text = tkinter.Text(width=30, height=15)

# button
save_button = tkinter.Button(text="Save", command=process_function)
decrypt_button = tkinter.Button(text="Decrypt", command=solution)

#pack

filelabel.pack()
label_filename.pack()
entry_filename.pack()
label_textname.pack()
secret_text.pack()
label_password.pack()
entry_password.pack()
save_button.pack()
decrypt_button.pack()

window.mainloop()

