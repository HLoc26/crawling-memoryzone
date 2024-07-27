from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from PageStructure import Item, Page, Collection

'''define driver'''
driver = webdriver.Edge()
url = 'https://memoryzone.com.vn/'
driver.get(url)

def GetText(elems: list) -> list:
    res = []
    for elem in elems:
        res.append(elem.text)
    return res

def GetItemInfoInPage(page: int) -> list[object]: # [[item1], [item2], [item3]]
    items = []
    # Get name
    names_elems = driver.find_elements(By.CSS_SELECTOR, ".product-name")
    names = GetText(names_elems)
    # print(names)
    # Get current price (discounted price)
    curr_prices_elems = driver.find_elements(By.CSS_SELECTOR, ".price")
    curr_prices = GetText(curr_prices_elems)
    # print(curr_prices)
    # Get original price (before discount)
    '''TODO: Some product does not have discount'''
    original_price_elems = driver.find_elements(By.CSS_SELECTOR, ".compare-price")
    original_prices = GetText(original_price_elems)
    # print(original_prices)
    # Get link
    link_elems = driver.find_elements(By.CSS_SELECTOR, ".product-name [href]")
    links = []
    for elem in link_elems:
        link = elem.get_attribute("href").strip()
        links.append(link)
    # print(links)
    print(f"names: {len(names)} | cur: {len(curr_prices)} | ori: {len(original_prices)} | links: {len(links)}")
    assert len(names) == len(curr_prices) == len(original_prices) == len(links), "ERROR: len not match"
    for i in range(len(names)):
        item = Item(name=names[i],\
                    curr_price=curr_prices[i], \
                    original_price=original_prices[i], \
                    link=links[i], rating="5", \
                    rate_count="10", \
                    feat="None")
        items.append(item)
    return items

def GetItemCollection(link: str) -> Collection:
    # Get title
    title = driver.find_element(By.CSS_SELECTOR, ".title_page").text
    collection = Collection(title)
    page1 = Page(1)
    page1.AddItem(GetItemInfoInPage(1))
    collection.AddPage(page1)
    # Get items in every other page
    pages = driver.find_elements(By.CSS_SELECTOR, ".page-item")
    pages_count = len(pages) # Count number of pages: get all class .page-item count then - 2 (2 arrows)
    for i in range(2, pages_count - 1):
        link = ""
    return collection

def main():
    link_product = []
    product_types = driver.find_elements(By.CSS_SELECTOR, ".item.slick-slide [href]")
    for type in product_types:
        link = type.get_attribute("href")
        if link not in link_product:
            link_product.append(link)
    if not link_product:
        product_types = driver.find_elements(By.CSS_SELECTOR, ".collections-slide  [href]")
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
        collections.append(GetItemCollection(link))

if __name__ == "__main__":
    main()