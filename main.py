from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep



def main():
    driver = webdriver.Edge()
    url = 'https://memoryzone.com.vn/'
    driver.get(url)
    link_product = []
    product_types = driver.find_elements(By.CSS_SELECTOR, ".item.slick-slide [href]")
    for type in product_types:
        link = type.get_attribute("href")
        if link not in link_product:
            link_product.append(link)
    collections = []
    for link in link_product[1:3]:
        driver.get(link)
        print(link)
        sleep(5)
        link = driver.current_url
        print(link)


if __name__ == "__main__":
    main()