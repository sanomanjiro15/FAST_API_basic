import os

url = "http://127.0.0.1:80"
token = ""
base_path = f"{os.path.dirname(os.path.abspath(__file__))}/"


ACCESSED_CATALOG_ENUM = ["food", "phones", "furniture", "vehicle", "international_food"]
ROLE_ENUM = ["admin", "seller", "expert"]