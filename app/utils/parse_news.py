from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from PIL import Image  

class Parse_News():

    title = "This is article title"
    description = "this is news parser"
    highlight = False
    headerImgUrl = "header Url"
    headerImageTitle = "header image title"

    author = {
                "displayName": "This is display name",
                "email": "this is email",
                "department": "this is department",
                "jobtitle": "this is job title"
            }

    paragraphs = {}

    newsItem = {            
        "paragraphs":{
            
        }
    }
    image = {
        "filename": "image filename",
        "height": "image height",
        "width": "image width" 
    }

    def createArticle():
        article = {
            "title": self.article.title,
            "author": {
                "displayName": self.author["displayName"],
                "email": self.author["email"],
                "department": self.author["department"],
                "jobtitle": self.author["jobtitle"]
            },
            "highlight": self.highlight,
            "description": self.description,
            "headerImgUrl": self.headerurl,
            "headerImgTitle": self.headerImageTitle,
            "paragraphs": self.paragraphs,
        }
        return article

    def printNews(self):
        print(self.newsItem)

    def parse_news(self, doc):
        i = 0
        image_paragraphs = []
        for image in document.inline_shapes: 
            image_paragraphs.append(image._inline.graphic.graphicData.pic.nvPicPr.cNvPr.name)
            print(image.height.cm, image.width.cm, image._inline.graphic.graphicData.pic.nvPicPr.cNvPr.name)


        for para in doc.paragraphs:
            rels = para.part.rels

            if para.style.name == "Heading 1":
                title = para.text
            elif para.style.name == "Image" and i == 0:
                headerImgUrl = 

             
            newpara = {
                "text": para.text,
                "imgUrl": None,
                "imgTitle": None,
                "style": para.style.name,
            }
            if 'graphicData' in para._p.xml:
                image_paragraphs.append(para)
               
            self.paragraphs[i] = newpara
            i += 1
        rels = document.part.rels
        print(image_paragraphs)
        #print(self.newsItem)
        for rel in rels:
            if rels[rel].reltype == RT.HYPERLINK:
                print("link: ", rel, "url: ", rels[rel]._target)
        #for image in document.inline_shapes: 
            #print (image.height.cm, image.width.cm, image._inline.graphic.graphicData.pic.nvPicPr.cNvPr.name)

   
filename = 'Joulupuu - Christmas Tree Campaign 2020 at Espoo Campus until Dec 7.docx'
document = Document(filename)
document.save(filename)

parseNews = Parse_News()

parseNews.parse_news(document)
#parseNews.printNews()




