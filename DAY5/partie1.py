import requests

def get_companies_with_name(name: str) -> list[dict]:
    url = "https://recherche-entreprises.api.gouv.fr/search"
    params = {"q": name}
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        results = []
        for e in data.get("results", []):
            results.append({
                "siren": e.get("siren"),
                "nom": e.get("nom_complet"),
                "date_creation": e.get("date_creation")
            })

        return results
    except Exception:
        return []

if __name__ == "__main__":
    entreprises = get_companies_with_name("EPITECH")
    for e in entreprises:
        print(e)





import requests

def get_all_companies_with_name(name: str) -> list[dict]:

    url = "https://recherche-entreprises.api.gouv.fr/search"
    params = {"q": name, "page": 1}
    all_results = []

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        total_results = data.get("total_results", 0)
        per_page = data.get("per_page", len(data.get("results", [])))
        total_pages = (total_results // per_page) + (1 if total_results % per_page else 0)

        for e in data.get("results", []):
            all_results.append({
                "siren": e.get("siren"),
                "nom": e.get("nom_complet"),
                "date_creation": e.get("date_creation")
            })

        for page in range(2, total_pages + 1):
            params["page"] = page
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()

            for e in data.get("results", []):
                all_results.append({
                    "siren": e.get("siren"),
                    "nom": e.get("nom_complet"),
                    "date_creation": e.get("date_creation")
                })

        return all_results
    except Exception:
        return []


if __name__ == "__main__":
    entreprises = get_all_companies_with_name("ESSEC")
    print(f"Nombre total d'entreprises : {len(entreprises)}")
    for e in entreprises[:5]:
        print(e)




import csv
import os

def get_and_store_companies(filename: str, name: str):

    companies = get_all_companies_with_name(name)
    if not companies:
        return

    existing_sirens = set()
    if os.path.exists(filename):
        with open(filename, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing_sirens.add(row["siren"])

    new_companies = [c for c in companies if c["siren"] not in existing_sirens]

    if not new_companies:
        return

    all_companies = []

    if os.path.exists(filename):
        with open(filename, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                all_companies.append(row)

    all_companies.extend(new_companies)

    all_companies.sort(key=lambda x: x["siren"])

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["siren", "nom", "date_creation"])
        writer.writeheader()
        writer.writerows(all_companies)


if __name__ == "__main__":
    get_and_store_companies("entreprises.csv", "APPLE")
    print("Fichier entreprises.csv mis à jour ")
