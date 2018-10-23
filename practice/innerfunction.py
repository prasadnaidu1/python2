def mobile(x):
    def sim():
        return 'IDEA'
    return 'mobile {} is inserted with sim{}'.format(x,sim())
#calling block
m=mobile('samsung')
print(m)