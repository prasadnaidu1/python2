class hospital:
    hospital_name='ramana clinic'
    hospital_address='hyderabad,08561244666'
    cold=200
    calf=250
    fever=500
    headache=100
    other=1000
    def doctor(self):
        self.diesease=input('enter your diesease:')
        if self.diesease=='cold':
            print('the doctor fee is:',hospital.cold)
        else:
            pass
        if self.diesease=='colf':
            print('the doctor fee is:', hospital.calf)
        else:
            pass
        if self.diesease == 'fever':
            print('the doctor fee is:', hospital.fever)
        else:
            pass
        if self.diesease == 'other':
            print('the doctor fee is:', hospital.other)
        else:
            pass
class patient(hospital):
    def department(self):
        pass
p=patient()
p.doctor()
p.department()

'''
print('no of items:',self.no_of_items)
        print('total cost of pattusarees:',girlshop.pattu_sarees+self.discount_on_pattu_sarees)
        print('total cost of banrassarees:', girlshop.banaras_sarees+ self.discount_on_banaras_sarees)
        print('total cost of dharmavaramsarees:', girlshop.dharmavaram_sarees + self.discount_on_dharmavaram_sarees)
        print('total cost of pattusarees:', girlshop.pattu_sarees + self.discount_on_pattu_sarees)
        print('total cost of magalagirisarees:', girlshop.mangalagiri_sarees + self.discount_on_mangalagiri_sarees)
        print('total cost of bombaycottonsarees:', girlshop.bombaycotton_sarees + self.discount_on_bombaycotton_sarees)
'''
#cottonshitrs




