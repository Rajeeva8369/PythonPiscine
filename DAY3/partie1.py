import requests

def get_request(url: str) -> (int, dict):
    try:
        response = requests.get(url)
        status_code = response.status_code

        try:
            data = response.json()
        except ValueError:
            data = {"error": "Réponse non au format JSON"}

        return status_code, data

    except requests.exceptions.RequestException as e:
        return 0, {"error": str(e)}


if __name__ == "__main__":
    url = "https://restcountries.com/v3.1/name/france"
    code, contenu = get_request(url)
    print("Code statut :", code)
    print("Contenu JSON :", contenu)





def get_countries_info(country_codes: list, info: list) -> (int, dict):
    try:
        codes_str = ",".join(country_codes)
        fields_str = ",".join(info)
        url = f"https://restcountries.com/v3.1/alpha?codes={codes_str}&fields={fields_str}"

        response = requests.get(url)
        status_code = response.status_code

        try:
            data = response.json()
        except ValueError:
            data = {"error": "Réponse non au format JSON"}

        return status_code, data

    except requests.exceptions.RequestException as e:
        return 0, {"error": str(e)}



if __name__ == "__main__":
    codes = ["fr", "de", "es"]
    infos = ["name", "capital", "languages"]
    code, contenu = get_countries_info(codes, infos)
    print("Code statut :", code)
    print("Contenu JSON :", contenu)




def handle_request_status(url: str) -> int | str:
    try:
        response = requests.post(url)
        response.raise_for_status()
        return response.status_code
    except requests.exceptions.RequestException as e:
        return str(e)


if __name__ == "__main__":
    test_url = "https://httpbin.org/post"
    print(handle_request_status(test_url))

    bad_url = "https://httpbin.org/status/404"
    print(handle_request_status(bad_url))





def send_query_parameters(params: dict) -> dict:
    try:
        url = "https://httpbin.org/response-headers"
        response = requests.get(url, params=params)
        return response.headers
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


if __name__ == "__main__":
    params = {"X-Test": "HelloWorld", "Content-Language": "fr"}
    headers = send_query_parameters(params)
    print(headers)



def send_headers(headers: dict) -> str:
    try:
        url = "https://httpbin.org/headers"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("headers", {})
    except requests.exceptions.RequestException as e:
        return str(e)


if __name__ == "__main__":
    custom_headers = {"X-Custom-Header": "ChatGPT", "User-Agent": "Python-Requests"}
    result = send_headers(custom_headers)
    print(result)
