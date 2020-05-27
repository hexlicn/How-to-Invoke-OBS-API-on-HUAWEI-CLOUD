import hashlib
import hmac
import binascii
from datetime import datetime
# from Passwd import AK, SK


SK = ''

httpMethod = "PUT"
contentType = "application/xml"

# ContentMD5 = 'EACIR9RFshIaQ5Rul7F8QA=='
ContentMD5 = ''
date = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
# date = 'Tue, 11 Feb 2020 02:58:13 GMT'
print(date)
canonicalizedHeaders = ''
# canonicalizedHeaders = "x-obs-acl:public-read"
# canonicalizedHeaders = "x-obs-acl:public-read\n"+'x-obs-storage-class:WARM\n'
# canonicalizedHeaders = r'x-obs-copy-source:/obs-iot-operation-quotas/analyze/output/application/01bf99be88044eeaab8272329b38c5c0/part-00000-01bf99be88044eeaab8272329b38c5c0-c000.csv' + '\n'
CanonicalizedResource = "/test-l00490846/"
canonical_string = httpMethod + "\n" + ContentMD5 + "\n" + contentType + "\n" + date + "\n" + canonicalizedHeaders + CanonicalizedResource
hashed = hmac.new(SK.encode('UTF-8'), canonical_string.encode('UTF-8'), hashlib.sha1)
encode_canonical = binascii.b2a_base64(hashed.digest())[:-1].decode('UTF-8')
print(canonical_string)
print(encode_canonical)

