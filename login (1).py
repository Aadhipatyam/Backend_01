from tkinter import *
from PIL import Image, ImageTk

# Create the main window
login_window = Tk()
login_window.geometry("990x660+50+50")
login_window.resizable(False, False)
login_window.title("Login Page")

# Background image
bg_raw = Image.open("bg.jpg")
bg_resized = bg_raw.resize((990, 660), Image.Resampling.LANCZOS)
bg_image = ImageTk.PhotoImage(bg_resized)

bg_label = Label(login_window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Unified background color for the panel (approximate to match bg.jpg panel)
bg_color = "#dee8dd"

# Background frame to hold widgets (overlaying soft panel only)
panel_frame = Frame(login_window, bg=bg_color, width=400, height=500)
panel_frame.place(x=300, y=80)

# Heading
heading = Label(panel_frame, text="CREATE AN ACCOUNT", font=("Segoe UI", 24, "bold"), bg=bg_color, fg="firebrick1")
heading.place(x=30, y=10)

# Email Entry
email_entry = Entry(panel_frame, width=30, font=("Microsoft YaHei UI Light", 11), fg="firebrick1", bg=bg_color, border=0)
email_entry.place(x=20, y=70)
email_entry.insert(0, "Email")
email_entry.bind("<FocusIn>", lambda e: email_entry.delete(0, END) if email_entry.get() == "Email" else None)

frame0 = Frame(panel_frame, width=280, height=2, bg="firebrick1")
frame0.place(x=20, y=92)

# Username Entry
username_entry = Entry(panel_frame, width=30, font=("Microsoft YaHei UI Light", 11), fg="firebrick1", bg=bg_color, border=0)
username_entry.place(x=20, y=110)
username_entry.insert(0, "Username")
username_entry.bind("<FocusIn>", lambda e: username_entry.delete(0, END) if username_entry.get() == "Username" else None)

frame1 = Frame(panel_frame, width=280, height=2, bg="firebrick1")
frame1.place(x=20, y=132)

# Password Entry
password_entry = Entry(panel_frame, width=30, font=("Poppins", 11), fg="firebrick1", bg=bg_color, border=0)
password_entry.place(x=20, y=150)
password_entry.insert(0, "Password")
password_entry.bind("<FocusIn>", lambda e: password_entry.delete(0, END) if password_entry.get() == "Password" else None)

frame2 = Frame(panel_frame, width=280, height=2, bg="firebrick1")
frame2.place(x=20, y=172)

# Confirm Password Entry
confirm_entry = Entry(panel_frame, width=30, font=("Poppins", 11), fg="firebrick1", bg=bg_color, border=0)
confirm_entry.place(x=20, y=190)
confirm_entry.insert(0, "Confirm Password")
confirm_entry.bind("<FocusIn>", lambda e: confirm_entry.delete(0, END) if confirm_entry.get() == "Confirm Password" else None)

frame3 = Frame(panel_frame, width=280, height=2, bg="firebrick1")
frame3.place(x=20, y=212)

# Eye button for Password (resized)
eye_raw = Image.open("eye.png").resize((15, 15), Image.Resampling.LANCZOS)
eye_img = ImageTk.PhotoImage(eye_raw)
eye_button = Button(panel_frame, image=eye_img, border=0, bg=bg_color, activebackground=bg_color, cursor="hand2")
eye_button.place(x=280, y=148)

# Terms Checkbox
terms = Checkbutton(panel_frame, text="I agree to the Terms & Conditions", font=("Open Sans", 9), bg=bg_color, fg="firebrick1", activebackground=bg_color, activeforeground="firebrick1")
terms.place(x=20, y=230)

# Signup Button
signup_button = Button(panel_frame, text="Signup", font=("Open Sans", 14, "bold"), bg="firebrick1", fg="white",
                      activeforeground="white", activebackground="firebrick1", cursor="hand2", width=25, border=0)
signup_button.place(x=20, y=270)

# Already have account text
already_label = Label(panel_frame, text="Don't have an account?", font=("Open Sans", 9), bg=bg_color, fg="firebrick1")
already_label.place(x=20, y=310)

login_link = Button(panel_frame, text="Log in", font=("Open Sans", 9, "bold", "underline"), bg=bg_color, fg="blue", border=0, cursor="hand2")
login_link.place(x=160, y=310)

# Social Media Icons (resized)
fb_resized = Image.open("fb.png").resize((20, 20), Image.Resampling.LANCZOS)
facebook_logo = ImageTk.PhotoImage(fb_resized)
fb_label = Label(panel_frame, image=facebook_logo, bg=bg_color)
fb_label.place(x=70, y=350)

gg_resized = Image.open("gg.png").resize((20, 20), Image.Resampling.LANCZOS)
google_logo = ImageTk.PhotoImage(gg_resized)
google_label = Label(panel_frame, image=google_logo, bg=bg_color)
google_label.place(x=110, y=350)
login_window.mainloop()
