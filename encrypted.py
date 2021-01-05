import base64

msg = 'AkgUEA0TBAEWTEgKEx4eHQIEGldNUkIIB1xfXBgIEgBJUFtSQg4bRFZcFAoDQkJQRhcDDQdCR0pe T11FSRkPERcODFlRVRxIS0VJEQIaDA4eVV5cFxtARVRQRgcLBwdTWFwdSEtFSQIAEAcCHEMUGUNP QBYPFgRVSUtPVlxWXk9dRUkHCBxETBU= '

my_eyes = str.encode('yogenparekh039')
decoded = base64.b64decode(msg)
decrypted = ''

for i in range(0, len(decoded)):
	a = my_eyes[i%len(my_eyes)]
	b = decoded[i]
	decrypted += chr(a ^ b)

print(decrypted)