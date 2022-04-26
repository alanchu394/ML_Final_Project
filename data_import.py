import eng_to_ipa as ipa
file = open('words.txt','r')
lines = file.readlines()
file.close()

file = open('data.csv','w')
count = 0
file.write('word,pronunciation\n')
for word in lines:
    if(count == 100):
        break
    if ipa.isin_cmu(word):
        line = word.strip('\n') + ',' + ipa.convert(word) + '\n'
        file.write(line)
    count +=1
file.close()