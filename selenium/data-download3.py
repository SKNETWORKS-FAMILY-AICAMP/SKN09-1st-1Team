from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import os


# Setup download directory
download_path = os.path.expanduser("C:/Users/playdata/Downloads")  # Change this to your desired path
options = webdriver.ChromeOptions()
prefs = {"download.default_directory": download_path}
options.add_experimental_option("prefs", prefs)
#options.add_argument("--headless")  # Run Chrome in headless mode
# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open the webpage
    url = "https://stat.molit.go.kr/portal/cate/statView.do?hRsId=58&hFormId=5498&hDivEng=&month_yn="
    driver.get(url)
    time.sleep(1)  # Wait for the page to load

    # Locate the download button
    download_button = driver.find_element(By.ID, "fileDownBtn")
    ActionChains(driver).move_to_element(download_button).click().perform()
    time.sleep(0.5)

    # Click the download button
    
    
    download_button1 = driver.find_element(By.XPATH,'//*[@id="file-download-modal"]/div[2]/div[3]/button')
    ActionChains(driver).move_to_element(download_button1).click().perform()
    time.sleep(10)  # Wait for the file to download



    print(f"File has been downloaded to {download_path}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the WebDriver
    driver.quit()
