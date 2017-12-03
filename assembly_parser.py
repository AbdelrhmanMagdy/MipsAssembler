def parse(input_lines):
    instruction_array=[]
    for line in input_lines:
        instruction = line.strip().replace(' ',',',1)
        instruction = instruction.replace(' ','').split(',')
        instruction_array.append(instruction)
    return instruction_array