dic = {'1': [('2.00', ['A']), ('1.25', ['B']), ('2.00', ['C']), ('1.00', ['D']), ('3.00', ['A', 'B']), ('3.50', ['A', 'C']), ('2.50', ['A', 'D']), ('3.00', ['B', 'C']), ('2.00', ['B', 'D']), ('2.75', ['C', 'D']), ('3.75', ['A', 'B', 'C']), ('3.50', ['A', 'B', 'D']), ('4.00', ['A', 'C', 'D']), ('3.50', ['B', 'C', 'D']), ('5.00', ['A', 'B', 'C', 'D'])], '2': [('1.50', ['A']), ('2.00', ['B']), ('1.75', ['C']), ('2.50', ['A', 'B']), ('2.00', ['A', 'C']), ('2.25', ['A', 'D']), ('3.50', ['B', 'C']), ('3.25', ['B', 'D']), ('3.50', ['C', 'D']), ('2.00', ['A', 'B', 'D']), ('3.00', ['A', 'C', 'D'])]}


def check_this(key, label_found, price, label_items, value):
    total_price = price
    final_list = []
    for item in value:
	if set(item[1]).issubset(label_items) and len(item[1]) == len(label_items):
	    total_price = float(price) + float(item[0])
            #print "Total price incurred ", total_price, ' for combo ', item[1], ' and ', label_found
	    final_list.append([key, total_price])

import pdb;pdb.set_trace()
label_items = ['C', 'B', 'A', 'D']
for key, value in dic.iteritems():
    for index, item in enumerate(value):
	#print item[0], item[1], label_items
	if set(item[1]).issubset(label_items):
	    for i in item[1]:
	        label_items.remove(i)
	    check_this(key, item[1], item[0], label_items, value)
	    for i in item[1]:
	        label_items.append(i)
