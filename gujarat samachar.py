import requests
import urllib.request
import os
import datetime
import re
from bs4 import BeautifulSoup
from PIL import Image
from PyPDF2 import  PdfReader, PdfMerger

# Creating Folders
dir_names = ['images/', 'PDFs/']
for name in dir_names:
    try:
        os.mkdir(name)
    except:
        FileExistsError
        print("Foler already exists")

# Scraping Page Links
html = "https://epaper.gujaratsamachar.com/ahmedabad/" + datetime.datetime.today().strftime('%d-%m-%Y') + "/1"
r = requests.get(html)
print("Website is connected")
soup = BeautifulSoup(r.content, 'html.parser')
pages = soup.find("ul", {"class": "nav nav-tabs nav-dots border-bottom-0"})
listofPage = []
for page in pages.find_all("a", {"class":"anchor_click"}, href = True):
    listofPage.append(page['href'])

# Downloading Images
def download_image(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

# Scraping Image Links
img = []
for pages in listofPage:
    p = BeautifulSoup(requests.get(pages).content, 'html.parser')
    s = p.find("img", {"class":"w-100 sky epaper_page"})
    img.append(s.get('src'))
print("Page links were scrapped!")

# Downloading Images
for i, url in enumerate(img):
    # construct the file name for the current image
    file_name = f"{i+1:02d}"
    # download the image using the current file name
    download_image(url, file_path="images/", file_name=file_name)
print("All pages downloaded as images.")

# Converting Images to PDF
image_list = os.listdir("images/") # list of images in images folder
for image in image_list:
    fimg = Image.open("images/" + image)
    a4img = Image.new("RGB", (2800, 3974), (255, 255, 255))
    a4img.paste(fimg, fimg.getbbox())
    a4img.save("PDFs/" + image + ".pdf", "PDF", quality = 70)
print("All images are converted to PDF format.")

# Merging PDFs
pdfs = os.listdir("PDFs/")
pdfs.sort(key=lambda f: int(re.sub('\D', '', f)))
merger = PdfMerger()
for file in pdfs:
    merger.append(PdfReader("PDFs/" + file, 'rb'))
merger.write("Gujarat Samachar_" + datetime.datetime.today().strftime('%d-%m-%Y') + ".pdf")
print("All PDFs are merged into one PDF file.")

# Deleting all Images
for image in image_list:
    os.remove("images/" + image)
print("Deleted All Images.")
# Deleting all Single PDFs
for pdf in pdfs:
    os.remove("PDFs/" + pdf)
print("Deleted All Single PDFs")