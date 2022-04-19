"""
    Klavyeden küçük harflerle girilen bir cümlenin kelimelerini büyük-harfli/küçük-harfli şeklinde
    yeniden yazdıran program.
"""

from operator import indexOf


try:
    text = input('Enter a sentence with lowecase please: ')
    text_list = text.split(' ')
    new_word = ''
    new_text = ''

    print(text_list)
  

    for word in text_list:  
        flag = True
        for letter in word:
            if flag:
                new_word += letter.upper()
            else:
                new_word += letter.lower()

            flag = not flag

        new_text += new_word + ' '
        new_word = ''

except:
    print('Enter a valid value please.')

print(new_text)