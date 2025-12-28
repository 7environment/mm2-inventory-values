import json
from src.utils.get_values import get_values

with open("src/Inventory.json", "r") as file:
    with open("src/to_xlsx_format.txt", "w") as outfile:
        values = get_values()
        rarities = [rarity.capitalize() for rarity in values.keys()]
        text = ""
        total_value = 0
        data = json.load(file)
        for items in data.values():
            for item_tag, item_data in items.items():
                if "Rarity" not in item_data.keys():
                    print(item_tag, item_data)
                else:
                    if item_data["Rarity"] in rarities:
                        if "Chroma" in item_data.keys():
                            item_data["ItemName"] = f"Chroma {item_data["ItemName"]}"
                            item_data["Rarity"] = "Chroma"
                        value = values.get(item_data["Rarity"].lower()).get(item_data["ItemName"].replace("Chroma ", "").replace("BattleAxe", "Battleaxe").strip())
                        if not value:
                            for try_ in ["Year", "ItemType"]:
                                if try_ in item_data.keys():
                                    value = values.get(item_data["Rarity"].lower()).get(item_data["ItemName"].replace("BattleAxe", "Battleaxe").strip() + f" ({item_data[try_]})")
                                    if value:
                                        break
                        if not value:
                            print(item_tag, item_data)
                        try:
                            total_value += value*item_data["Count"]
                        except TypeError as e:
                            pass
                        text += f"{item_tag}_{item_data["ItemName"]}_{item_data["ItemType"]}_{item_data["Rarity"]}_{item_data["Count"]}_{value}\n"
                    else:
                        print(item_tag, item_data)
        print(total_value)
        outfile.write(text)
        outfile.close()
    file.close()