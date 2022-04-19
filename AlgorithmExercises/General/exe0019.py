"""
    Klavyeden küçük harflerle girilen bir cümlede kelimelerin sadece ilk harflerini büyütüp
    yeniden yazdıran program.
"""

new_text = ''

sentence = input('Enter a sentence please: ')

words_in_sentence = sentence.split(' ')

for i in words_in_sentence:
    new_text += i.capitalize() + ' '

print(new_text)


