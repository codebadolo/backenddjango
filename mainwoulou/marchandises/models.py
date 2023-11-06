from django.db import models

# Create your models here.
class  Categories(models.Model):
   
    CHOIX =( 
    ("Homme", "Homme"), 
    ("femme", "femme"), 
    ("enfant", "enfant")
    
    ) 
    nom_category = models.CharField(max_length=11, choices=CHOIX, verbose_name='Sexe')

class Article(models.Model):

    titre_article  = models.CharField(max_length=30)
    description_article = models.CharField(max_length=250 )
    categorie_article = models.ForeignKey(Categories , on_delete=models.CASCADE)
    prix_article = models.CharField( max_length= 10 )
    etat_article = models.CharField(max_length=15 )
    date_publication= models.DateField()
    
    
    # et autre champs  a ajouter  au cas ou le besion  ce fait sentire  
    def __str__(self):
        return self.titre_article   
    class Meta:
        
        verbose_name  =  'article'
        verbose_name_plural = 'articles'






   