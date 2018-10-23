from abc import ABC,abstractmethod
class wholesale(ABC):
    @abstractmethod
    def retailer(self):
        pass
class girlshop(wholesale):
    shopname='meenakshi silk store'
    shopaddress='hyderabad'
    pattu_sarees=3000
    banaras_sarees=2000
    dharmavaram_sarees=3000
    mangalagiri_sarees=3500
    bombaycotton_sarees=4500
    def retailer(self):
        self.sarees=input('enter saree name')
        self.no_of_items=int(input('enter no of items:'))
        self.discount_on_pattu_sarees=(self.no_of_items+girlshop.pattu_sarees)*0.05
        self.discount_on_banaras_sarees=(self.no_of_items+girlshop.banaras_sarees)*0.03
        self.discount_on_dharmavaram_sarees=(self.no_of_items+girlshop.dharmavaram_sarees)*0.08
        self.discount_on_mangalagiri_sarees = (self.no_of_items + girlshop.mangalagiri_sarees)* 0.10
        self.discount_on_bombaycotton_sarees = (self.no_of_items + girlshop.bombaycotton_sarees) * 0.15
    def dispaly(self):
        if self.sarees == 'pattu_sarees':
            print('no of items:', self.no_of_items)
            print('discount on pattu sarees:', self.discount_on_pattu_sarees)
            print('total cost of pattusarees:', girlshop.pattu_sarees + self.discount_on_pattu_sarees)
        else:
            pass

        if self.sarees == 'banaras_sarees':
            print('no of items:', self.no_of_items)
            print('discount on pattu sarees:', self.discount_on_banaras_sarees)
            print('total cost of pattusarees:', girlshop.banaras_sarees + self.discount_on_banaras_sarees)
        else:
            pass

        if self.sarees == 'dharmavaram_saree':
            print('no of items:', self.no_of_items)
            print('discount on pattu sarees:', self.discount_on_dharmavaram_sarees)
            print('total cost of pattusarees:', girlshop.dharmavaram_sarees + self.discount_on_pattu_sarees)
        else:
            pass
        if self.sarees == 'magalagiri_sarees':
            print('no of items:', self.no_of_items)
            print('discount on pattu sarees:', self.discount_on_mangalagiri_sarees)
            print('total cost of pattusarees:', girlshop.mangalagiri_sarees + self.discount_on_mangalagiri_sarees)
        else:
            pass

        if self.sarees == 'bombaycotton_sarees':
            print('no of items:', self.no_of_items)
            print('discount on pattu sarees:', self.discount_on_bombaycotton_sarees)
            print('total cost of pattusarees:', girlshop.bombaycotton_sarees + self.discount_on_bombaycotton_sarees)
        else:
            pass


class boysshop(wholesale):
    silk_shirts=1000
    cotton_shirts=1900
    buffello_shirts=2500
    def retailer(self):
        self.shirt_name=input('enter shirt name:')
        self.no_of_items=int(input('enter no of items:'))
        self.discount_on_silk_shirts=(self.no_of_items+boysshop.silk_shirts)*0.05
        self.discount_on_cotton_shirts=(self.no_of_items+boysshop.cotton_shirts)*0.08
        self.discount_on_buffello_shirts = (self.no_of_items + boysshop.buffello_shirts)*0.10
    def show(self):

        if self.shirt_name=='silk_shirts':
            print('shirt name:',self.shirt_name)
            print('no of shirts',self.no_of_items)
            print('dicount on silk shirts:',self.discount_on_silk_shirts)
            print('Total cost of silk shirt:',self.silk_shirts+self.discount_on_silk_shirts)
        else:
            pass
        if self.shirt_name == 'cotton_shirts':
            print('shirt name:', self.shirt_name)
            print('no of shirts', self.no_of_items)
            print('dicount on silk shirts:', self.discount_on_cotton_shirts)
            print('Total cost of cotton shirt:', self.cotton_shirts + self.discount_on_cotton_shirts)
        else:
            pass
        if self.shirt_name == 'buffello_shirts':
            print('shirt name:', self.shirt_name)
            print('no of shirts', self.no_of_items)
            print('dicount on buffello shirts:', self.discount_on_buffello_shirts)
            print('Total cost of buffello shirt:', self.buffello_shirts + self.discount_on_buffello_shirts)
        else:
            pass

g=girlshop()
g.retailer()
print('shop name:',girlshop.shopname)
print('shop address:', girlshop.shopaddress)
g.dispaly()
print('amount paid')
print('Thanks you for making shoping')
print('==================================================')
b=boysshop()
print('shop name:',girlshop.shopname)
print('shop address:', girlshop.shopaddress)
b.retailer()
b.show()













