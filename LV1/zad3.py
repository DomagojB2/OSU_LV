def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

list = []
while True:
    x =input()
    if (x.lower()=="done"):
        break
    if isfloat(x):
        list.append(float(x))
    else:
        print("Nije broj.")
print("Broj znamenki:", len(list))
print("Srednja vrijednost:", sum(list)/len(list))
print("Maksimalna vrijednost:", max(list))
print("Minimalana vrijednost", min(list))
list.sort()
print(list)