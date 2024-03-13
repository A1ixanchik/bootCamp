# with open('test.txt', 'r') as file:
#     print(file.tell())
#     data = file.read()
#     print(data, '!!')
#     print(file.tell())
#     file.seek(0)
#     data = file.read()
#     print(data, '!!')
#     print(file.tell())


with open('test.txt', 'w') as file:
    file.write('Hello world!\n')
    file.write('My name is John Snow \n')
    file.write(' I\'m Ned Starks bastard!f\n')
    file.seek(0)   
    data = ['Test 1 stroka\n', 'Test 2 stroka\n']
    file.writelines(data)

with open ('test.txt', 'a+')as f:
    f.write('\nJohn Snos is King of North!')
    f.write('\nYou know nothing John Snow!')
    f.seek(0)
    print(f.read())


# ===================
from PIL import Image
import pytesseract
import re
base_url = '/Users/KurmanbekovAlihan/Desktop/bootCamp/workWithFiles/'
 
def get_imei_codes(image_path:str):
    string = pytesseract.image_to_string(image_path)
    # print(string)
    list_of_imei = re.findall(r'IMEI\d.\s\d+', string)
    print(list_of_imei)

    with open('imei_codes.txt', 'w')as file:
        file.writelines(f'{x}\n'for x in list_of_imei)



image_path = base_url + 'imei.jpg'
get_imei_codes(image_path)