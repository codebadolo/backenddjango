from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView, # new
    DestroyAPIView, # new
)
from  .models import  Article
from .serializers  import  ArticleSerializer


# Create view
class RecipeCreateView(CreateAPIView):
    serializer_class = ArticleSerializer

# Update view
class RecipeUpdateView(UpdateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

# List view
class RecipeListView(ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

# Delete view
class RecipeDeleteView(DestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
# Create your views here.
#these are the main views i need to develop
#  for the articles and the panier
 

 # publication des articles 
#  recherche des articles  
# detail des articles

