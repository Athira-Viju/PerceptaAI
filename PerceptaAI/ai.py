from tkinter import *
from PIL import Image, ImageTk
import sptotx
import action # type: ignore

# Create the main window
root = Tk()
root.title("Percepta")
root.geometry("550x650")  # Set window size
root.resizable(False, False)  # Fixed window size
root.config(bg="#818180")  # Background color

# Define button commands
def ask():
    user_val=sptotx.speech_to_text()
    bot_val=action.action(user_val)
    text.insert(END,'User-->'+user_val+"\n")
    if bot_val!=None:
        text.insert(END,"BOT<---"+str(bot_val)+"\n")
    if bot_val=='ok sir':
        root.destroy()

def send():
    send=entry.get()
    bot=action.action(send)
    text.insert(END,'User-->'+send+"\n")
    if bot!=None:
        text.insert(END,"BOT<---"+str(bot)+"\n")
    if bot=='ok sir':
        root.destroy()


def delete_txt():
    text.delete('1.0','end')

# Create a LabelFrame
frame = LabelFrame(root, padx=100, pady=7, borderwidth=2, relief="raised")
frame.config(bg="#818180")
frame.grid(row=0, column=0, padx=45, pady=30)

# Create a text label
text_label = Label(frame, text="Its You", font=("Cambria", 15, "bold"), highlightbackground="#f7f4a3", fg="#393838")
text_label.grid(row=0, column=0, padx=14, pady=10)

# Load and resize the image
image_path = r"C:\Users\arath\Pictures\ai.png"  # Update to a valid image path
image = Image.open(image_path)
new_size = (250, 250)
resized_image = image.resize(new_size, Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(resized_image)

# Create an image label
image_label = Label(frame, image=photo)
image_label.grid(row=1, column=0, pady=20)
image_label.image = photo  # Keep a reference to avoid garbage collection

# Create and configure the Text widget
text = Text(root, font=('Courier', 10, 'bold'), bg="#eae2d8")
text.place(x=45, y=400, width=460, height=80)  

# Entry widget
entry = Entry(root, justify=CENTER, bg="#eae2d8")
entry.place(x=65, y=500, width=420, height=35)

# Button1
Button1 = Button(root, text="ASK", bg="#6e6b69", pady=16, padx=40, borderwidth=2, relief=SOLID, command=ask)
Button1.place(x=70, y=575)

# Button2
Button2 = Button(root, text="SEND", bg="#6e6b69", pady=16, padx=40, borderwidth=2, relief=SOLID, command=send)
Button2.place(x=400, y=575)

# Button3
Button3 = Button(root, text="DELETE", bg="#6e6b69", pady=16, padx=40, borderwidth=2, relief=SOLID, command=delete_txt)
Button3.place(x=225, y=575)

# Run the Tkinter event loop
root.mainloop()
