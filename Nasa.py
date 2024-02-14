import requests
import os
from datetime import datetime
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from PIL import Image
import random
from bs4 import BeautifulSoup
import pyttsx3 #for speak
import speech_recognition as sr #for take command


engine = pyttsx3.init('sapi5')#to activiate sapi5 driver
voices = engine.getProperty('voices')#it will get all voices
engine.setProperty('voices',voices[0].id)#which voices to be use
engine.setProperty('rate',170)#speed rate of voices

def Speak(audio):
    print("    ")
    print(f": {audio}")
    print("    ")
    engine.say(audio)
    engine.runAndWait()

Api_key = "5RHra66DtqeTuqM5QCAlNzAL6wb0XPVjikalRY6G"

def NasaNews(date):
    Speak('Extracting Data From NASA.')

    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': Api_key, 'date': str(date)}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        data = response.json()

        title = data.get('title', 'No Title')
        explanation = data.get('explanation', 'No Explanation')
        image_url = data.get('url', '')

        # Download and save the image
        image_response = requests.get(image_url)
        image_filename = f'{date}.jpg'
        with open(image_filename, 'wb') as image_file:
            image_file.write(image_response.content)

        # Move the image to a specific directory
        source_path = os.path.abspath(image_filename)
        destination_path = os.path.join('C:\\Users\\alij7\\OneDrive\\Desktop\\Final_projec_desktop_assistant\\database\\nasa_database', image_filename)
        os.rename(source_path, destination_path)

        # Open the image
        img = Image.open(destination_path)
        img.show()


        # Concatenate title and explanation into a single string
        output_text = f'{title}. {explanation}'

        # Limit the output to two lines
        lines = output_text.split('.')
        Speak(lines[0])  # Speak the first line
        Speak(lines[1])  # Speak the second line
        os.remove(destination_path)
        print(f"the image deleted {destination_path}")

    except requests.RequestException as e:
        Speak(f'Error during NASA API request: {e}')

    except Exception as e:
        Speak(f'An unexpected error occurred: {e}')



def Summary(Body):
    list__ = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
    value = random.choice(list__)
    path = 'C:\\Users\\alij7\\OneDrive\\Desktop\\Final_projec_desktop_assistant\\database\\nasa_database\\Imagesused\\' + str(value) + '.jpg'

    os.startfile(path)

    name = str(Body)
    
    try:
        # Wikipedia API URL
        url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exintro=true&titles={name}"

        response = requests.get(url)
        response.raise_for_status()  # Check for errors

        data = response.json()
        
        # Extracting the page content from the API response
        pages = data.get('query', {}).get('pages', {})
        page_id = list(pages.keys())[0]
        page_content = pages[page_id].get('extract', '')

        if page_content:
            # Using BeautifulSoup to clean up HTML content
            soup = BeautifulSoup(page_content, 'html.parser')
            cleaned_content = ' '.join(soup.stripped_strings)
            
            # Restrict the content to two lines with a character limit
            max_chars_per_line = 100  # Adjust as needed
            content_lines = [cleaned_content[i:i+max_chars_per_line] for i in range(0, len(cleaned_content), max_chars_per_line)]
            restricted_content = ' '.join(content_lines[:2])
            
            Speak(f"According to Wikipedia, {restricted_content}")
        else:
            Speak("No Data Available, Try Again Later!")

    except requests.exceptions.RequestException as e:
        Speak(f"Error making API request: {e}")

def MarsImage(Value):
    date = Value

    Speak('Wait sir, I am finding images')

    name = 'curiosity'

    Api_ = str(Api_key)  # Assuming Api_key is defined somewhere

    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={Api_key}"

    r = requests.get(url)

    Data = r.json()

    photos = Data['photos'][:3]

    try:

        for index, photo in enumerate(photos):

            camera = photo['camera']
            rover = photo['rover']

            rover_name = rover['name']
            camera_name = camera['name']
            full_camera_name = camera['full_name']
            date_of_photos = photo['earth_date']
            img_url = photo['img_src']

            p = requests.get(img_url)

            img = f'{index}.jpg'

            with open(img, 'wb') as file:
                file.write(p.content)

            path_1 = "C:\\Users\\alij7\\OneDrive\\Desktop\\Final_projec_desktop_assistant\\" + str(img)
            path_2 = "C:\\Users\\alij7\\OneDrive\\Desktop\\Final_projec_desktop_assistant\\database\\nasa_database\\marsimages\\" + str(img)

            os.rename(path_1, path_2)

            os.startfile(path_2)

            Speak(f"This image was captured with : {full_camera_name}")

            # Delete the image file after showing it
            os.remove(path_2)

    except Exception as e:
        print(e)
        Speak('Something went wrong')



def trackISS():
    try:
        url = "http://api.open-notify.org/iss-now.json"

        r = requests.get(url)
        r.raise_for_status()  # Raise an HTTPError for bad responses

        data = r.json()

        dt = data['timestamp']
        lat = data['iss_position']['latitude']
        lon = data['iss_position']['longitude']

        Speak(f"Latitude: {lat}")
        Speak(f"Longitude: {lon}")

        plt.figure(figsize=(10, 8))
        ax = plt.axes(projection=ccrs.PlateCarree())
        ax.stock_img()

        plt.scatter(float(lon), float(lat), color='blue', marker='o')
        Speak('Here it is located now.')
        plt.show()

    except requests.RequestException as e:
        Speak(f'Error during API request: {e}')

    except Exception as e:
        Speak(f'An unexpected error occurred: {e}')

import requests

def Astro(start_date, end_date):
    try:
        url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={Api_key}"

        r = requests.get(url)
        r.raise_for_status()  # Raise an HTTPError for bad responses

        Data = r.json()

        Total_Astro = Data['element_count']

        neo = Data['near_earth_objects']

        Speak(f"Total Astroid Between {start_date} and {end_date} Is : {Total_Astro}")

        Speak("Exact Data For Those Astroids Are Listed Below .")
        for body in neo[start_date]:
            id = body['id']
            name = body['name']
            absolute = body['absolute_magnitude_h']

            print(f"The id number : {id} and name is :{name} and value is {absolute}")

    except requests.exceptions.RequestException as e:
        print(f"Error making the request: {e}")
        # Handle the error, log it, or take appropriate action

    except KeyError as e:
        print(f"Error accessing data: {e}")
        # Handle the KeyError, log it, or take appropriate action

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        # Handle other exceptions if necessary


def SolarBodies(body):
    try:
        url = "https://api.le-systeme-solaire.net/rest/bodies/"

        r = requests.get(url)
        r.raise_for_status()  # Raise an HTTPError for bad responses

        data = r.json()
        bodies = data['bodies']
        number = len(bodies)

        url_1 = f"https://api.le-systeme-solaire.net/rest/bodies/{body}"

        rrr = requests.get(url_1)
        rrr.raise_for_status()

        data_1 = rrr.json()

        mass = data_1['mass']['massValue']
        volume = data_1['vol']['volValue']
        density = data_1['density']
        gravity = data_1['gravity']
        escape = data_1['escape']

        Speak(f"Number of Bodies In Solar System: {number}, That data is available in NASA.")
        Speak(f"Mass of {body} Is {mass} kilograms.")
        Speak(f"Gravity of {body} Is {gravity} meters per second square (m/s²).")
        Speak(f"Escape Velocity of {body} Is {escape} meters per second.")
        Speak(f"Density of {body} Is {density} grams per cubic centimeter.")

    except requests.RequestException as e:
        Speak(f'Error during API request: {e}')

    except Exception as e:
        Speak(f'An unexpected error occurred: {e}')

