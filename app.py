data = """1, 4.00, burger
1, 8.00, tofu_log
2, 5.00, burger
2, 6.50, tofu_log
3, 4.00, chef_salad
3, 8.00, steak_salad_sandwich
4, 5.00, steak_salad_sandwich
4, 2.50, wine_spritzer
5, 4.00, extreme_fajita
5, 8.00, fancy_european_water
6, 5.00, fancy_european_water
6, 6.00, extreme_fajita, jalapeno_poppers, extra_salsa
"""

__author__ = "mumin"

class my_app(object):
    
    def __init__(self):
        fd = open("sample_data.csv",'r')
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

    def prices_n_rest(self, label):
        for key in total_data.keys():
            #import pdb;pdb.set_trace()
            for item in total_data[key]:
                if label in item[1]:
                    return key, item[0]
        return None, None

    def min_of(self, lst):
        for label in lst:
            meta_data = self.prices_n_rest(label)
            print label, '\t:\t', meta_data

if __name__ == '__main__':
    app_obj = my_app()
    import sys
    total_data = {}
    app_obj.get_data()
    label_lst = sys.argv[2:]
    app_obj.min_of([i for i in sys.argv[2:][0:]])
