fo1 = open('C:/Users/amaheshwar24/Documents/pythontraining/chunks', 'wb')
for i in range(0, 5761):
    fo2 = open('C:/Users/amaheshwar24/Documents/pythontraining/chunks' + str(i) + '.jpg', 'rb')
    for line in fo2:
        line.read()
fo1.close()
