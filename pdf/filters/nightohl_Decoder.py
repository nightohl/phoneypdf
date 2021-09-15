from PDFFilters import decodeStream
from binascii import a2b_hex

file = open("2filter_stream", 'br')
original_stream = file.read()

encoded_stream = decodeStream(original_stream, '/FlateDecode')[1]
#print(encoded_stream)

out = open("2filter_stream_decoded", "wb")
out.write(encoded_stream)