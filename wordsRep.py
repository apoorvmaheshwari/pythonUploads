fin = open("C:/Users/amaheshwar24/Documents/pythontraining/data.txt", "rt")
fout = open("out.txt", "wt")
li = ["vacation", "party", "outhouse"]
for line in fin:
    fout.write(line.replace('python', '******'))

fin.close()
fout.close()
