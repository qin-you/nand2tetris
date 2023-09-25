import sys
import os
import pdb


class Assembler:
    def __init__(self, parser, coder, symbol_table) -> None:
        self.parser = parser
        self.coder = coder
        self.symbol_table = symbol_table        
    
    def compile(self, asmfile:str):
        hacklist = []
        pc = -1
        varaddr = 16
        
        with open(asmfile, "r") as f:
            lines = f.readlines()

        #first scan : get label symbols
        for line in lines:
            newline = self.parser.parse(line)
            if not newline:
                continue            
            if self.parser.type == 'L':
                self.symbol_table.add(self.parser.asmlabel, pc+1)
            else:
                pc += 1
            
            
        # second scan : get variable symbols and compile
        for line in lines:
            newline = self.parser.parse(line)
            if not newline:
                continue
            
            if self.parser.type == 'A' and not s2i(self.parser.Avalue) and not self.symbol_table.contain(self.parser.Avalue):
                self.symbol_table.add(self.parser.Avalue, varaddr)
                varaddr += 1

            if self.parser.type != 'L':
                # transfer to binary
                binary = self.coder.code(line, self.parser, self.symbol_table)
                hacklist.append(binary)
            
        # save result
        dirname = os.path.dirname(asmfile)
        basename = os.path.basename(asmfile)
        purename = basename.split('.')[0]
        
        savefile = dirname + '/' + purename + ".hack"
        with open(savefile, "w") as f:
            for line in hacklist:
                f.write(line+'\n')


class Parser:
    '''in asm space, split fields'''
    def __init__(self) -> None:
        self.init()
        
    def init(self) -> None:
        self.type = ''      # A C L instruction
        self.Avalue = ''    # A
        self.asmdest = ''   # C
        self.asmcomp = ''   # C
        self.asmjump = ''   # C
        self.asmlabel = ''  # L
        
        
    def parse(self, line:str) -> int:
        line = line.strip()
        if not line or line.startswith("//"):
            return 0
        
        # del comments end of line
        tmp = line.split("//")
        line = tmp[0].strip()
        
        self.init()
        
        if line.startswith('@'):
            self.type = 'A'
            self.parseA(line)
        elif line.startswith('('):
            # label
            self.type = 'L'
            self.parseL(line)
        else:
            # C-instruction
            self.type = 'C'
            self.parseC(line)
        
        return line

    def parseA(self, line:str) -> None:
        self.Avalue = line[1:]
    
    def parseC(self, line:str) -> None:
        tmp = line.split(";")
        if len(tmp) == 2:
            self.asmjump = tmp[1]
        tmp = tmp[0].split('=')
        if len(tmp) == 1:
            self.asmcomp = tmp[0]
        else:
            self.asmdest = tmp[0]
            self.asmcomp = tmp[1]

    def parseL(self, line:str) -> None:
        self.asmlabel = line[1:-1]


class Coder:
    def __init__(self) -> None:
        pass

    def code(self, line, parser, table) -> str:
        if parser.type == 'A': 
            return self.codeA(line, parser, table)
        else:
            return self.codeC(line, parser, table)
        
    def codeA(self, line, parser, table):
        tmp = 0
        if s2i(parser.Avalue):
            addr = create_addr15(parser.Avalue)
        else:
            addr = table.table[parser.Avalue]
        
        return '0' + addr
    
    def codeC(self, line, parser, table):
        binary = '111'
        binary += self.comp(parser.asmcomp)
        binary += self.dest(parser.asmdest)
        binary += self.jump(parser.asmjump)
        return binary
    
    
    def dest(self, asmdest):
        bin = ['0', '0', '0']
        if asmdest is None:
            return ''.join(bin)
        if 'A' in asmdest:
            bin[0] = '1'
        if 'D' in asmdest:
            bin[1] = '1'
        if 'M' in asmdest:
            bin[2] = '1'
        return ''.join(bin)

    def comp(self, asmcomp):
        comp_dict = {
            '0': '101010',
            '1': '111111',
            '-1': '111010',
            'D': '001100',
            'A': '110000',
            '!D': '001101',
            '!A': '110001',
            '-D': '001111',
            '-A': '110011',
            'D+1': '011111',
            'A+1': '110111',
            'D-1': '001110',
            'A-1': '110010',
            'D+A': '000010',
            'D-A': '010011',
            'A-D': '000111',
            'D&A': '000000',
            'D|A': '010101',
        }
        a_bit = '0'
        if 'M' in asmcomp:
            a_bit = '1'
        asmcomp = asmcomp.replace('M', 'A')
        c_bit = comp_dict.get(asmcomp, '000000')
        return a_bit + c_bit
    
    
    def jump(self, asmjump):
        jump_dict = {
            'JGT': '001',
            'JEQ': '010',
            'JGE': '011',
            'JLT': '100',
            'JNE': '101',
            'JLE': '110',
            'JMP': '111',
        }
        return jump_dict.get(asmjump, '000')


class SymboleTable:
    def __init__(self) -> None:
        self.table = self.base_table()
        
    def add(self, key:str, value:str):
        self.table[key] = create_addr15(value)
        
    def contain(self, key) -> bool:
        if key in self.table: 
            return True
        return False
        
    def base_table(self): # 15 bit addresses, 32K locations
        return {
             'SP': '000000000000000',
            'LCL': '000000000000001',
            'ARG': '000000000000010',
           'THIS': '000000000000011',
           'THAT': '000000000000100',
             'R0': '000000000000000',
             'R1': '000000000000001',
             'R2': '000000000000010',
             'R3': '000000000000011',
             'R4': '000000000000100',
             'R5': '000000000000101',
             'R6': '000000000000110',
             'R7': '000000000000111',
             'R8': '000000000001000',
             'R9': '000000000001001',
            'R10': '000000000001010',
            'R11': '000000000001011',
            'R12': '000000000001100',
            'R13': '000000000001101',
            'R14': '000000000001110',
            'R15': '000000000001111',
         'SCREEN': '100000000000000',
            'KBD': '110000000000000',
        }
    
    

def create_addr15(s) -> str:
    address = '{0:b}'.format(int(s))
    base = (15 - len(address)) * '0'
    return base + address


def s2i(s:str) -> int:
    ''' if s can transfer to a num. return true/false'''
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True


if __name__ == "__main__":
    # pdb.set_trace()

    asmfile = sys.argv[1]
    assembler = Assembler(Parser(), Coder(), SymboleTable())
    assembler.compile(asmfile)
    

    
