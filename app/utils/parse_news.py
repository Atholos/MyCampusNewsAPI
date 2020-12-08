from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from PIL import Image  

class Parse_News():


    newsItem = {            
        "paragraphs":{
            
        }
    }
    def createArticle():
        article = {
            "id": self.article.id,
            "title": self.article.title,
            "author": {
                "id": self.author.id,
                "displayName": self.author.displayName,
                "email": self.author.email,
                "department": self.author.department,
                "jobtitle": self.author.jobtitle
            },
            "highlight": self.article.highlight,
            "description": self.article.description,
            "created_at": self.article.created_at.strftime("%d-%b-%Y (%H:%M:%S.%f)"),
            "headerImgUrl": self.headerurl,
            "headerImgTitle": self.headerImage.title,
            "paragraphs": self.dictparagraphs,
        }
        return article

    def printNews(self):
        print(self.newsItem)

    def parse_news(self, doc):
        i = 0
        image_paragraphs = []
        for para in doc.paragraphs:
            rels = para.part.rels
            newpara = {
                "text": para.text,
                "imgUrl": None,
                "imgTitle": None,
                "style": para.style.name,
            }
            if 'graphicData' in para._p.xml:
                image_paragraphs.append(para)   
            self.newsItem["paragraphs"][i] = newpara
            i += 1
        rels = document.part.rels
        print(image_paragraphs)
        print(self.newsItem)
        for rel in rels:
            if rels[rel].reltype == RT.HYPERLINK:
                print("link: ", rel, "url: ", rels[rel]._target)
        for image in document.inline_shapes:
            #print("hi")    
            print (image.height.cm, image.width.cm, image._inline.graphic.graphicData.pic.nvPicPr.cNvPr.name)

   
filename = 'Joulupuu - Christmas Tree Campaign 2020 at Espoo Campus until Dec 7.docx'
document = Document(filename)
document.save(filename)

parseNews = Parse_News()

parseNews.parse_news(document)
#parseNews.printNews()




