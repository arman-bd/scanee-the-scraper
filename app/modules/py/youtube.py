import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

async def main():
    
    # Start Driver
    driver = uc.Chrome()

    # Open the page
    driver.get(f"https://www.youtube.com/watch?v={id}")

    # Wait for the page to load
    time.sleep(5)
    
    # Take Screenshot [ After the page loads ]
    driver.save_screenshot("/storage/youtube.png")

    # Get the Title
    title = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[1]/h1/yt-formatted-string").text
    
    # Click on "...more"
    driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[3]/div[1]/div/ytd-text-inline-expander/tp-yt-paper-button[1]").click()
    time.sleep(1)
    
    # Get the Description
    description = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[3]/div[1]/div/ytd-text-inline-expander/yt-formatted-string").text
    
    # Get the Channel
    channel_name = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/ytd-video-owner-renderer/div[1]/ytd-channel-name/div/div/yt-formatted-string/a").text
    
    # Save Screenshot [ Before finishing ]
    driver.save_screenshot("/storage/youtube.png")
    
    # Return the Metadata
    return {
        "title": title,
        "description": description,
        "channel_name": channel_name
    }