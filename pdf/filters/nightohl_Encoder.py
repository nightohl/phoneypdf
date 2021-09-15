from PDFFilters import encodeStream
from binascii import a2b_hex

file = open("stream", 'br')
original_stream = file.read()

encoded_stream = encodeStream(original_stream, '/FlateDecode')[1]
#print(encoded_stream)

out = open("encodedStream", "wb")
out.write(encoded_stream)