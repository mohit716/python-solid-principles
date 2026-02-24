# copy characters from keyboard to printer 

import sys

class Keyboard:
    def read(self):
        # read 1 character from stdin (keyboard)
        c = sys.stdin.read(1)
        if c == "":   # EOF in Python comes as empty string
            return none
        return c

class Printer:
    def write(self, c):
        # Write 1 charater to stdout (pretend this is a printer device)
        sys.stdout.write(c)
        sys.stdout.flush()

def main():
    keyboard = Keyboard() # hard-coded dependency
    printer = Printer()  # hard-coded dependency

    while True:
        c = keyboard.read()  # directly depends on keyboard
        if c is None:  # EOF
            break
        printer.write(c)

if __name__ == "__main__":
    main()



# keyboard:
## read

#printer
## write

class reader
    abastract def read :void;

class writer:
    abastradt def write: void
    

class keyboard implements reader():


Main:
    Reader reader = new keyboard


