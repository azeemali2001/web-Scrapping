import requests                     #request - obtain information from a link in the form of HTML
from bs4 import BeautifulSoup       #beautifulsoup - parse that information
import time
import csv
import send_email
from datetime import date

today = str(date.today()) + ".csv"

urls = ["https://finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch","https://finance.yahoo.com/quote/FB2A.BE?p=FB2A.BE&.tsrc=fin-srch","https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch","https://finance.yahoo.com/quote/NFLX.NE?p=NFLX.NE&.tsrc=fin-srch","https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch","https://finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch"]

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

csv_file = open(today,"w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Stock Name','Current Price','Previous Close','Open','Bid','Ask','Day\'s Range','52 Week Range','Volume','Avg. Volume','Market Cap','Beta (5Y Monthly)','PE Ratio (TTM)','EPS (TTM)','Earnings Date','Forward Dividend & Yield','Ex-Dividend Date','1y Target Est'])



for url in urls:
    stock = []
    html_page = requests.get(url,headers=header)
    soup = BeautifulSoup(html_page.content,"lxml")

#----------------------------------------------------------------------------------------------------------------------
    header_info = soup.find_all("div",id="quote-header-info")[0]
    stock_title = header_info.find("h1").get_text()
    current_price = header_info.find("div",class_="D(ib) Mend(20px)").find("fin-streamer").get_text()
    stock.append(stock_title)
    stock.append(current_price)
#----------------------------------------------------------------------------------------------------------------------
    table_info_1 = soup.find_all("table",class_="W(100%)")[0]
    for i in range(0,8):
        value = table_info_1.find_all("td",class_="Ta(end) Fw(600) Lh(14px)")[i].get_text()
        stock.append(value)
#----------------------------------------------------------------------------------------------------------------------

    table_info_2 = soup.find_all("table",class_="W(100%) M(0) Bdcl(c)")[0]
    for i in range(0,8):
        value = table_info_2.find_all("td",class_="Ta(end) Fw(600) Lh(14px)")[i].get_text()
        stock.append(value)

    csv_writer.writerow(stock)
    time.sleep(5)    


csv_file.close()
send_email.send(file_name=today)



