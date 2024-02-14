'''needed to be solved add google image scraper
import os
from GoogleImageScraper import GoogleImageScraper

def GoogleImage():
    oo = open("C:\\Users\\alij7\\OneDrive\\Desktop\\Final_projec_desktop_assistant\\database\\data.txt","rt")
    query = str(oo.read())
    oo.close
    print(query)
    pppp = open("C:\\Users\\alij7\\OneDrive\\Desktop\\Final_projec_desktop_assistant\\database\\data.txt","r+")
    pppp.truncate(0)
    pppp.close

    webdriver = "C:\\Users\\alij7\\OneDrive\\Desktop\\Final_projec_desktop_assistant\\database\\webdriver\\chromedriver.exe"
    photos = "C:\\Users\\alij7\\OneDrive\\Desktop\\Final_projec_desktop_assistant\\database\\GooglePhotos"

    search_key = [f"(query)"]
    number = 10
    head = False
    max = (1000,1000)
    min = (0,0)
    for search_key in search_key:
        image_search = GoogleImageScraper(webdriver,photos,search_key,number,head,min,max)
        image_url = image_search.find_image_urls()
        image_search.save_image(image_url)

    os.startfile(photos)
GoogleImage()
'''