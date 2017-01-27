from bs4 import BeautifulSoup
import urllib2
count = 2

def generate_next_url(url,count):
    new_url = url +"?page="+str(count)
    print(new_url)
    print("---------------------------------------")
    return new_url

list_of_lists =[]

def basic_function(current_url):
    web_page = urllib2.urlopen(current_url)
    page_text = web_page.read()
    soup = BeautifulSoup(page_text,"lxml")
    tags = soup.find_all("div",{"class":"list-art-image"})
    print(len(tags))
    for i in range(24):
        list_of_lists.append(tags[i].a.get("href"))

def main_function(count):
    url = "http://www.saatchiart.com/paintings/fine-art"
    basic_function(url)
    for i in range(1):
        basic_function(generate_next_url(url,count))
        count+=1
    print("lenth of the total")
    print(len(list_of_lists))
    with open("urls_data_fineart_sample", "w") as a_file:
        a_file.write('\n'.join(url for url in list_of_lists))

main_function(count)