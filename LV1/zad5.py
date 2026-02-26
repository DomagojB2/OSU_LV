fhand = open("SMSSpamCollection.txt", encoding="utf-8")
ham_caunt = 0
ham_words = 0
spam_count = 0
spam_words = 0
usklicnik = 0
for line in fhand:
    label, massage = line.split(None, 1)
    if label == "ham":
        ham_caunt += 1
        ham_words += len(massage.split())
    elif label == "spam":
        spam_count += 1
        spam_words += len(massage.split())
        if massage.strip().endswith("!"):
            usklicnik += 1
fhand.close()
print("Prosjecan broj ham poruka:", int(ham_words/ham_caunt))
print("Prosjecan broj spam poruka:", int(spam_words/spam_count))
print("Usklicnici na kraju spam poruka:", usklicnik)