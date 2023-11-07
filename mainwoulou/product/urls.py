from django.urls import include, path
from rest_framework import routers


'''
from .views import (
    ProductViewSet,
    ProductCreate,
    ProductDelete,
    ProductUpdate,
    ProductList,
    ProductDetail,
)
from .views import (
    CategoryViewSet,
    CategoryCreate,
    CategoryDelete,
    CategoryUpdate,
    CategoryList,
    CategoryDetail,
)


routercat = routers.DefaultRouter()
routercat.register(r"categories-api", CategoryViewSet)

router = routers.DefaultRouter()
router.register(r"product-api", ProductViewSet)

app_name = "products"
'''
app_names = "product" 
from .views import ProductListAPI, ProductDetailAPI, CategoryListAPI, CategoryDetailAPI ,CategoryCreateAPI
urlpatterns = [
    
    
    
 path('api/products/', ProductListAPI.as_view(), name='product-list-api'),
 path('api/categories/create/', CategoryCreateAPI.as_view(), name='category-create-api'),

    path('api/products/<int:pk>/', ProductDetailAPI.as_view(), name='product-detail-api'),
    path('api/categories/', CategoryListAPI.as_view(), name='category-list-api'),
    path('api/categories/<int:pk>/', CategoryDetailAPI.as_view(), name='category-detail-api'),
 
]

   ###############################
'''
    path("", include(router.urls,)),
    path("product/add/", ProductCreate.as_view(), name="product-add"),
    path("product/<int:pk>/", ProductDetail.as_view(), name="product-detail"),
    path("product/<int:pk>/update/", ProductUpdate.as_view(), name="product-update"),
    path("product/<int:pk>/delete/", ProductDelete.as_view(), name="product-delete"),
    path("product/", ProductList.as_view(), name="product-list"),
      
      
      path("", include(routercat.urls,)),
    path("category/add/", CategoryCreate.as_view(), name="category-add"),
    path("category/<int:pk>/", CategoryDetail.as_view(), name="category-detail"),
    path("category/<int:pk>/update/", CategoryUpdate.as_view(), name="category-update"),
    path("category/<int:pk>/delete/", CategoryDelete.as_view(), name="category-delete"),
    path("category/", CategoryList.as_view(), name="category-list"),
    '''