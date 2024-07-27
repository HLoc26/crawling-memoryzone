import pandas as pd
class Item:
    def __init__(self, name, curr_price, original_price, link, rating, rate_count) -> None:
        self.name = name
        self.curr_price = curr_price
        self.link = link
        self.rating = rating
        self.rate_count = rate_count
        if original_price == "":
            self.original_price = "Not on discount"
        else:
            self.original_price = original_price
    def __str__(self) -> str:
        info =  f"Item name: {self.name}\nCurrent price: {self.curr_price}\n" + \
                f"Origianl price: {self.original_price}\nLink: {self.link}\n" + \
                f"Rating: {self.rating}\nRate Count: {self.rate_count}\n"
        return info
    def __repr__(self) -> str:
        info =  f"\nItem name: {self.name}\nCurrent price: {self.curr_price}\n" + \
                f"Origianl price: {self.original_price}\nLink: {self.link}\n" + \
                f"Rating: {self.rating}\nRate Count: {self.rate_count}\n"
        return info

class Page:
    items = list[Item]
    def __init__(self, index: int) -> None:
        self.index: int = index
        self.items: list[Item] = []
    def __repr__(self) -> str:
        info = ""
        for item in self.items:
            info += str(item) + "\n"
        return info
    def AddItem(self, item: list[Item]):
        for i in item:
            self.items.append(i)
    def GetItemCount(self):
        return len(self.items)

class Collection:
    pages = list[Page]
    def __init__(self, title: str) -> None:
        self.title = title
        self.pages: list[Page] = []
    def __repr__(self) -> str:
        info = ""
        for page in self.pages:
            info += str(page) + "\n"
        return info
    def AddPage(self, page: Page):
        self.pages.append(page)
    def GetPageCount(self):
        count = 0
        for page in self.pages:
            count += page.GetItemCount()
        return count
    def ToDataFrame(self) -> pd.DataFrame:
        data = []
        for page in self.pages:
            for item in page.items:
                data.append({
                    'Name': item.name,
                    'Current price': item.curr_price,
                    'Original price': item.original_price,
                    'Link': item.link,
                    'Rating': item.rating,
                    'Rate Count': item.rate_count
                })
        df = pd.DataFrame(data)
        return df
        