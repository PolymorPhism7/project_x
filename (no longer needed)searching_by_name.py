import requests
from bs4 import BeautifulSoup

class name:
    def __init__(self,manga_name_text):
        self.manga_name_text = manga_name_text

    def manga_name(self):

        url = 'https://mangapill.com/search?title='

        split = self.manga_name_text.split() #splitinig manga_name_text in list
        join = '_'.join(split) #joining split list with _ in middle

        final_url = url+join
        return final_url
        # print(final_url)


if __name__ == "__main__":
    manga_name_text = input("Enter the manga name you want to download:")

    passing_value = name(manga_name_text)
    passing_value.manga_name()
