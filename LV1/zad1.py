def total_euro(sati, satnica):
    return float(sati)*float(satnica)

print ('Radni sati: ')
sati = input()
print('eura/h: ')
satnica = input()
total = total_euro(sati, satnica)
print ("Radni sati:",sati,"h \neura/h:",satnica,"\nUupno:",total,"eura")