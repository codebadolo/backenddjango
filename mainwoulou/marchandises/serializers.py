from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'titre_article',
                'description_article',
                'categorie_article' ,
                 'prix_article',
                'etat_article',
                'date_publication'
                ]
        
'''
class  CategorySerializer(serializers.ModelSerializer):
    nom_catgr = ArticleSerializer(many=True)
    
    class Meta:
        model = Categorie
        fields = (
            
            "nom_categorie",
            "nom_catgr",
        )

'''