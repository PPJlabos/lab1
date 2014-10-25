import sys
print "a"



def citajUlaz():
    acc = []
    out = ''
    while True:
        try:
            acc.append(raw_input('')) # Or whatever prompt you prefer to use.
        except EOFError:
            out = '\n'.join(acc)
            break
    print out
    print acc

if __name__ == "__main__":
    print "helo"
    citajUlaz()