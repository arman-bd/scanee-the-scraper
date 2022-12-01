import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

async def wikipedia_metadata(driver: uc.Chrome, tag: str, wait: int = 5):
    """ Get Wikipedia Metadata 
    
    Args:
        driver {uc.Chrome} -- Chrome Driver
        
        tag {str} -- Wikipedia Tag
        
        wait {int} -- Wait Time
    
    Returns:
        dict -- Wikipedia Metadata
    """

    # Open The Page
    driver.get(f"https://en.wikipedia.org/wiki/{tag}")
    
    # Wait for the page to load
    time.sleep(wait)
    
    # Take a Screenshot [ After the page loads ]
    driver.save_screenshot("/storage/wikipedia.png")
    
    # Get the Title
    title = driver.find_element(By.XPATH, "/html/body/div[3]/h1/span").text
    
    # Get the Description
    description = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[1]/p[2]").text
    
    # Take a Screenshot [ Before finishing ]
    driver.save_screenshot("/storage/wikipedia.png")
    
    # Return the Metadata
    return {
        "title": title,
        "description": description
    }


async def youtube_metadata(driver: uc.Chrome, id: str, wait: int = 5):
    """ Get Youtube Metadata
    
    Args:
        driver {uc.Chrome} -- Chrome Driver
        
        id {str} -- Youtube Video Id
        
        wait {int} -- Wait Time
        
    Returns:
        dict -- Youtube Metadata
    """

    # Open the page
    driver.get(f"https://www.youtube.com/watch?v={id}")

    # Wait for the page to load
    time.sleep(wait)
    
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


async def googleplay_metadata(driver: uc.Chrome, package: str, wait: int = 5):
    """ Get Google Play Metadata
    
    Args:
        driver {uc.Chrome} -- Chrome Driver
        
        package {str} -- Google Play Package
        
        wait {int} -- Wait Time
        
    Returns:
        dict -- Google Play Metadata
    """

    # Open the page
    driver.get(f"https://play.google.com/store/apps/details?id={package}")
    
    # Wait for the page to load
    time.sleep(wait)
    
    # Take Screenshot [ After the page loads ]
    driver.save_screenshot("/storage/googleplay.png")
    
    # Get the Title
    title = driver.find_element(By.XPATH, "/html/body/c-wiz[2]/div/div/div[1]/div[1]/div/div/c-wiz/div[2]/div[1]/div/h1/span").text
    
    # Get the Publisher
    publisher = driver.find_element(By.XPATH, "/html/body/c-wiz[2]/div/div/div[1]/div[1]/div/div/c-wiz/div[2]/div[1]/div/div/div[1]/a/span").text
    
    # Download Count
    download_count = driver.find_element(By.XPATH, "/html/body/c-wiz[2]/div/div/div[1]/div[1]/div/div/c-wiz/div[2]/div[2]/div/div/div[2]/div[1]").text
    
    # Click on "About this app"
    driver.find_element(By.XPATH, "/html/body/c-wiz[2]/div/div/div[1]/div[2]/div/div[1]/c-wiz[2]/div/section/header/div/div[2]/button").click()
    time.sleep(3)
    
    # Copy Full Description
    description = driver.find_element(By.TAG_NAME, "html-blob").text
    
    # Save Screenshot [ Before finishing ]
    driver.save_screenshot("/storage/googleplay.png")
    
    # Return the Metadata
    return {
        "title": title,
        "publisher": publisher,
        "download_count": download_count,
        "description": description
    }