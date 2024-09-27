class Tasks:
    name = "";
    des = "";
    comp = False;

    def __init__(self, name, des, comp):
        self.name = name
        self.des = des
        self.comp = comp

    def get_name(self):
        return self.name
    def get_des(self):
        return self.des
    def get_comp(self):
        return self.comp

def add_task1(classn1, rep1, date1, name1):
    addclassn = classn1
    addrep1 = rep1
    adddate1 = date1
    addname1 = name1
    return addclassn,addrep1,adddate1,addname1

classn1 = ""
rep1: int = 0
date1 = ""
name1 = ""

task1 = Tasks(classn1,rep1,date1,name1)

while True:
    orr = input("Add to add task, remove to remove, update to update: ")
    
    if orr == "add":
        name1 = input("Name of Task? ")
        
        final = add_task1(classn1,rep1,date1,name1)
        
    print(final)
    break