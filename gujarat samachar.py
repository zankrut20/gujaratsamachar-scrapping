# required modules
import requests
import urllib.request
import os
import datetime
import re
from bs4 import BeautifulSoup
from PIL import Image
from PyPDF2 import  PdfFileReader, PdfFileMerger

# auto generation of website link
html = "https://epaper.gujaratsamachar.com/ahmedabad/" + datetime.datetime.today().strftime('%d-%m-%Y') + "/1"
r = requests.get(html)
print("Website is connected")
soup = BeautifulSoup(r.content, 'html.parser')

# find pages & their respective download links
pages = soup.find("ul", {"class": "nav nav-tabs nav-dots border-bottom-0"})
listofPage = []
for page in pages.find_all("a", {"class":"anchor_click"}, href = True):
    listofPage.append(page['href'])

# issue pages are in .jpef format
# download all pages in .jpeg format
# download function
def download_image(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

print("Downloading pages...")
img = []
for pages in listofPage:
    p = BeautifulSoup(requests.get(pages).content, 'html.parser')
    s = p.find("img", {"class":"w-100 sky epaper_page"})
    img.append(s.get('src'))

for url in img:
    download_image(url, file_path = "images/", file_name = url.split("/")[4].split("-")[3].split(".")[0])
print("All pages downloaded as images.")
# convert all pages to pdf
# current_dir = os.getcwd() # current directory
image_list = os.listdir("images/") # list of images in images folder
image_list.sort(key=lambda f: int(re.sub('\D', '', f))) # sort images in ascending order

# convert images to pdf
for image in image_list:
    fimg = Image.open("images/" + image)
    a4img = Image.new("RGB", (2800, 3974), (255, 255, 255))
    a4img.paste(fimg, fimg.getbbox())
    a4img.save("PDFs/" + image + ".pdf", "PDF", quality = 70)
print("All images are converted to PDF format.")

# merge all pdfs into one pdf
pdfs = os.listdir("PDFs/")
pdfs.sort(key=lambda f: int(re.sub('\D', '', f)))
merger = PdfFileMerger()
for file in pdfs:
    merger.append(PdfFileReader("PDFs/" + file, 'rb'))
merger.write("Gujarat Samachar_" + datetime.datetime.today().strftime('%d-%m-%Y') + ".pdf")