import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = "https://www.amazon.com/s/ref=nb_sb_ss_c_1_15?url=search-alias%3Daps&field-keywords=tumeric+supreme+gaia&sprefix=tumeric+supreme%2Caps%2C154&crid=11381C0PRK8IO"

#makes connection and grabs the webpage
uClient = uReq(my_url)
#offloads content into a variable
page_html = uClient.read()
#clsoes connection
uClient.close()
#html parsing
page_soup = soup(page_html, 'html.parser')

# grabs each product
containers = page_soup.findAll("div",{"class":"s-item-container"})

for container in containers:
    brand = container.findAll("span",{"class":"a-size-small a-color-secondary"})[1].text
    title_container = container.div.div.div.div.div.a.img["alt"]
    product_name = title_container
    price = container.findAll("span",{"class":"a-offscreen"})[0].text

    print("brand: " + brand)
    print("product_name: " + product_name)
    print("price: " + price)
