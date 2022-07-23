from re import sub
from decimal import Decimal
from bs4 import BeautifulSoup
import requests
import smtplib
from email.message import EmailMessage
from datetime import datetime
from tkinter import *
from tkinter import messagebox
from urllib.parse import urlparse

# THIS FUNCTION EXTRACTS THE DOMAIN NAME FROM URL AND CHECKS WHETHER IT IS 'WWW.AMAZON.IN' OR NOT


def URL_CHECK(url):
    website = urlparse(url).netloc
    return website == "www.amazon.in"


def is_cheap(price, target):
    return price <= target


def get_details():
    receiver_email = EMAIL_ENTRY.get()
    URL = URL_ENTRY.get()
    budget = (BUDGET_ENTRY.get())
    if not URL_CHECK(URL):
        messagebox.showinfo(title="INVALID URL", message="PLEASE ENTER A PRODUCT LINK FROM WWW.AMAZON.IN")
        # CLEARING USER INPUTS
        EMAIL_ENTRY.delete(0, END)
        BUDGET_ENTRY.delete(0, END)
        URL_ENTRY.delete(0, END)
    if len(receiver_email) == 0 or len(URL) == 0 or len(budget) == 0:
        messagebox.showinfo(title="INVALID INPUT", message="YOU HAVE NOT FILLED ALL DETAILS CORRECTLY")
        # CLEARING USER INPUTS
        EMAIL_ENTRY.delete(0, END)
        BUDGET_ENTRY.delete(0, END)
        URL_ENTRY.delete(0, END)
    else:
        target_price = float(budget)
    # HERE WE NEED TO PASS ADDITIONAL INFORMATION TO GET HTML OF THE SITE

    response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                                                        " (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
                                          "Accept-Language": "en-US,en;q=0.9"})
    # SCRAPING USING BEAUTIFUL SOUP
    soup = BeautifulSoup(response.text, "html.parser")
    # GETTING HOLD OF PRICE

    # IF IT IS PRIME DAY THEN CODE HAS TO BE CHANGED TO GET CORRECT VALUE SINCE WEBSITE LAYOUT CHANGES
    price = soup.find_all(name="span", class_="a-offscreen")
    item_price = price[1].getText()
    value = Decimal(sub(r'[^\d.]', '', item_price))  # STACK OVERFLOW TO CONVERT PRICE TO FLOAT

    # GETTING CURRENT TIME
    time_now = datetime.now()

    # STRUCTURE OF EMAIL

    message = EmailMessage()  # creating an OBJECT of EmailMessage Class
    if is_cheap(value, target_price):
        message["Subject"] = "PRICE OF ITEM HAS DROPPED"
        message.set_content(
            f"This message is sent via Python Code.. The item listed has price of ₹ {value} as of {time_now} on "
            f"Amazon, OLD PRICE WAS ₹ {value}  \n\n HURRY!!!\n\n\nLink : {URL}")
    else:
        message["Subject"] = f"PRICE OF ITEM HAS NOT dropped to ₹ {target_price}"
        message.set_content(
            f"This Message is sent via Python Code.. The Price is ₹{value} as of {time_now} and has not"
            f" dropped below ₹ {target_price} \n\n\n Link : {URL}")

    message["to"] = receiver_email
    message["from"] = email

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.send_message(message)

    messagebox.showinfo(title="SUCCESS!", message="MAIL SENT SUCCESSFULLY!")
    # CLEARING USER INPUTS
    EMAIL_ENTRY.delete(0, END)
    BUDGET_ENTRY.delete(0, END)
    URL_ENTRY.delete(0, END)


# CREATING WINDOW
window = Tk()
window.title("AMAZON PRICE TRACKER BOT")
canvas = Canvas(height=230, width=230)
window.config(padx=50, pady=50)
amazon_logo = PhotoImage(file="Amazon_icon.png")
canvas.create_image(115, 115, image=amazon_logo)
canvas.grid(row=0, column=1)

# CREATING LABELS FOR WINDOW


URL_LABEL = Label(text="ENTER PRODUCT URL : ")
URL_LABEL.grid(row=1, column=0)
BUDGET_LABEL = Label(text="ENTER YOUR BUDGET : ")
BUDGET_LABEL.grid(row=2, column=0)
EMAIL_LABEL = Label(text="ENTER YOUR EMAIL ID : ")
EMAIL_LABEL.grid(row=3, column=0)
URL_LABEL.focus()

# CREATING ENTRY FOR EACH LABEL
URL_ENTRY = Entry(width=20)
URL_ENTRY.grid(row=1, column=1)
BUDGET_ENTRY = Entry(width=20)
BUDGET_ENTRY.grid(row=2, column=1)
EMAIL_ENTRY = Entry(width=20)
EMAIL_ENTRY.grid(row=3, column=1)
# CREATING BUTTON

button = Button(text="CHECK", command=get_details)
button.grid(row=4, column=1)
# END OF TKINTER GUI CODE
# EMAIL AND PASSWORD FOR BOT

email = "botmanprofessional@gmail.com"
password = "egxisuczyabtqyee"

window.mainloop()
