from urllib import request
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests  # Import the requests module
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Replace 'path_to_webdriver' with the actual path to your web driver executable
driver = webdriver.Chrome(ChromeDriverManager().install())
print('driver',driver)
# chromedriver_path = 'C:/Users/hp/Desktop/nstaReelDownload'
# driver = webdriver.Chrome(executable_path=chromedriver_path)
# driver = webdriver.Chrome('C:/Users/hp/Desktop/nstaReelDownload')
video_url = "https://www.instagram.com/reel/CsJJtnQhM9f/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA=="  # Replace 'VIDEO_ID' with the actual video ID
driver.get(video_url)
print('video_url',video_url)
# Wait for the page to load for 3 seconds
time.sleep(5)
# Wait for the video element to be present
wait = WebDriverWait(driver, 10)
video_element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "video")))
print('video_element',video_element)
video_source = video_element.get_attribute("src")
print(video_source)
# Download the video using the extracted URL
with open('video_reel.mp4', 'wb') as video_file:
    response = requests.get(video_source)   
    print('response',response)
    video_file.write(response.content)
