import which_one
import getting_chapter_url_x

import requests
from bs4 import BeautifulSoup
import csv
import time
import os


global downloaded_count

def sercher():
    print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    manga_name_text =  input("Enter the manga name you want to download:")
    passing_value = which_one.name(manga_name_text)
    passing_value.manga_name()
    

def all():
    blacklist = ['\,' '/', ':', '*', '?', '”', '<,', '>', '|']

    a = which_one.to_chapter
    # print(a)

    requesting = requests.get(a)
    soup = BeautifulSoup(requesting.content,'html.parser')

    downloading_mangaName = soup.find('h1',class_='font-bold text-xl md:text-3xl').get_text()
    
    #~~~~~~~~~~~~~~~~~~~~~
    downloading_mangaName = list(downloading_mangaName)
    # print("kdajskf{}".format(downloading_mangaName))
    num = 0
    for i in downloading_mangaName:
        if i in blacklist:
            downloading_mangaName[num] = ''
        num+=1
    downloading_mangaName = ''.join(downloading_mangaName)
    # print(downloading_mangaName)

    #~~~~~~~~~~~~~~~~~~~

    start_time = time.time()

    path = 'D:\\downloaded manga'
    os.chdir(path)

    os.mkdir(downloading_mangaName)

    path1 = "{}\\{}".format(path,downloading_mangaName)
    os.chdir(path1)

    with open('D:\project_x\manga_all_chapter_url_link.csv','r') as rf:
        csv_reader = csv.reader(rf)

        i = 0 
        downloaded_count=0

        for row in csv_reader:

            if i >= 1:
                print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Downloading chapter {}".format(i))

                requesting_chp_url = requests.get(row[1])
                soup = BeautifulSoup(requesting_chp_url.content,'html.parser')

                images = soup.find_all('img', attrs={'data-src':True})

                os.mkdir("{}_chapter_{}".format(downloading_mangaName,i))

                a = "{}_chapter_{}".format(downloading_mangaName,i)

                for inder_num,image in enumerate(images):
                    image_src = image['data-src']

                    image_data = requests.get(image_src).content#getting_img

                    with open(a+"\\"+str(inder_num+1)+'.jpg','wb+') as f:
                        f.write(image_data)

                    downloaded_count+=1

                print("finished downloading chapter {}".format(i))
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            i+=1


                
    print("Finished downloading")
    second = time.time() - start_time

    hour = second/3600
    hour = int(hour)

    mins = second/60
    mins = mins-hour*60
    mins = int(mins)

    sec = second-hour*3600-mins*60
    mili = sec-int(sec)
    sec = int(sec)


    print("{} page has been downloaded in {}:{}:{}:{}(hour,min,sec,mili-second)".format(downloaded_count,hour,mins,sec,mili))


sercher()
all()