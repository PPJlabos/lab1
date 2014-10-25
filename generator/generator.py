import sys
import json




def regexGen(ulaz):
    reg_dict = {}
    regs = ulaz.split('%X')[0]
    reglist = regs.split('\n')
    for reg in reglist:
        _key = reg.split(" ")
        try:
            reg_dict[_key[0]] = _key[1]#.split("|")
        except IndexError:
            pass
    return reg_dict

def citajUlaz():
    acc = []
    out = ''
    while True:
        try:
            acc.append(raw_input('')) # Or whatever prompt you prefer to use.
        except EOFError:
            out = '\n'.join(acc)
            break
    return out

def prijelazGen(ulaz):
    
    for pravilo in ulaz.split('%L')[1].split('\n')[2:]:
        print pravilo
  
    
    
    

def saveToFile(fileName, data):
    output = open(fileName, 'w')
    json.dump(data, output)
    output.close()

def loadFile(fileName):
    input = open (fileName, 'r')
    return json.loads(fileName)[0]

def generator():
    regs = {}
    newregs = {}
    prijelazi = {}
    ulaz = ''
    ulaz = citajUlaz() # dohvati podatke s stdin
    regs = regexGen(ulaz)
    prijelazGen(ulaz)
    print ""
    
    print ""
   
    for key in regs.keys():
        print regs[key]
        print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    print regs.keys()
if __name__ == "__main__":
    generator()