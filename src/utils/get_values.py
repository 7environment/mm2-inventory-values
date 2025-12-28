from bs4 import BeautifulSoup
import requests

links = {
    "unique": "https://supremevalues.com/mm2/uniques",
    "ancient": "https://supremevalues.com/mm2/ancients",
    "godly": "https://supremevalues.com/mm2/godlies",
    "chroma": "https://supremevalues.com/mm2/chromas",
    "classic": "https://supremevalues.com/mm2/vintages",
    "legendary": "https://supremevalues.com/mm2/legendaries",
    "rare": "https://supremevalues.com/mm2/rares",
    "uncommon": "https://supremevalues.com/mm2/uncommons",
    "common": "https://supremevalues.com/mm2/commons"
}

def get_values() -> dict[str, dict[str, float]]:
    """
    return: dict like
    {*rarity*: {*itemname*: *itemvalue*}}\n
    edit links under function if you need\n
    classic rarity is vintage rarity
    """
    values = {}
    for rarity, link in links.items():
        html = requests.get(link).text
        soup = BeautifulSoup(html, "lxml")
        for item_div in soup.find_all("div", class_="itemcell"):
            item_name = item_div.find("div", class_="itemhead").text.replace("C.", "").replace("Chroma", "").strip()
            item_value_div = item_div.find("b", class_="itemvalue")
            if item_value_div:
                try:
                    item_value = int(item_value_div.text.replace(",", "").strip())
                except ValueError:
                    item_value = 0.3
                values.setdefault(rarity, {})[item_name] = item_value
    return values

if __name__ == "__main__":
    values = get_values()
    for pair in values.values():
        for item, value in pair.items():
            print(item, value)