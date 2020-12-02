from db_create import DBCreate


class CreateArticle():
    self.db = DBCreate()
    self.data =
    {
        "title": "Welcome to Nokia Finland Christmas Session on December 10",
        "author": {
            "id": 1,
            "displayName": "Maki, Tuuli-Maria (Nokia - FI/Espoo)",
            "email": "tuuli-maria.maki@nokia.com",
            "department": "MN L1 Espoo TC",
            "jobtitle": "Campus Communication trainee"
        },
        "highlight": true,
        "description":
        "Welcome to Christmas Session with stand-up comedian & TV host Jaakko Saariluoma on Dec 10",
        "timestamp": "2020-11-27",
        "bannerImgUrl": "christmas_session.jpg",
            "bannerImgTitle": "Open internal positions in Espoo",
            "paragraphs": {
                "1": {
                    "text": "Dear colleagues,",
                    "imgUrl": null,
                    "imgTitle": null,
                    "style": "normal"
                },
                "2": {
                    "text":
                    "Many things have changed this year due to COVID-19, and so have our plans for the traditional local Christmas parties in Finland. This year we offer you something else. We invite you all to experience something fun together virtually, just before the year end.",
                    "imgUrl": null,
                    "imgTitle": null,
                    "style": "normal"
                },
                "3": {
                    "text":
                    "Welcome to a relaxed session with actor, stand-up comedian and television host Jaakko Saariluoma. He´s a quick thinker, sharp and fun – always a step ahead of everyone. Take your seats and get ready to be entertained!",
                    "imgUrl": null,
                    "imgTitle": null,
                    "style": "normal"
                },
                "4": {
                    "text":
                    "The session will be hosted by one of Finland’s leading business speakers and writers André Noël Chaker. As an entrepreneur, André has been a leading force in many science, technology, gaming and sports related start-up ventures.",
                    "imgUrl": null,
                    "imgTitle": null,
                    "style": "normal"
                },
                "5": {
                    "text": "beep",
                    "imgUrl": null,
                    "imgTitle": null,
                    "style": "normal"
                },
                "6": {
                    "text":
                    "This is an internal event dedicated for Nokia employees in Finland. Join us for a fun and relaxed session!",
                    "imgUrl": null,
                    "imgTitle": null,
                    "style": "normal"
                },
                "7": {
                    "text": "Welcome!",
                    "imgUrl": null,
                    "imgTitle": null,
                    "style": "normal"
                },
                "8": {
                    "text":
                    "Tip! You may want to consider arranging your own virtual Christmas get-together with your team right after this show.",
                    "imgUrl": null,
                    "imgTitle": null,
                    "style": "normal"
                },
                "9": {
                    "text": "Br,",
                    "imgUrl": null,
                    "imgTitle": null,
                    "style": "normal"
                },
                "10": {
                    "text": "Finland Communications",
                    "imgUrl": null,
                    "imgTitle": null,
                    "style": "normal"
                }
        }
    }

    # def __init__ (self, data):
    #self.data = data

    def create_newsitem(self):
        article = db.create_article()
