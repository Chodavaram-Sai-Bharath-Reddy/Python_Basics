import pytesseract
import cv2
from bs4 import BeautifulSoup

img = cv2.imread("testImg1.jpg")
text = pytesseract.image_to_string(img)
para = text.split("\n")
print(para)

initial_html = """
<html>
    <head>
        <title>My New HTML Document</title>
    </head>
    <body>
    </body>
</html>
"""
soup = BeautifulSoup(initial_html, 'html.parser')
txt = ""

new_heading = soup.new_tag('h1')
j = 0

for i in range(len(para)):
    if para[i] != '':
        if para[i-1] != '':
            txt+=' '+para[i]
        else:
            txt+=para[i]
    else:
        if j != 0:
            new_paragraph = soup.new_tag('p')
            new_paragraph.string = txt
            soup.body.append(new_paragraph)
            txt = ''
        else:
            new_heading.string = txt
            soup.body.append(new_heading)
            element = soup.find('title')
            element.string = txt
            txt = ''
            j+=1


with open('test.html', 'w', encoding='utf-8') as file:
    file.write(str(soup.prettify()))
