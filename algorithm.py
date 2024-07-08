stakes = {'50':45, '100':40, '200':30, '500':100, '1000':50, '2500':400, '5000':150}
# print(list(stakes.keys())[0])
var = list('50.89%')
new_var = ''
del var[-1]
for i in var:
    new_var += i
print(new_var)
new_var = float(new_var)
print(new_var / 100)
