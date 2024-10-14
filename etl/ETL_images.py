
import os
from pprint import pprint
from typing import List

import requests as req
from bs4 import BeautifulSoup


class ETLImages:
    BASE_URL:str = "https://kodem-tcg.com/"
    PATHS: List[str] = [
        "raices-misticas",
        "la-guerra-roja",
        "titanes-de-la-corteza-deck",
    ]
    FOLDER_IMG:str = "img"

    def __init__(self) -> None:
        self.texts = {
            path: [] for path in self.PATHS
        }
        self.images_paths = {
            path: [] for path in self.PATHS
        }

    def extract(self) -> None:
        for path in self.PATHS:
            response = req.get(self.BASE_URL + path)
            if response.status_code == 200:
                self.texts[path].append(response.text)

    def transform(self) -> None:
        for key, texts in self.texts.items():
            for text in texts:
                soup = BeautifulSoup(text, "html.parser")
                img_tags = soup.find_all("img")
                for img_tag in img_tags:
                    src = img_tag.get("src")
                    if src:
                        self.images_paths[key].append(src)

    def load(self) -> None:
        for key, imgs_path in self.images_paths.items():
            print(os.path.exists(os.path.join(self.FOLDER_IMG, key)))
            if not os.path.exists(os.path.join(self.FOLDER_IMG, key)):
                os.makedirs(os.path.join(self.FOLDER_IMG, key))

            for img_path in imgs_path:
                try:
                    img_data = req.get(img_path).content
                    name_img = img_path.split("/")[-1]
                    with open(
                        f"{self.FOLDER_IMG}/{key}/{name_img}", "wb"
                        ) as handler:
                        handler.write(img_data)
                    print(img_path)
                except Exception as e:
                    print("!" * 50)
                    print(f"Error al descargar la imagen: {e}")
                    print("!" * 50)

    def __str__(self) -> str:
        return "ETLImages class"


if __name__ == '__main__':
    etl = ETLImages()
    etl.extract()
    etl.transform()
    etl.load()
