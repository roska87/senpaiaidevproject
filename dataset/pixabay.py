import requests
import json
import math
import sys
import os

page = 1
per_page = 200
limit = 2000
url = 'https://pixabay.com/api/?key=17655836-b65b60b63807902874dd28028&q={}&image_type=photo&pretty=true&page={}' \
              '&per_page={}'
url_set = set()


def get_results(url, search_words, page, per_page):
    url = url.format(search_words, page, per_page)
    print(url)
    r = requests.get(url)
    json_object = json.loads(r.text)
    return json_object


def download_image(path, url):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        name = url.split('/')[-1]
        file = open(path + name, "wb")
        file.write(r.content)
        file.close()


search_words = input('Enter search words: ')
if len(search_words) != 0:
    search_words = search_words.replace(" ", "+")
    print(search_words)
else:
    print("Must enter search words")
    sys.exit()

target_folder = os.path.join("images/", '_'.join(search_words.lower().split(' ')))
if not os.path.exists(target_folder):
    os.makedirs(target_folder)
target_folder = target_folder + "/"

print("Get data")
result = get_results(url, search_words, page, per_page)
total_hits = result['totalHits']
pages = math.ceil(total_hits/per_page)+1

for page in range(1, pages):
    print("page", page)
    result = get_results(url, search_words, page, per_page)
    hits = result['hits']
    print(len(list(hits)))
    for hit in list(hits):
        url_set.add(hit['previewURL'])
        # print(hit['previewURL'])
    if len(url_set) >= limit:
        break

print("Download", len(url_set), "images")
lst = list(url_set)
for i in range(len(lst)):
    if i % 50 == 0:
        print("Downloaded", i, "from", len(lst))
    download_image(target_folder, lst[i])
