"""estore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from api.views import ProductView,AddView,DiffView,MulView,SumView,SubtractView
from api.views import CubeView,NumcheckView,FactorialView,WordcountView,PrimenumView,ArmstrongView,PallindromeView,\
    ProductView,ProductDetailsView,ReviewsView,ReviewDetailsView,ProductsViewsetView,ProductModelViewsetView,\
    ReviewModelViewsetView,UsersView
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("api/v1/products",ProductsViewsetView,basename="products")
router.register("api/v2/products",ProductModelViewsetView,basename="books")
router.register("api/v1/reviews",ReviewModelViewsetView,basename="reviews")
router.register("register",UsersView,basename="myusers")

urlpatterns = [
    path('superuser/', admin.site.urls),
    # path("products",ProductView.as_view()),
    # path("add",AddView.as_view()),
    # path("dif",DiffView.as_view()),
    # path("multi",MulView.as_view()),
    # path("sum",SumView.as_view()),
    # path("minus",SubtractView.as_view())
    path("cube",CubeView.as_view()),
    path("numchk",NumcheckView.as_view()),
    path("fact",FactorialView.as_view()),
    path("wc",WordcountView.as_view()),
    path("prime",PrimenumView.as_view()),
    path("armstrong",ArmstrongView.as_view()),
    path("pallin",PallindromeView.as_view()),
    path("products",ProductView.as_view()),
    path("products/<int:id>",ProductDetailsView.as_view()),
    path("reviews",ReviewsView.as_view()),
    path("reviews/<int:id>",ReviewDetailsView.as_view())



]+router.urls
