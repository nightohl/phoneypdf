import sys
from PDFFilters import encodeStream, decodeStream
from binascii import a2b_hex

def convertFilterNumToFilter(filterNum):
    '''
		convert filter number to filter string

		@param filterNum: Filter number to convert
             1 : '/ASCIIHexDecode'
             2 : '/ASCII85Decode'
             3 : '/LZWDecode'
             4 : '/FlateDecode'
             5 : '/RunLengthDecode'
             6 : '/CCITTFaxDecode'
             7 : '/JBIG2Decode'
             8 : '/DCTDecode'
             9 : '/JPXDecode'
            10 : '/Crypt'
        @return: valid filter string or None
	'''
    if filterNum == '1':
            return '/ASCIIHexDecode'
    elif filterNum == '2':
            return '/ASCII85Decode'
    elif filterNum == '3':
            return '/LZWDecode'
    elif filterNum == '4':
            return '/FlateDecode'
    elif filterNum == '5':
            return '/RunLengthDecode'
    elif filterNum == '6':
            return '/CCITTFaxDecode'
    elif filterNum == '7':
            return '/JBIG2Decode'
    elif filterNum == '8':
            return '/DCTDecode'
    elif filterNum == '9':
            return '/JPXDecode'
    elif filterNum == '10':
            return '/Crypt'
    else:
        return None

def encoder(path, filterNum, parameters={}):
    '''
		Encode the given file
		
		@param path: file path to encode
		@param filterNum: Filter number to apply to encode the streams
             1 : '/ASCIIHexDecode'
             2 : '/ASCII85Decode'
             3 : '/LZWDecode'
             4 : '/FlateDecode'
             5 : '/RunLengthDecode'
             6 : '/CCITTFaxDecode'
             7 : '/JBIG2Decode'
             8 : '/DCTDecode'
             9 : '/JPXDecode'
            10 : '/Crypt'
        @param parameters: List of PDFObjects containing the parameters for the filter
	'''
    file = open(path, 'br')
    original_stream = file.read()
    
    filter = convertFilterNumToFilter(filterNum)
    if filter != None:
        encoded_stream = encodeStream(original_stream, filter)[1]
        out = open(path+"_encoded", "wb")
        out.write(encoded_stream)
    else:
        print("filter is not correct")
        sys.exit()

def decoder(path, filterNum, parameters={}):
    '''
		Decode the given file
		
		@param path: file path to decode
		@param filterNum: Filter number to apply to decode the streams
             1 : '/ASCIIHexDecode'
             2 : '/ASCII85Decode'
             3 : '/LZWDecode'
             4 : '/FlateDecode'
             5 : '/RunLengthDecode'
             6 : '/CCITTFaxDecode'
             7 : '/JBIG2Decode'
             8 : '/DCTDecode'
             9 : '/JPXDecode'
            10 : '/Crypt'
        @param parameters: List of PDFObjects containing the parameters for the filter
	'''
    file = open(path, 'br')
    original_stream = file.read()

    filter = convertFilterNumToFilter(filterNum)
    if filter != None:
        encoded_stream = decodeStream(original_stream, filter, parameters)[1]
        out = open(path+"_decoded", "wb")
        out.write(encoded_stream)
    else:
        print("filter is not correct")
        sys.exit()

def usage():
    print("[*] Usage ------------\n")
    print(" $ python nightohl_EnDecoder.py path method filterNum [parameters]\n")
    print(" - path : filepath to encode or decode")
    print(" - method : what to do")
    print("\t -e : encode")
    print("\t -d : decode")
    print(" - filterNum : select filter nubmer")
    print(" - parameters : optional parameter for List of PDFObjects containing the parameters")
    print("\t  1 : '/ASCIIHexDecode'")
    print("\t  2 : '/ASCII85Decode'")
    print("\t  3 : '/LZWDecode'")
    print("\t  4 : '/FlateDecode'")
    print("\t  5 : '/RunLengthDecode'")
    print("\t  6 : '/CCITTFaxDecode'")
    print("\t  7 : '/JBIG2Decode'")
    print("\t  8 : '/DCTDecode'")
    print("\t  9 : '/JPXDecode'")
    print("\t 10 : '/Crypt'")
    print("\n[*] ------------------")

if len(sys.argv) < 4:
    usage()
    sys.exit()

path = sys.argv[1]
method = sys.argv[2]
if method != '-e' and method != '-d':
    print("method choice is not correct")
    print("'-d' : decode\n'-e' : encode")
    sys.exit() 
filterNum = sys.argv[3]

if len(sys.argv) == 5:
    parameters = sys.argv[4]
    if method == '-e':
        encoder(path, filterNum, parameters)
    elif method == '-d':
        decoder(path, filterNum, parameters)
else:
    if method == '-e':
        encoder(path, filterNum)
    elif method == '-d':
        decoder(path, filterNum)