import requests


def get_photo_link(photo_bytes):
    data = {"file": photo_bytes}
    with requests.Session() as session:
        r = session.post("https://telegra.ph/upload/", files=data)
        link = "https://telegra.ph/" + r.json()[0]["src"]
    return link
