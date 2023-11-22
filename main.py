import ebooklib
from ebooklib import epub

#book = epub.read_epub('moby-dick.epub')

#for image in book.get_items_of_type(ebooklib.ITEM_IMAGE):
    #print(image)


#for item in book.get_items():
    #if item.get_type() == ebooklib.ITEM_DOCUMENT:
        #print('==================================')
        #print('NAME : ', item.get_name())
        #print('----------------------------------')

        #print(item.get_content())
        #print('==================================')


book = epub.read_epub('moby-dick.epub')
items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
#print(items)
title_list = list(book.get_metadata('DC', 'title'))
print(title_list)