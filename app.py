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
total_data = {}

class my_app(object):
    
    def __init__(self):
        fd = open("sample_data.csv",'r')
        lines = fd.readlines()
        lines = [[j.strip() for j in i.strip('\r\n').split(',')] for i in lines]

    def get_data(self):
        for item in lines:
            labels = [item[i] for i in range(2, len(item))]
            res_id = item[0]
            if res_id in total_data.keys():
                lst_of_tup_of_prices = total_data[res_id]
                lst_of_tup_of_prices.append((item[1], labels))
                total_data[res_id] = lst_of_tup_of_prices
            else:
                total_data[res_id] = [(item[1], labels)]
        #print total_data 

    def min_of(self, lst):
        import pdb;pdb.set_trace()
        print lst

if __name__ == '__main__':
    app_obj = my_app()
    import sys
    label_lst = sys.argv[2:]
    app_obj.min_of([i for i in sys.argv[2:][0:]])