from bs4 import BeautifulSoup
import urllib2
import re
import csv

with open("urls_data_fineart", "r") as a_file:
    url_data = a_file.read().split("\n")

title_list =[]
creator_list =[]
size_prod_list =[]
views_list =[]
favourites_list = []
price_list =[]
medium_list =[]
co =0
a = "http://www.saatchiart.com/"

for url in url_data:
    s = a+url
    web_page = urllib2.urlopen(s)
    page_text = web_page.read()
    soup = BeautifulSoup(page_text,"lxml")
    # tag1 = soup.find("div",{"class":"small-12 medium-6 large-12 columns art-meta"})
    # print(tag1.text)
    # tag2= soup.find("div",{"class":"small-12 medium-6 large-12 columns"})
    # print(tag2.text)
    title = soup.find("h3",{"itemprop":"name"})
    if title.text != None:
        if isinstance(title.text ,str):
            title1 = unicode(title.text, "utf-8")
            title_list.append(title1)
        title_list.append(title.text.encode("utf-8"))
    else:
        title_list.append("NA")
    creator = soup.find("p",{"itemprop":"creator"}).a
    if creator.text != None:
        if isinstance(creator.text ,str):
            creator1 = unicode(creator.text, "utf-8")
            creator_list.append(creator1)
        creator_list.append(creator.text.encode("utf-8"))
    else:
        creator_list.append("NA")
    size = soup.find("p",{"class":"category-size"})
    sizes = [re.search(r'[\d.]+', s.text).group() for s in size.find_all("span")]
    size_list = [float(x) for x in sizes]
    size_prod = reduce(lambda x, y: x*y, size_list)
    size_prod_list.append(size_prod)
    medium = soup.find_all("div",{"class":"small-12 columns"})
    # medium2 = medium
    if "Canvas" and not "Oil" in medium[1].text.strip():
        medium_list.append("1")
    elif "Wood" and "Acrylic" in medium[1].text.strip():
        medium_list.append("2")
    elif  "Acrylic" and "Oil" in medium[1].text.strip():
        medium_list.append("3")
    else:
        medium_list.append("0")
    # print("------")
    #
    # print(len(size_prod_list))
    price = soup.find('span',{"class":"price"})
    if price != None :
        prices =(price.text.strip())
        prices1 = prices.strip("$")
    else:
        prices1 = "1400"
    views = soup.find("div",{"class":"art-detail-stats"})
    view =re.search(r'[\d]+', views.text).group()
    favourites = soup.find("div",{"id":"favoriteCount"})
    views_list.append(view)
    favourites_list.append(favourites.text)
    price_list.append("".join(prices1.split(",")))
    # print("".join(prices1.split(",")))
    # print(co)
    # co+=1
    # if co==20:
    #     break

# l = []
# print(len(title_list))
# for ls in [title_list, creator_list, size_list, views_list, favourites_list, price_list]:
#     print(ls)
# print("-------------------------------------------------------------------------------------------------------------------------")

print(len(title_list),len(creator_list),len(size_prod_list),len(views_list),len(favourites_list),len(price_list),len(medium_list))

for t, c, s, v, f, p,m in zip(title_list, creator_list, size_prod_list, views_list, favourites_list, price_list,medium_list):
    print(str(t),str(c),int(s),int(v),int(f),int(p),int(m))

with open('final_file.csv', 'wb') as csvfile:
    wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    # wr.writerows()
    for a in zip(title_list, creator_list, size_prod_list, views_list, favourites_list, price_list,medium_list):
        wr.writerow(a)
