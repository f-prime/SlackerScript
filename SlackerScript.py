import sys
class SlackerScript:
    def __init__(self):
        try:
            self.file = sys.argv[1]
        except IndexError:
            print "Usage: python SlackerScript.py <file.slacker>"

        self.variables = {}
        self.keys = {

                "ADD":self.add,
                "SUBTRACT":self.subtract,
                "MULTIPLY":self.multiply,
                "DIVIDE":self.divide,
                "SAY":self.say,
                "FOR":self.forloop,
                "FOREVER":self.foreverloop,
                }
        self.endvars = False

    def main(self):
        with open(self.file, 'r') as source:
            for x in source.readlines():
                line = x.rstrip("\n")
                if line.startswith("#"):
                    continue
                if line == "END VARS":
                    self.endvars = True
                if self.endvars == False:
                    line = line.replace(" ", '')
                    var, equalsign, value = line.partition("=")
                    self.variables[var] = value
                 
                else:
                    try:
                        for key in self.keys:
                            if key in line:
                                self.keys[key](line)
                    except KeyError:
                        pass


    def add(self, line):
        line = line.split()[1].split(',')
        output = int(self.variables[line[0]]) + int(self.variables[line[1]])
        self.variables[line[0]] = output
        print output

    def subtract(self, line):
        line = line.split()[1].split(',')
        output = int(self.variables[line[0]]) - int(self.variables[line[1]])
        self.variables[line[0]] = output
        print output

    def multiply(self, line):
        line = line.split()[1].split(',')
        output = int(self.variables[line[0]]) * int(self.variables[line[1]])
        self.variables[line[0]] = output
        print output

    def divide(self, line):
        line = line.split()[1].split(',')
        output = int(self.variables[line[0]]) / int(self.variables[line[1]])
        self.variables[line[0]] = output
        print output

    def say(self, line):
        print ' '.join(line.split(" ")[1:])

    def forloop(self, line):
        line = line.replace("FOR:", '')
        line = line.split(" ")
        forrange = int(line[0])
        code = ' '.join(line[1:])
        for x in range(forrange):
            for key in self.keys:
                if key in code:
                    self.keys[key](code)
    def foreverloop(self, line):
        line = line.replace("FOREVER", '')
        line = line.split(" ")
        code = ' '.join(line[1:])
        while True:
            for key in self.keys:
                if key in code:
                    self.keys[key](code)

if __name__ == "__main__":
    try:
        SlackerScript().main()
    except KeyboardInterrupt:
        exit()
