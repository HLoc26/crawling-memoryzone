from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep



def main():
    driver = webdriver.Edge()
    url = 'https://memoryzone.com.vn/'
    driver.get(url)
    

if __name__ == "__main__":
    main()