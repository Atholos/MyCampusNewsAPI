from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from PIL import Image  

class Parse_News():

    title = "This is article title"
    description = "this is news parser"
    highlight = False
    headerImgUrl = "header Url"
    headerImageTitle = "header image title"

    # Dummy author
    author = {
                "displayName": "This is display name",
                "email": "this is email",
                "department": "this is department",
                "jobtitle": "this is job title"
            }

    # Empty paragraph dictionary
    paragraphs = {}

    # Node for images
    articleImage = {
        "filename": "image filename",
        "height": "image height",
        "width": "image width" 
    }

    def createArticle(self):
        article = {
            "title": self.title,
            "author": {
                "displayName": self.author["displayName"],
                "email": self.author["email"],
                "department": self.author["department"],
                "jobtitle": self.author["jobtitle"]
            },
            "highlight": self.highlight,
            "description": self.description,
            "headerImgUrl": self.headerImgUrl,
            "headerImgTitle": self.headerImageTitle,
            "paragraphs": self.paragraphs,
        }
        return article


    def parse_news(self, doc):

        # Initializing indexes and creating an array for images
        i = 0
        image_paragraphs = []
        # looping through images inside the document and saving them to image array
        for image in document.inline_shapes:
            # First creating an articleImage object
            self.articleImage["filename"] = image._inline.graphic.graphicData.pic.nvPicPr.cNvPr.name
            self.articleImage["height"] = image.height.cm
            self.articleImage["width"] = image.width.cm
            image_paragraphs.append(self.articleImage)

        # Looping through paragraphs inside the document
        for para in doc.paragraphs:
            # If paragraph is the main header
            if para.style.name == "Heading 1":
                self.title = para.text
            # If paragraph is the header image
            elif para.style.name == "Image" and i == 0:
                self.headerImgUrl = image_paragraphs[0]["filename"]
                image_paragraphs.pop(0)
            # And if its neither we go to normal paragraph creation
            else:
                paraimg = None
                if 'graphicData' in para._p.xml:
                    paraimg = image_paragraphs[0]
                    image_paragraphs.pop(0)

                newpara = {
                    "text": para.text,
                    "image": paraimg,
                    "style": para.style.name,
                }
                i += 1
                self.paragraphs[i] = newpara    

             
        
            #if 'graphicData' in para._p.xml:
                #image_paragraphs.append(para)  
            
           
        #rels = document.part.rels
        #print(image_paragraphs)
        #print(self.newsItem)
        #for rel in rels:
           # if rels[rel].reltype == RT.HYPERLINK:
             #   print("link: ", rel, "url: ", rels[rel]._target)
        #for image in document.inline_shapes: 
            #print (image.height.cm, image.width.cm, image._inline.graphic.graphicData.pic.nvPicPr.cNvPr.name)

   
filename = 'Joulupuu - Christmas Tree Campaign 2020 at Espoo Campus until Dec 7.docx'
document = Document(filename)
document.save(filename)

parseNews = Parse_News()

parseNews.parse_news(document)
print(parseNews.createArticle())
#parseNews.printNews()




