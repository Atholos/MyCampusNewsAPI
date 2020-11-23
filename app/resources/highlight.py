from flask import Flask
from flask_restful import Api, Resource, reqparse


class Highlight(Resource):

    @ staticmethod
    def get():
        highlightItem = {
                "title": "Halloween party",
                "higlight": True,
                "description": "Nokia halloween party this saturday at dream cafe! Come join us for some eerie fun",
                "timestamp": "October 20, 2020",
                "imgUrl": "../assets/pexels-wilson-vitorino-3230473.jpg",
                "imgTitle": "Halloween Party",
                "paragraphs": {
                    "1": "This is the world we live in",
                    "2": "Come join us in death",
                    "3": "Hehou hahau",
                    "4": '''Lorem ipsum dolor sit amet, meis expetenda ei eam, has ne assum aeque adipiscing, no legere utroque qui. Vix et congue invidunt facilisi, audire sententiae ea sea. Nulla accusam elaboraret eos ne. Solet putant epicuri te duo, per no error vivendum contentiones, legere mnesarchum duo ne. At qui sint dignissim, eum oratio veniam an.

                        Probo ancillae vituperatoribus in mea, his an dico enim bonorum, illum gubergren posidonium ex quo. Sit ea case minimum, mei malorum accusam expetendis ex. Ei has exerci nemore convenire, duo id eirmod nonumes. Eos et animal dolorum epicurei, te eam altera mediocrem, eu sea torquatos reformidans.

                        Elitr iudicabit eloquentiam cu vim. Graecis mediocritatem his in, ne erant harum soleat cum. In natum propriae mel. Quod impetus.''',
                    "5": '''Lorem ipsum dolor sit amet, meis expetenda ei eam, has ne assum aeque adipiscing, no legere utroque qui. Vix et congue invidunt facilisi, audire sententiae ea sea. Nulla accusam elaboraret eos ne. Solet putant epicuri te duo, per no error vivendum contentiones, legere mnesarchum duo ne. At qui sint dignissim, eum oratio veniam an.

                        Probo ancillae vituperatoribus in mea, his an dico enim bonorum, illum gubergren posidonium ex quo. Sit ea case minimum, mei malorum accusam expetendis ex. Ei has exerci nemore convenire, duo id eirmod nonumes. Eos et animal dolorum epicurei, te eam altera mediocrem, eu sea torquatos reformidans.

                        Elitr iudicabit eloquentiam cu vim. Graecis mediocritatem his in, ne erant harum soleat cum. In natum propriae mel. Quod impetus.''',
                },
                "paragraphImg": {
                        "2": "../assets/pexels-wilson-vitorino-3230473.jpg",
                        "5": "../assets/pexels-wilson-vitorino-3230473.jpg",
                },
        }
       
        return highlightItem, 200
