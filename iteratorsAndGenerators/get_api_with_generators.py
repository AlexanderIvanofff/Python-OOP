import requests

URL = "https://api.instantwebtools.net/v1/passenger?page={page}&size={size}"


def list_all_passangers():
    size = 20
    page = 0
    total_pages = None
    while True:
        if page == total_pages:
            break
        url = URL.format(page=0, size=size)
        response = requests.get(url)
        date = response.json()
        total_pages = date["totalPages"]
        for passangers in date["data"]:
            yield passangers
        page += 1


for p in list_all_passangers():
    print(p["name"])