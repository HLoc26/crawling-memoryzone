def ExtractPrices(price_strs: list[str]) -> list[float]:
    for i in range(len(price_strs)):
        price_strs[i] = float(price_strs[i][:-3].replace(".", "_").replace(",", "."))
    return price_strs
