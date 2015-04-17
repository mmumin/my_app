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

    def remove_identical(self, data_dict):
	new_dict = {}
	for key, data in data_dict.iteritems():
	    new_data = []
	    for item in data:
		if item not in new_data:
		    new_data.append(item)
	    new_dict[key] = new_data
	return new_dict

    def get_permutations(self, label_items):
	import itertools
	permutats = list(itertools.permutations(label_items, len(label_items)))
	permutats = [list(i) for i in permutats]
	identical = []
	for item in permutats:
	    if not set(item) in [set(j) for j in identical]:
		identical.append(item)
	return identical

    def check_permut_price_if_any(self, permut, total_ramaining_rest_data):
	lst_of_prices = []
	for item in total_ramaining_rest_data:
	    if set(permut).issubset(item[1]) and len(permut) <= len(item[1]):
		lst_of_prices.append(item[0])
	try:
	    return min([float(i) for i in lst_of_prices])
	except:
	    return None

    def check_this(self, rest_id, label_found, label_found_price, remaining_label_items, total_ramaining_rest_data):
        total_price = float(label_found_price)
	permutats = self.get_permutations(remaining_label_items)
	for permut in permutats:
	    remaining_price = self.check_permut_price_if_any(permut, total_ramaining_rest_data)
	    if remaining_price:
		total_price = total_price + float(remaining_price)
	        if not [rest_id, total_price] in multiple_list:
	            multiple_list.append([rest_id, total_price])
	#print rest_id, multiple_list

    def check_minimum(self, label_items):
        for rest_id, rest_data in self.data_dict.iteritems():
            for index, item in enumerate(rest_data):
	        if set(item[1]).issubset(label_items):
                    for i in item[1]:
                        label_items.remove(i)
                        self.check_this(rest_id, item[1], item[0], label_items, rest_data)
                    for i in item[1]:
                        label_items.append(i)


    def check_multiple_rest(self, items_label):
	label_list = [i for i in items_label]
	self.data_dict = {}
	for key, value in total_data.iteritems():
	    for each in value:
		for item in items_label:
	            if set([item]).issubset(each[1]):
		        label_list.remove(item)
		        if not key in self.data_dict.keys():
			    self.data_dict[key] = [each]
        		else:
			    old_data = self.data_dict[key]
			    old_data.append(each)
			label_list.append(item)
	self.data_dict = self.remove_identical(self.data_dict)
	self.check_minimum(items_label)
	multuple_menu_cost = self.check_lowest_of_all_labels(items_label)
	return multuple_menu_cost


    def min_of_label(self, label, data, prices):
	for index, item in enumerate(data):
	    if set(label).issubset(item[1]):
	        if label in prices.keys():
		    if float(prices[label][1]) > float(item[0]):
		        prices[label] = (index, item[0])
		else:
		    prices[label] = (index, item[0])
	return prices


    def check_lowest_of_all_labels(self, lables):
	data = self.data_dict#{'1': [('2.00', ['A']), ('1.25', ['B']), ('2.00', ['C']), ('1.00', ['D']), ('1.00', ['A', 'B']), ('1.50', ['A', 'C']), ('2.50', ['A', 'D'])]}
	#lables = ['B', 'C', 'A', 'D']
	lowest_comb_in_rest = {}
	for rest_id in data.keys():
	    prices = {}
	    for label in lables:
		prices = self.min_of_label(label, data[rest_id], prices)
	    new_dict = {}
	    index_list = []
	    data_list = []
	    for key, tup in prices.iteritems():
		if not float(tup[0] in index_list):
		    data_list.append(float(tup[1]))
		    index_list.append(float(tup[0]))
	    leng = 0.0
	    for i in data_list:
		leng = leng + i
	    lowest_comb_in_rest[rest_id] = leng
	#print lowest_comb_in_rest, lables
	if lowest_comb_in_rest:
	    return min(lowest_comb_in_rest, key=lowest_comb_in_rest.get),  min(lowest_comb_in_rest.values())
	return None, None
	


if __name__ == '__main__':
	total_data = {}
	multiple_list = []
	import sys
	app_obj = my_app(sys.argv[1])
	app_obj.get_data()
	label_lst = [i for i in sys.argv[2:][0:]]
	restaurant, prices = app_obj.check_single_rest(label_lst)
	#import pdb;pdb.set_trace()
	multuple_menu_cost = app_obj.check_multiple_rest(label_lst)
	#import pdb;pdb.set_trace()
	multi_rest, mult_price = None, None
	flag = False
	#import pdb;pdb.set_trace()
	if multiple_list:
	    multi_rest, mult_price = app_obj.minimun(multiple_list)
	    flag = True
	    if multuple_menu_cost:
		if multuple_menu_cost[1] < mult_price:
		    multi_rest, mult_price = multuple_menu_cost[0], multuple_menu_cost[1]
	elif multuple_menu_cost:
	    multi_rest, mult_price = multuple_menu_cost[0], multuple_menu_cost[1]
	    flag = True
        list_of_restaurants = []
	if restaurant and prices:
            list_of_restaurants.append((restaurant, prices))
	if multi_rest and mult_price and list_of_restaurants:
	    if float(mult_price) > float(list_of_restaurants[0][1]):
		flag = False
	if flag:
	    print int(multi_rest), float(mult_price)
        elif list_of_restaurants and not flag:
            print int(list_of_restaurants[0][0]), float(list_of_restaurants[0][1])
	else:
            print "Nil"




