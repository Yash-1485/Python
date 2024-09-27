"""
Pattern Type - 1
*
**
***
****
*****
"""
def tr_pattern(type='1',limit=5,obj='*',mirror=False,bt_space='',bf_space=''):
    if type=='1' and mirror==False:
        for i in range(limit):
            for k in range(limit,i,-1):
                print(end=bf_space)
            for j in range(i+1):
                print(obj,end=bt_space)
            print()