class Item:
    def __init__(self, name, curr_price, original_price, link, rating, rate_count, feat) -> None:
        self.name = name
        self.curr_price = curr_price
        self.original_price = original_price
        self.link = link
        self.rating = rating
        self.rate_count = rate_count
        self.feat = feat
    def __str__(self) -> str:
        if self.original_price == "":
            original = "Not on discount"
        else:
            original = self.original_price
        features = '\t'.join(self.feat)
        info =  f"Item name: {self.name}\nCurrent price: {self.curr_price}\n" + \
                f"Origianl price: {original}\nLink: {self.link}\n" + \
                f"Rating: {self.rating}\nRate Count: {self.rate_count}\n" + \
                f"Features: \n\t{features}"
        return info

    def __repr__(self) -> str:
        if self.original_price == "":
            original = "Not on discount"
        else:
            original = self.original_price
        features = '\t'.join(self.feat)
        info =  f"\nItem name: {self.name}\nCurrent price: {self.curr_price}\n" + \
                f"Origianl price: {original}\nLink: {self.link}\n" + \
                f"Rating: {self.rating}\nRate Count: {self.rate_count}\n" + \
                f"Features: \n\t{features}\n"
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