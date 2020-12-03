from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from PIL import Image  

class Parse_News():

    newsItem = {
        "paragraphs":{
            
        }
    }

    def printNews(self):
        print(self.newsItem)

    def parse_news(self, doc):
        i = 0
        for para in doc.paragraphs:
            rels = para.part.rels
            newpara = {
                "text": para.text,
                "imgUrl": None,
                "imgTitle": None,
                "style": para.style.name,
            }   
            self.newsItem["paragraphs"][i] = newpara
            i += 1
        rels = document.part.rels
        print(self.newsItem)
        for rel in rels:
            if rels[rel].reltype == RT.HYPERLINK:
                print("link: ", rel, "url: ", rels[rel]._target)
        for image in document.inline_shapes:
            #print("hi")    
            print (image.height.cm, image.width.cm, image._inline.graphic.graphicData.pic.nvPicPr.cNvPr.name)

   

document = Document('Joulupuu - Christmas Tree Campaign 2020 at Espoo Campus until Dec 7.docx')
document.save('Joulupuu - Christmas Tree Campaign 2020 at Espoo Campus until Dec 7.docx')

parseNews = Parse_News()

parseNews.parse_news(document)
#parseNews.printNews()




