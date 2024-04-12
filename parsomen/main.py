from flask import Flask
from flask_graphql import GraphQLView

from parsomen.sorgular.sorgu import sorgu_semasi

app = Flask(__name__)
app.debug = True

"""
Create endpoints for Parsomen

Parsomen -> Hamur -> Blok

Yetenekleri:
* Metin arama: elasticsearch ile kullanılabilir
Parsomen title'lari veya bloklarin metin olanlarındaki verileri arayacak. Tipik regex arama yapilacak.

* Parsomen yarat, güncelle, hamur hariç diğer verileri getir
* Hamur uret, hamur sira no blok guncelleme. 
* Blok uret. Blok getir

"""

# Add the GraphQL endpoint to your Flask app
app.add_url_rule('/graphql',
                 view_func=GraphQLView.as_view('graphql', schema=sorgu_semasi, graphiql=True))


if __name__ == '__main__':
    app.run()
