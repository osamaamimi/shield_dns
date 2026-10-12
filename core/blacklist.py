from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
BLACKLIST_PATH = BASE_DIR / "data" / "blacklist.txt"

def load_domains():
    domains=set()
    with open("data/blacklist.txt", encoding="utf-8")as f:
        for ligne in f:
            ligne = ligne.strip()
            ligne = ligne.lower()
            if not ligne or ligne.startswith("#") :
                continue

            domains.add(ligne)

    return domains

