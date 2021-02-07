import requests
from bs4 import BeautifulSoup
import pandas as pd
import getting_chapter_url_x
# import final_downloader_x

manga_names = []
raw_link = []
list_of_links = []
dup_list_of_links = []

class which_manga:

    def __init__(self,url):
        self.url = url

    def which_title(self):

        requesting = requests.get(self.url)
        soup = BeautifulSoup(requesting.content, 'html.parser')
        
        text = soup.find_all('a', class_ = 'block text-sm font-bold truncate pb-3 text-color-text-primary')

        def for_loops():
            for i in text:
                for j in i:
                    manga_names.append(j)
            num = 0

            for link in soup.findAll('a'):
                if num >= 7:
                    raw_link.append(link.get('href'))
                num+=1
        for_loops()

        list_of_links = list(dict.fromkeys(raw_link))
        # print(list_of_links)

        if not list_of_links:
            print("There is no such type of manga sorry:")
            print("please try again from start")
            exit()


        del list_of_links[-1]


        # print(manga_names)
        for i in list_of_links:
            dup_list_of_links.append(i)

    def selecting_links(self):

        global to_chapter
        # print("name{}".format(manga_names))

        if len(manga_names) == 1:
            fin_raw_link = dup_list_of_links[0]
            to_chapter = "https://mangapill.com"+fin_raw_link

            # print(to_chapter)


        elif len(manga_names) >= 2:

            print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            printing = pd.DataFrame(
                {
                    'list':manga_names,
                }
            )

            print(printing)
            # print(manga_names)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    

            which_number = int(input("Enter the number of manga you want to download:"))

            if which_number > len(manga_names):
                print("There is only {} option in list.".format(len(manga_names)))
                print("please try again.")
                pass

            else:

                # num = 0
                for i in range(len(manga_names)):

                    if which_number == i:
                        
                        fin_raw_link = dup_list_of_links[which_number]
                        # print(fin_raw_link,'aksjdfhakjsdhfkajsdhfjkasdhfjkasdhfakjsdfhkajsdfhkjdass')
                        to_chapter = "https://mangapill.com"+fin_raw_link
                        # print(to_chapter)
          
    def getting_chapter_url(self):
        passing_value2 = getting_chapter_url_x.Random_name(to_chapter)
        passing_value2.main_program()

class name:
    def __init__(self,manga_name_text):
        self.manga_name_text = manga_name_text

    def manga_name(self):

        url = 'https://mangapill.com/search?title='

        split = self.manga_name_text.split() #splitinig manga_name_text in list
        join = '_'.join(split) #joining split list with _ in middle

        final_url = url+join
        
        passing_value1 = which_manga(final_url)
        passing_value1.which_title()
        passing_value1.selecting_links()
        # passing_value1.getting_chapter_url()
        # print(final_url)


if __name__ == "__main__":
    print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    manga_name_text = input("Enter the manga name you want to download:")

    passing_value = name(manga_name_text)
    passing_value.manga_name()





# print("testing")