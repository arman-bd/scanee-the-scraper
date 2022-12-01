import undetected_chromedriver as uc

def create_driver() -> uc.Chrome:
    options = uc.ChromeOptions()
    options.add_argument('--headless')  # Run Selenium Driver in Headless Mode
    # options.add_argument('--no-sandbox') # No Sandbox for Selenium Driver
    # options.add_argument('--disable-dev-shm-usage') # Disable Dev Shm Usage for Selenium Driver
    
    # Create the Selenium Driver
    driver: uc.Chrome = uc.Chrome(options=options)
    
    # Set Window Size [ 800 x 800 ]
    driver.set_window_position(0, 0)
    driver.set_window_size(800, 800)
    
    return driver