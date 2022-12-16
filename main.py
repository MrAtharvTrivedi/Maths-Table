# Author ---> Atharv Trivedi

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Multiplication Table")
root.resizable(0,0)
root.geometry("300x200")

clicks = 0

def table_maker():
    global output_frame
    global output_label
    global clicks
    clicks = clicks + 1

    if clicks > 1 and output_frame.winfo_exists():
        output_frame.destroy()
    output_frame = customtkinter.CTkFrame(master=root, fg_color="#1a1b1b")
    output_frame.pack()
    if user_input.get().isdigit():
        root.geometry("300x500")
        for i in range(1, 11):            
            output_label = customtkinter.CTkLabel(master=output_frame, text_color="white", text_font=("Roboto",18), text=f"{user_input.get()} x {i} = {int(user_input.get()) * i}")
            output_label.pack(fill="both")
    else:
        root.geometry("300x200")
        output_label = customtkinter.CTkLabel(master=output_frame, text_color="red", text="Kindly Enter a number")
        output_label.pack()

user_input = customtkinter.CTkEntry(master=root, placeholder_text="Enter the number", width=150)
user_input.pack(ipadx=25, ipady=5, padx=10, pady=(30,10))

btn = customtkinter.CTkButton(master=root, text="SUBMIT", bg="black", text_color="white", command=table_maker, width=150)
btn.pack(ipadx=25, ipady=5, padx=10, pady=(10,30))

root.mainloop()
