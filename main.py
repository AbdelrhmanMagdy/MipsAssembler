
import sys
import assembly_parser, assembler
def usage():
    print 'Usage: '+sys.argv[0]+' -i <file1>'
    sys.exit(1)

def main(argv):
    files = argv
    if len(files) is not 1:
        usage()
    for filename in files:
        myFile        = open(filename)
        instructions  = myFile.readlines()
        instruction_array = assembly_parser.parse(instructions)
        output        = assembler.assemble( instruction_array )


if __name__ == '__main__':
    main(sys.argv[1:])

