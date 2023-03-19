from image_info import image_info
from pprint import pprint
import QtQuick6
import QtQuick.Window2.15
import QtQuick.Controls6
import QtQuick.Controls.Material2.15

new_dict = {}
for img in image_info:
    new_dict[img['id']] = [tag.lower() for tag in img['tags']]

    for keyword in img['title'].split():
        new_dict[img['id']].append(keyword.rstrip(',').lower())

    new_dict[img['id']].insert(0,0)
    new_dict[img['id']].insert(1, img['title'][0].lower())
    
    def get_count_from_search(my_search):
       my_search = my_search.lower()
       max_key = ''
       max = 0
       for key, value in new_dict.items():
           for counter, term in enumerate(value):
               if counter > 1:
                   if term in my_search:
                       value[0] += 1
               if value[0] > max:
                   max = value[0]
                   max_key = key
                   print(max_key)
       return max_key



my_search = input("start typing->")
get_count_from_search(my_search)