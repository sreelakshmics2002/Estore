from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Books,Reviews
from api.serializers import BookSerializer,ReviewSerializer,UserSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from django.contrib.auth.models import User

# class ProductView(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response({"msg":"inside products get"})
#
# class AddView(APIView):
#     def get(self,request,*args,**kwargs):
#         a=int(input("enter first number"))
#         b=int(input("enter second number"))
#         sum=a+b
#         return Response({"result":sum})
#
# class DiffView(APIView):
#     def get(self,request,*args,**kwargs):
#         a = int(input("enter first number"))
#         b = int(input("enter second number"))
#         sub = a-b
#         return Response({"result": sub})
#
# class MulView(APIView):
#     def get(self,request,*args,**kwargs):
#         a=int(input("enter first number:"))
#         b=int(input("enter second number:"))
#         pro=a*b
#         return Response({"result":pro})
#
# class SumView(APIView):
#     def post(self,request,*args,**kwargs):
#         n1=request.data.get("n1")
#         n2=request.data.get("n2")
#         sum=int(n1)+int(n2)
#         return Response({"result":sum})
#
#
# class SubtractView(APIView):
#     def post(self,request,*args,**kwargs):
#         a= request.data.get("a")
#         b=request.data.get("b")
#         subt=int(a)-int(b)
#         return Response({"result":subt})
#

class CubeView(APIView):
    def post(self,req,*args,**kwargs):
        n=int(req.data.get("num"))
        ans= n**3
        return Response({"result":ans})


class NumcheckView(APIView):
    def post(self,req,*args,**kwargs):
        n=int(req.data.get("num"))
        res=""
        if n%2==0:
            res="number is even"
        else:
            res="number is odd"
        return Response({"result":res})


class FactorialView(APIView):
    def post(self,req,*args,**kwargs):
        n=int(req.data.get("num"))
        res=1
        for i in range(1,(n+1)):
            res=res*i
        return Response({"factorial is":res})


class WordcountView(APIView):
    def post(self,request,*args,**kwargs):
        txt=request.data.get("text")
        words= txt.split(" ")
        wc={}
        for w in words:
            if w in wc:
                wc[w]+=1
            else:
                wc[w]=1
        return Response(data=wc)






class PrimenumView(APIView):
    def post(self,req,*args,**kwargs):
        n=int(req.data.get("num"))
        res=0
        for i in range(1,n+1):
            if n%i==0:
                res=res+1
        if res==2:
            return Response({"result":"prime number"})
        else:
            return Response({"result":"Not prime"})




class ArmstrongView(APIView):
    def post(self,req,*args,**kwargs):
        n=int(req.data.get("num"))
        res=0
        m=n
        while n>0:
            rem=n%10
            res=res*rem*rem*rem
            n=n//10
        if m==res:
            return Response({"result":"Armstrong"})
        else:
            return Response({"result":"Not armstrong"})



class PallindromeView(APIView):
    def post(self,req,*args,**kwargs):
        n=int(req.data.get("num"))
        res=0
        m=n
        while n>0:
            rem=n%10
            res=res*10+rem
            n=n//10
        if m==res:
            return  Response({"result":"pallindrome"})
        else:
            return  Response({"result":"not pallindrome"})

# ********************************SERIALIZER*****************************
class ProductView(APIView):
    def get(self,req,*args,**kwargs):
        qs=Books.objects.all()
        serializer=BookSerializer(qs,many=True)
        return Response(data=serializer.data)




    # def post(self,req,*args,**kwargs):

        # bname=req.data.get("name")
        # bauthor=req.data.get("author")
        # bprice=req.data.get("price")
        # bpublisher=req.data.get("publisher")
        # Books.objects.create(name=bname,author=bauthor,price=bprice,publisher=bpublisher)
        # return Response(data="created")


    def post(self,req,*args,**kwargs):
        serializer=BookSerializer(data=req.data)
        if serializer.is_valid():
            Books.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class ProductDetailsView(APIView):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        serializer=BookSerializer(book,many=False)
        return Response(data=serializer.data)

    def delete(self,req,*args,**kwargs):
        id=kwargs.get("id")
        Books.objects.get(id=id).delete()
        return Response(data="Deleted")

    def put(self,req,*args,**kwargs):
        id=kwargs.get("id")
        serializer=BookSerializer(data=req.data)
        if serializer.is_valid():
            Books.objects.filter(id=id).update(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)






class ReviewsView(APIView):

    def get(self,req,*args,**kwargs):
        reviews=Reviews.objects.all()
        serializer=ReviewSerializer(reviews,many=True)
        return Response(data=serializer.data)

    def post(self,req,*args,**kwargs):
        serializer=ReviewSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)





class ReviewDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(qs,many=False)
        return Response(data=serializer.data)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        object=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(instance=object,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Reviews.objects.get(id=id).delete()
        return Response(data="deleted")




class ProductsViewsetView(ViewSet):

    def list(self,req,*args,**kwargs):
        qs=Books.objects.all()
        serializer=BookSerializer(qs,many=True)
        return Response(data=serializer.data)


    def create(self,req,*args,**kwargs):
        serializer=BookSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)



    def retrieve(self,req,*args,**kwargs):
        id=kwargs.get("pk")
        book=Books.objects.get(id=id)
        serializer=BookSerializer(book,many=False)
        return Response(data=serializer.data)



    def update(self,req,*args,**kwargs):
        id=kwargs.get("pk")
        book=Books.objects.filter(id=id)
        serializer=BookSerializer(instance=book,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)



    def destroy(self,req,*args,**kwargs):
        id=kwargs.get("pk")
        Books.objects.get(id=id).delete()
        return Response(data="deleted")






class ProductModelViewsetView(ModelViewSet):
    serializer_class=BookSerializer
    queryset = Books.objects.all()


class ReviewModelViewsetView(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Reviews.objects.all()
    def list(self, request, *args, **kwargs):
        allreviews=Reviews.objects.all()
        if "user" in request.query_params:
            allreviews=allreviews.filter(user=request.query_params.get("user"))
        serializer = ReviewSerializer(allreviews, many=True)
        return Response(data=serializer.data)




class UsersView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
