class Item:
    def __init__(self, name, curr_price, original_price, link, rating, rate_count) -> None:
        self.name = name
        self.curr_price = curr_price
        self.original_price = original_price
        self.link = link
        self.rating = rating
        self.rate_count = rate_count
    def __str__(self) -> str:
        if self.original_price == "":
            original = "Not on discount"
        else:
            original = self.original_price
        info =  f"Item name: {self.name}\nCurrent price: {self.curr_price}\n" + \
                f"Origianl price: {original}\nLink: {self.link}\n" + \
                f"Rating: {self.rating}\nRate Count: {self.rate_count}\n"
        return info

    def __repr__(self) -> str:
        if self.original_price == "":
            original = "Not on discount"
        else:
            original = self.original_price
        info =  f"\nItem name: {self.name}\nCurrent price: {self.curr_price}\n" + \
                f"Origianl price: {original}\nLink: {self.link}\n" + \
                f"Rating: {self.rating}\nRate Count: {self.rate_count}\n"
        return info

class Page:
    items = list[Item]
    def __init__(self, index: int) -> None:
        self.index: int = index
        self.items: list[Item] = []
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
    def AddPage(self, page: Page):
        self.pages.append(page)
    def GetPageCount(self):
        count = 0
        for page in self.pages:
            count += page.GetItemCount()
        return count