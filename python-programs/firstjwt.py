import jwt
key='Tasdfasdf34535234jn234kj234bnDFASDF32'
encoded=jwt.encode({'time':'12:10 pm', 'exp': 23423423423}, key, algorithm='HS256')
print(encoded)
decoded = jwt.decode(encoded,key, algorithms='HS256')
print(decoded)
