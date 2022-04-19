"""
    Klavyeden girilen bir cümlede, kaç tane a ile biten kelime olduğunu bulan program.
"""

sentence = input('Enter a sentence please : ')
sentence_list = sentence.split(' ')

count = 0
for i in sentence_list:
    if(i[-1].lower() == 'a'):
        count += 1

print(count)
