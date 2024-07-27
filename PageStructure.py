class Item:
    def __init__(self, name, curr_price, original_price, link, rating, rate_count, feat) -> None:
        self.name = name
        self.curr_price = curr_price
        self.original_price = original_price
        self.link = link
        self.rating = rating
        self.rate_count = rate_count
        self.feat = feat

class Page:
    def __init__(self, index: int) -> None:
        self.index: int = index
        self.items: list[Item] = []
    def AddItem(self, item: list[Item]):
        self.items.append(item)

class Collection:
    def __init__(self, title: str) -> None:
        self.title = title
        self.pages: list[Page] = []
    def AddPage(self, page: Page):
        self.pages.append(page)