import requests
from bs4 import BeautifulSoup
import pandas as pd


class Random_name:
    def __init__(self,url):
        self.url = url

    def main_program(self):

        requesting = requests.get(self.url)
        soup = BeautifulSoup(requesting.content,'html.parser')
        
        chapter_url = soup.find_all('a',attrs={'class':'py-1 px-2 border border-color-border-secondary rounded text-sm'})
        # print(chapter_url)

        url_list = []

        for url in chapter_url:
            every_chapter_url = url['href']
            real_url = ('https://mangapill.com'+every_chapter_url)
            url_list.append(real_url)

        url_list.reverse()

        url_stuff = pd.DataFrame(
            {
                'chapter_links':url_list,
            }
        )

        url_stuff.to_csv('manga_all_chapter_url_link.csv')

if __name__ == "__main__":
    print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    url = input("Enter the url of manga you want to download:")

    passing_value = Random_name(url)
    passing_value.main_program()