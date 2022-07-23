# AMAZON_INDIA_PRICE_TRACKER
The Project uses BeautifulSoup to scrape price of an item in  www.amazon.in , the URL taken as User Input ,and checks against User's budget (User Input)
and sends an email to User's Email ID
# USER INPUTS :
Item URL
Budget
User Email ID
# WEB SCRAPING USING BEAUTIFUL SOUP
The Project employs BeautifulSoup to Scrape the price of an item whose URL is provided as User Input. After getting the price , it checks it against User's budget.
# SMTPLIB and email.message
After checking whether the price of item is above or below budget , an email is sent using smtplib and Email Message generated with the help of email.message
# GUI generated via Tkinter
Window generated using Tk class and amazon logo added to window with the help of Canvas class.
# messagebox
messagebox imported from Tkinter to generate success or failure messages depending on User Inputs.
# urllib.parse 
urllib.parse used to parse the URL and extract domain name and check if URL is from www.amazon.in
The python file AmazonPriceTracker.py as well as the .png image file is uploaded. Download them and keep them in the same folder. 
# PREVIEW
![Amazon](https://user-images.githubusercontent.com/109027110/180621367-568d2ef2-6c9e-417e-b5ca-92bd04f9d45a.jpg)
