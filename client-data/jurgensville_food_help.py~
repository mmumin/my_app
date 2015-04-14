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
	import pdb;pdb.set_trace()
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


    def check_this(self, key, label_found, price, label_items, value):
        total_price = price
        final_list = []
        for item in value:
	    if set(item[1]).issubset(label_items) and len(item[1]) == len(label_items):
	        total_price = float(price) + float(item[0])
                #print "Total price incurred ", total_price, ' for combo ', item[1], ' and ', label_found
	        self.final_list.append([key, total_price])

    def check_minimum(self, label_items, data_dict):
        #label_items = ['C', 'B', 'A', 'D']
        for key, value in data_dict.iteritems():
            for index, item in enumerate(value):
	        if set(item[1]).issubset(label_items):
                    for i in item[1]:
                        label_items.remove(i)
                        self.check_this(key, item[1], item[0], label_items, value)
                    for i in item[1]:
                        label_items.append(i)


    def check_multiple_rest(self, items_label):
	label_list = [i for i in items_label]
	data_dict = {}
	for key, value in total_data.iteritems():
	    for each in value:
		for item in items_label:
	            if set([item]).issubset(each[1]):
		        label_list.remove(item)
		        if not key in data_dict.keys():
			    data_dict[key] = [each]
        		else:
			    old_data = data_dict[key]
			    old_data.append(each)
			label_list.append(item)
	data_dict = self.remove_identical(data_dict)
	#print data_dict
	self.final_list = []
	self.check_minimum(items_label, data_dict)
	import pdb;pdb.set_trace()
	print self.final_list


if __name__ == '__main__':
	total_data = {}
	import sys
	app_obj = my_app(sys.argv[1])
	app_obj.get_data()
	label_lst = [i for i in sys.argv[2:][0:]]
	restaurant, prices = app_obj.check_single_rest(label_lst)
	app_obj.check_multiple_rest(label_lst)
	import pdb;pdb.set_trace()
	multi_rest, mult_price = app_obj.minimun(app_obj.final_list)
        list_of_restaurants = []
	if restaurant and prices:
            list_of_restaurants.append((restaurant, prices))
	flag = False
	if multi_rest and mult_price and list_of_restaurants:
	    if float(mult_price) < float(list_of_restaurants[0][1]):
		flag = True
	if flag:
	    print int(multi_rest), float(mult_price)
        elif list_of_restaurants and not flag:
            print int(list_of_restaurants[0][0]), float(list_of_restaurants[0][1])
	else:
            print "Nil"

