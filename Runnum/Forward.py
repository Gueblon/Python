import string
import random
import os

def randompassword():
  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
  size = random.randint(9, 10)
  return ''.join(random.choice(chars) for x in range(size)) +'1'
#--------------------------------------------

def did126 (lsclient, obj):
    sbc = '192.168.128.91'
    z = [lsclient+';'+row+';A'+lsclient+row+';'+sbc for row in obj]
    with open(os.path.dirname(__file__)+"/did.csv", 'w') as f:
        f.write("Personal_account;Account_id;DID;IP\n")
    with open(os.path.dirname(__file__)+"/did.csv", 'a') as f:
        for row in z:
            f.write(row + '\n')
#-----------------------------------------

def add126(ls, obj, product, batch):
    routing_plan = '3732'
    z = [ls+';'+row+';'+randompassword()+';'+product+';Credit;;'+batch+';'+routing_plan for row in obj]
    with open(os.path.dirname(__file__)+"/add.csv", 'w') as f:
        f.write("LS;Account;Password;Product;Type(Debit/Credit);Credit_limit;Batch;Routing_plan\n")
    with open(os.path.dirname(__file__)+"/add.csv", 'a') as f:
        for row in z:
            f.write(row + '\n')
#-----------------------------------------

def num (obj):
    with open(os.path.dirname(__file__)+"/num.csv", 'w') as f:
        f.write("Nums\n")
    with open(os.path.dirname(__file__)+"/num.csv", 'a') as f:
        for row in obj:
            f.write(row+'\n')
#-------------------------------------------------

try:
    with open(os.path.dirname(__file__)+"/numbers.txt") as f:
        x = [line.strip() for line in f]
    with open(os.path.dirname(__file__)+"/info.txt") as f2:
        z = [line.strip() for line in f2]
    ls = z[0] #number of LS
    print(ls + ' - LS')
    product = z[1] #product for add
    print(product + '- product')
    batch = z[2] #batch for add
    print(batch + '- batch')
    y = list(filter(lambda x: len(x) == 14 or len(x) == 11, x))
    assert (x == y)
    num(y)
    did126(ls, y)
    add126(ls, y, product, batch)

except:
    print("Проверь файлы")
