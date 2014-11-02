def ucitaj_file(file_name):
    list = []
    input_file = open(file_name, 'r')
    for line in input_file:
        list.append(line.strip)
    return list
    
    
def usporedi(original, test_file):
    if (cmp(original, test_file) == 0):
        print "pass                                     :)"
    else:
        print test_file
        
       
