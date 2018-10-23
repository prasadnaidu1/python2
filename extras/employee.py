class satyaemployee:
    company_name='satya technologies'
    contact_no=9052766763
    def __init__(self,idno,name=None,subjects=[]):
        self.idno=idno
        self.name=name
        self.subjects=subjects
    def display(self):
        print('company name:',satyaemployee.company_name)
        print('company contact number:',satyaemployee.contact_no)
        print('idno: ', self.idno)
        print('name: ', self.name)
        print('faculty subjects')
        for x in self.subjects:
            print(x)
