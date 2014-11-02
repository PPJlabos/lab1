class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'





for i in range (1,21):
    original = open('testout\\'+str(i)+".out", "r")
    testing = open('tests_analizirano\\' + str(i) + '.out', 'r' )
    
    original_lines = []
    testing_lines = []
    for line in original:
        original_lines.append(line)
     
    for line in testing:
        testing_lines.append(line)
        
    print "file id: " + str(i),   
    if cmp(original_lines, testing_lines) == 0:
        print  'passed                        :)'
    else:
        print 'failed !!!!!                    :('