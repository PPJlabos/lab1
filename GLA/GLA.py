import regex_gen_automata  # import state machine generator from regular expresison
from regex import *

def generiraj_lex_automat():
    # read every line in the file
    while line < len(file)):
        state_definition = ""
        state_counter = 0
        # check the state list for state in the list
        for state in states:

            if "<"+state+">" in file[line]:
                    state_definition = file[line]
                    # dopuni ostatak regularnih izraza  zamjenom kljuceva
                    for key in regex.keys():
                        if key in state_definition:
                            state_definition = state_definition.replace(key, "("+regex[keys]+")")
                    break
        try:
            directive = []
            line = line + 1
            while file[line].strip() != "}":
                directive.append(file[line])
                line = line + 1

            automat[state_definition] = directive
            state_counter = state_counter + 1
        except IndexError:
            pass
    return states


def ucitaj_ulaz():
    file = ""
    input_lines = []

    while True:
        try:
            input_lines.append(raw_input())
        except EOFError:
            file = '\n'.join(input_lines)
            break

    print file

    for line in range(len(input_lines)):

        if
