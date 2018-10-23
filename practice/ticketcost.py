adult_cost=400
child_cost=adult_cost/2
no_of_adults=int(input('enter a no of adults:'))
no_of_childs=int(input('enter no of childs:'))
total_cost_of_adults=no_of_adults*adult_cost
total_cost_of_childs=no_of_childs*child_cost
discount_of_adults=total_cost_of_adults*0.05
discount_of_childs=total_cost_of_adults*0.07
if total_cost_of_adults>=1000:
    print('No of adults:',no_of_adults)
    print('dicount for adults:',discount_of_adults)
    print('total cost of ticket:',total_cost_of_adults-discount_of_adults)
else:
    print('No of adults:',no_of_adults)
    print('total cost of ticket',total_cost_of_adults)
print('=================================================================')
if total_cost_of_childs>=800:
    print('No of childs:',no_of_childs)
    print('dicount for childs:',discount_of_childs)
    print('total cost of ticket:',total_cost_of_childs-discount_of_childs)
else:
    print('No of childs:',no_of_childs)
    print('total cost of ticket',total_cost_of_childs)
