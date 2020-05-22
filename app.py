from models.alert import Alert

alert = Alert('cd1f17270ebf4fbfb17dc7305079a0c9', 2000)
alert.save_to_mongo()






# from models.item import Item
#
# url = 'https://www.johnlewis.com/2020-apple-ipad-pro-11-inch-a12z-bionic-ios-wi-fi-128gb/space-grey/p4949052'
# tag_name = 'p'
# query = {'class': 'price price--large'}
#
# ipad = Item(url, tag_name, query)
# ipad.save_to_mongo()
#
# items_loaded = Item.all()
# print(items_loaded)
# print(items_loaded[0].load_price())
