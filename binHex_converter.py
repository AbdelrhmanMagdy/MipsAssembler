def hex2bin(hex_val, num_bits):
    ''' Returns binary string of num_bits length of hex value (pos or neg)
    '''

    # Adjust for negative by performing Two's Complement (tc)
    tc = False
    if '-' in hex_val:
        tc = True
        hex_val = hex_val.replace('-', '')

    bit_string = '0' * num_bits
    bin_val    = str(bin(int(hex_val, 16)))[2:]
    bit_string = bit_string[0: num_bits - len(bin_val)] + bin_val + bit_string[num_bits:]

    # Two's complement if negative hex value
    if tc:
        tsubstring = bit_string[0:bit_string.rfind('1')]
        rsubstring = bit_string[bit_string.rfind('1'):]
        tsubstring = tsubstring.replace('1', 'X')
        tsubstring = tsubstring.replace('0', '1')
        tsubstring = tsubstring.replace('X', '0')
        bit_string = tsubstring + rsubstring

    return bit_string

def bin2hex(bit_string):
    bit_string = '0b'+bit_string
    hex_string = str(hex(int(bit_string, 2)))[2:]
    hex_string = hex_string.zfill(2)
    return hex_string

def intTo16Bin(strIn):
	# txt.replace('-','')
	# print(txt)
	if strIn[0]=='-':
		posTxt = strIn.replace('-','')
		# print(posTxt)
		x = '{0:016b}'.format(int(posTxt))
		for index,char in enumerate(x):
			if char=='0':
				x = x.replace('0','1',1)
			else:break
		return x
	else:
		return '{0:016b}'.format(int(strIn)) 
