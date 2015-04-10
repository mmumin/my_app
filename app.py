__author__ = "mumin"

class my_app(object):
    
    def __init__(self, file_arg):
	fd = open(file_arg,'r')
	self.lines = fd.readlines()
	self.lines = [[j.strip() for j in i.strip('\r\n').split(',')] for i in self.lines]

    def get_data(self):
	for item in self.lines:
	    if len(item) < 3:
	        continue
	    labels = [item[i] for i in range(2, len(item))]
	    res_id = item[0]
	    if res_id in total_data.keys():
	        lst_of_tup_of_prices = total_data[res_id]
	        lst_of_tup_of_prices.append((item[1], labels))
	        total_data[res_id] = lst_of_tup_of_prices
	    else:
	        total_data[res_id] = [(item[1], labels)]

    def minimun(self, lst):
	mini_price = lst[0][1]
	rest_id = lst[0][0]
	for i in lst:
	    if float(i[1]) < float(mini_price):
	        mini_price = i[1]
                rest_id = i[0]
	return rest_id, mini_price

    def check_single_rest(self, item_labels):
	final_list = []
	for index, item in enumerate(self.lines):
	    if set(item_labels).issubset(item):
	        final_list.append([item[0], item[1]])
	if final_list.__len__() >= 1:
	    return self.minimun(final_list)
        else:
            return None, None

    def prices_n_rest(self, label):
	lst_of_metadata = []
	for key in total_data.keys():
	    for item in total_data[key]:
	        if label in item[1]:
	            rest_id, price = key, item[0]
	            lst_of_metadata.append((rest_id, price))
	return lst_of_metadata

    def get_mult_comb(self, item_labels):
	for label in item_labels:
	    meta_data = self.prices_n_rest(label)
	    print label, '\t:\t', meta_data

if __name__ == '__main__':
	total_data = {}
	import sys
	app_obj = my_app(sys.argv[1])
	app_obj.get_data()
	label_lst = [i for i in sys.argv[2:][0:]]
	restaurant, prices = app_obj.check_single_rest(label_lst)
        list_of_restaurants = []
	if restaurant and prices:
            list_of_restaurants.append((restaurant, prices))
	app_obj.get_mult_comb(label_lst)
        if not list_of_restaurants:
            print "Nil"
        else:
            print list_of_restaurants[0][0], list_of_restaurants[0][1],'\n\n'
            print list_of_restaurants
        #print total_data
	#print app_obj.lines
