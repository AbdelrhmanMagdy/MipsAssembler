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
                    instruction.insert(len(instruction),'00') #add shamt
                    instruction.insert(len(instruction),instruction_table[element]['func'])
    # print(instruction_array)
    for word in instruction_array:
        output = ''
        if int(hex2bin(word[0],6))==0: #support R format
            output += hex2bin(word[0],6)
            output += hex2bin(word[2],5)
            output += hex2bin(word[3],5)
            output += hex2bin(word[1],5)
            output += hex2bin(word[4],5)
            output += hex2bin(word[5],6)
        word_array.append(output)
    
    # print(word_array)
    return word_array