import easyocr

reader = easyocr.Reader(['en'])
result = reader.readtext('TEST_TEXT.png', detail = 0)
print(result)
