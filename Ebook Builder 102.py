from lxml import html
import requests, docx
i=1872
mydoc=docx.Document()
while i<2300:
    page= requests.get("https://goblinsguide.com/versatile-mage/versatile-mage-chapter-"+str(i))
    tree= html.fromstring(page.content)
    '''print(tree)'''
    texta=tree.xpath('//p/text()')
    print(texta)

    
    head=texta[0]
    print(head)
    mydoc.add_heading(head,level=1)
    mydoc.add_paragraph(texta)
    mydoc.add_paragraph("            ")
    mydoc.add_paragraph("            ")


    i=i+1
mydoc.save("Epub.docx")