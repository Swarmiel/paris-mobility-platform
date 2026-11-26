import requests
from pathlib import Path

response = requests.get("https://data.iledefrance-mobilites.fr/api/explore/v2.1/catalog/datasets/validations-reseau-ferre-nombre-validations-par-jour-2eme-trimestre/records", timeout=30)
response.raise_for_status()
data = response.json()
content = response.content
Path("data/raw/validations-reseau-ferre-nombre-validations-par-jour-2eme-trimestre.json").write_bytes(content)