from tables import instruction_table, register_table
from binHex_converter import hex2bin, bin2hex

word_array = []
def assemble(instruction_array):
    for word_i,word in enumerate(instruction_array):
        for element_i,element in enumerate(word):
            instruction = instruction_array[word_i] 
            if element in register_table:
                instruction[element_i]=register_table[element]
            elif element in instruction_table:
                instruction[element_i]=instruction_table[element]['opcode']
                if instruction_table[element]['type'] == 'RFormat':
                    instruction.insert(len(instruction),'0x00') #add shamt
                    instruction.insert(len(instruction),instruction_table[element]['func'])
                    
    for word in instruction_array:
        output = ''
        for element in  word:
            output += element
        word_array.append(output)
    
    print(word_array)