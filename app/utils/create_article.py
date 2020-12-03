from .db_create import DBCreate
from .db_query import DBQuery
from flask import current_app


class CreateArticle():
    dbc = DBCreate()
    dbq = DBQuery()
    '''
    data = {
        "title": "Welcome to Nokia Finland Christmas Session on December 10",
        "author": {
            "id": 1,
            "displayName": "Maki, Tuuli-Maria (Nokia - FI/Espoo)",
            "email": "tuuli-maria.maki@nokia.com",
            "department": "MN L1 Espoo TC",
            "jobtitle": "Campus Communication trainee"
        },
        "highlight": True,
        "description":
        "Welcome to Christmas Session with stand-up comedian & TV host Jaakko Saariluoma on Dec 10",
        "timestamp": "2020-11-27",
        "headerImgUrl": "Welcome to Christmas Session with stand-up comedian & TV host Jaakko Saariluoma on Dec 10 .jpg",
        "headerImgTitle": "Open internal positions in Espoo",
            "paragraphs": {
                "1": {
                    "text": "Dear colleagues,",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
                },
                "2": {
                    "text":
                    "Many things have changed this year due to COVID-19, and so have our plans for the traditional local Christmas parties in Finland. This year we offer you something else. We invite you all to experience something fun together virtually, just before the year end.",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
                },
                "3": {
                    "text":
                    "Welcome to a relaxed session with actor, stand-up comedian and television host Jaakko Saariluoma. He´s a quick thinker, sharp and fun – always a step ahead of everyone. Take your seats and get ready to be entertained!",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
                },
                "4": {
                    "text":
                    "The session will be hosted by one of Finland’s leading business speakers and writers André Noël Chaker. As an entrepreneur, André has been a leading force in many science, technology, gaming and sports related start-up ventures.",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
                },
                "5": {
                    "text":
                        "Opening by André Noël Chaker",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
                },
                "6": {
                    "text": "Nokia’s season’s greetings",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
                },
                "8": {
                    "text":  "by Country Senior Officer Tommi Uitto and Site Heads Vesa Kohtamäki, Erja Sankari and Petri Ahokas",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
                },
                "9": {
                    "text": "André’s take on Finns & Christmas by André Noël Chaker",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
                },
                "10": {
                    "text": "Christmas music from Nokia sites in Finland by Nokia employees",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
                },
                "11": {
                    "text":
                        "Stand-up show by Jaakko Saariluoma",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
                },
                "12": {
                    "text":
                    "Take a sneak peek on Jaakko’s greetings to our Nokia employees here.",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
                },
                "13": {
                    "text":
                    "This is an internal event dedicated for Nokia employees in Finland. Join us for a fun and relaxed session!",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
                },
                "14": {
                    "text": "Welcome!",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
                },
                "15": {
                    "text":
                    "Tip! You may want to consider arranging your own virtual Christmas get-together with your team right after this show.",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
                },
                "16": {
                    "text": "Br,",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
                },
                "17": {
                    "text": "Finland Communications",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
                },
                "18": {
                    "text": "How to join the session:",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
                },
                "19": {
                    "text": "The session is a live stream. A recording of the session will be made available soon afterwards",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
                },
                "20": {
                    "text": "The live stream will be available here.",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "List Paragraph"
                },
                "21": {
                    "text": "Password for the session is: NokiaFinland",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "List Paragraph"
                },
                "22": {
                    "text": "Please note that for optimal viewing, it is best not to use VPN. If the live stream doesn't load when the session starts, please refresh the page or try another browser.",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
                },
        },
        "links": {
            "20": {
                "link": "https://nokia.sharepoint.com/:v:/r/sites/espoo_HQ_campus/Espoo Campus Pictures/2020/Christmas session with Jaakko Saariluoma 10.12.2020/Jaakko Saariluoma%27s greetings to Nokia employees.mp4?csf=1&web=1&e=8pEZab",
                "link_keyword": "here"
            },
            "21": {
                "link": "https://livekatsomo.fi/streams/nokia-saariluoma/",
                "link_keyword": "here"
            }
        }
    }
    '''

    def setData(self,data):
        self.data = data

   

    def create_newsitem(self):

        # creating author, article, image, header, paragraph, links, database objects

        author  = self.dbc.create_author(self.data["author"]["displayName"], self.data["author"]["email"], self.data["author"]["department"], self.data["author"]["jobtitle"])
        article = self.dbc.create_article(self.data["title"], self.data["description"], self.data["highlight"], author.id)
        # filename, url, container, articleid, imgtitle
        headerimage = self.dbc.create_image(self.data["headerImgUrl"], None , current_app.config["IMAGE_CONTAINER_NAME"], article.id, self.data["headerImgTitle"])
        header = self.dbc.create_header(article.id, headerimage.id)
        paragraphs = self.parse_paragraphs(article.id)

       
        print(author.id, article.id)
      
        return {"author": author.id, "article": article.id, "headerimage": headerimage.id, "header": header.id, "paragraphs": paragraphs}  

     # for parsing the paragraphs from dictionary
    def parse_paragraphs(self, articleid):
        # Empty dict of paragraphs to return for testing purposes
        paragraphs = {}

        for paragraph in self.data["paragraphs"]:
            # Key is the order number 
            order_nr = paragraph
            text =  self.data["paragraphs"][paragraph]["text"]
            imgUrl = self.data["paragraphs"][paragraph]["imgUrl"]
            imgTitle =  self.data["paragraphs"][paragraph]["imgTitle"]
            style = self.data["paragraphs"][paragraph]["style"]
            #If paragraphs has images we create them first.
            image = None
            paraid = None
            if imgUrl != None or "":
                image = self.dbc.create_image(imgUrl, None, current_app.config["IMAGE_CONTAINER_NAME"], articleid, imgTitle)
                # self, text, style, articleid, imageid, ordernr
                dbpara = self.dbc.create_paragraph(text, style, articleid, image.id, order_nr)
                paraid = dbpara.id
                # Adding database objects id to testing dictionary
                paragraphs[paragraph] = paraid
            else:
                #If paragraph has no image then go here
                dbpara = self.dbc.create_paragraph(text, style, articleid, image, order_nr)
                paraid = dbpara.id
                 # Adding database objects id to testing dictionary
                paragraphs[paragraph] = paraid

            # Checking if paragraph has any links attached to it
            for link in self.data["links"]:
                if link == order_nr:
                    # paragraph_id, link, link_keyword
                    link_url = self.data["links"][link]["link"]
                    link_key =  self.data["links"][link]["link_keyword"]
                    dblink = self.dbc.create_link(paraid, link_url , link_key)
        return paragraphs
        

       
