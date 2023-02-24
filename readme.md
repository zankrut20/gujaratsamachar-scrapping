# NEWSPAPER (Gujarat Samachar) SCRAPING PROJECT 
## Objective:
The objective of this project is to scrape pages which are available in image format and merge them into a single PDF file.

## Problem:
The website does not provide the option to download the entire newspaper as a single PDF file, unlike other Gujarati language newspaper websites. To download the entire newspaper, one has to download each page separately, wait for the redirect and then download the next page, and so on. This can be a tedious and time-consuming process.

## Approach:
To overcome the problem statement, we can use web scraping with Beautiful Soup and automate the download process of the pages as images. We can then use the PyPDF module to convert these images into a PDF format and merge them into a single PDF file.

As a trial, we have also included a Jupyter notebook version, which connects to your Google Drive and does all the processing in Google Drive itself, including downloading and deleting the images and PDFs after merging all the pages into a single PDF.

This project can be useful for people who need to access the newspaper in a more convenient and readable format. It also demonstrates the power of web scraping and how it can be used to automate repetitive tasks.
