def ucitajUlaz():
    inputs = []
    # procitaj ulaznu datoteku definicije jezika, spremi svaki red kao novi clan liste inputs
    while True:
        try:
            inputs.append(raw_input())
        except EOFError:
            break
    return inputs
    
    
def ispisi_stanja():
    inputs = ucitajUlaz()
 
    for input in inputs:
        if "<" in input:
            print input
if __name__ == "__main__":
    ispisi_stanja()