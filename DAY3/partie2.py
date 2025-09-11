from bs4 import BeautifulSoup

def create_bs_obj(file: str) -> BeautifulSoup:
    try:
        with open(file, "r") as f:
            html_content = f.read()
        soup = BeautifulSoup(html_content, "html.parser")
        return soup
    except FileNotFoundError:
        print(f"Erreur : le fichier {file} n'existe pas.")
        return None
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return None


if __name__ == "__main__":
    soup_obj = create_bs_obj("resources/example.html")
    if soup_obj:
        print(soup_obj.title.string)






def find_title(file: str) -> str:
    try:
        with open(file, "r", encoding="utf-8") as f:
            html_content = f.read()
        soup = BeautifulSoup(html_content, "html.parser")
        title_tag = soup.title
        return str(title_tag.string) if title_tag else ""
    except FileNotFoundError:
        return f"Erreur : le fichier {file} n'existe pas."
    except Exception as e:
        return f"Erreur lors de la lecture du fichier : {e}"


if __name__ == "__main__":
    file = "resources/example.html"
    title = find_title(file)
    print(title)




def find_paragraphs(file: str) -> list[str]:
    try:
        with open(file, "r", encoding="utf-8") as f:
            html_content = f.read()
        soup = BeautifulSoup(html_content, "html.parser")

        paragraphs = soup.find_all("p")

        return [str(p) for p in paragraphs]

    except FileNotFoundError:
        return [f"Erreur : le fichier {file} n'existe pas."]
    except Exception as e:
        return [f"Erreur lors de la lecture du fichier : {e}"]


if __name__ == "__main__":
    file = "resources/example.html"
    paragraphs = find_paragraphs(file)
    for paragraph in paragraphs:
        print(paragraph)












