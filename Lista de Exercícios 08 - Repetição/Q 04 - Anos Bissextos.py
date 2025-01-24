print ('Anos bissextos do ano 2000 até 3000: ')
for i in range(2000, 3000):
    if (i % 400 == 0) or ((i % 4 == 0) and (i % 100 != 0)):
        print (i)