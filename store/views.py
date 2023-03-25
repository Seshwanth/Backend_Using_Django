from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from store.permissions import FullDjangoModelPermissions, IsAdminOrReadOnly, ViewCustomerHistoryPermission
from .models import Cart, CartItem, Customer, Order, OrderItem, Product,Collection,Review
from .serializers import AddCartItemSerializer, CartItemSerializer, CartSerializer, CollectionSerializer, CustomerSerializer, OrderSerializer, ProductSerializer, ReviewSerializer, UpdateCartItemSerializer
from store import serializers
from rest_framework.views import APIView
from django.db.models import Count
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.permissions import DjangoModelPermissions
# Create your views here.

# class ProductList(ListCreateAPIView):
    
#     queryset= Product.objects.select_related('collection').all()
#     serializer_class= ProductSerializer

#     def get_serializer_context(self):
#         return {'request': self.request}

# @api_view(['GET','POST','DELETE'])
# def product_list(request):
#     if request.method == 'GET':
#         queryset = Product.objects.select_related('collection').all()
#         serializer = ProductSerializer(queryset, many=True,context={'request':request})
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         # if serializer.is_valid():
#         #     serializer.validated_data
#         #     return Response('The Data has been POSTED')
#         # else:
#         #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         print(serializer.validated_data)
#         return Response(serializer.data, status=HTTP_201_CREATED)

# class ProductDetail(RetrieveUpdateDestroyAPIView):
#     queryset=Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field='id'

#     def delete(self,request, id):
#         product = get_object_or_404(Product, pk=id)
#         if product.orderitem_set.count() >0:
#             return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET','PUT','DELETE'])
# def product_detail(request,id):
#     product = get_object_or_404(Product, pk=id)
#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ProductSerializer(product,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         if product.orderitem_set.count() >0:
#             return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class CollectionList(ListCreateAPIView):
    
#     queryset = Collection.objects.annotate(products_count=Count('products')).all()
#     serializer_class = CollectionSerializer

# @api_view(['GET', 'POST'])
# def collection_list(request):
#     if request.method == 'GET':
#         queryset = Collection.objects.annotate(products_count=Count('products'))
#         serializer = CollectionSerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CollectionSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)

# class CollectionDetail(RetrieveUpdateDestroyAPIView):
#     queryset=Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field='id'

#     def delete(self,request,id):    
#         if collection.products.count() > 0:
#             return Response({'error': 'Collection cannot be deleted because it includes one or more products.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def collection_detail(request, pk):
#     collection = get_object_or_404(Collection.objects.annotate(products_count=Count('products')), pk=pk)
#     if request.method == 'GET':
#         serializer = CollectionSerializer(collection)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = CollectionSerializer(collection,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         if collection.products.count() > 0:
#             return Response({'error': 'Collection cannot be deleted because it includes one or more products.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class ProductViewSet(ModelViewSet):
#     queryset=Product.objects.all()
#     serializer_class= ProductSerializer

#     def get_serializer_context(self):
#         return {'request': self.request}

#     def destroy(self,request,*args,**kwargs):
#         if product.orderitems.count > 0:
#             return Response({'error':'Product cannot be deleted because it includes one or more products.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         return super().destroy(request, *args,**kwargs)


    # def delete(self,request,id):
    #     product = get_object_or_404(Product, pk=pk)
    #     if product.orderitems.count() >0:
    #         return Response({'error':'Product cannot be deleted because it includes one or more products.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     product.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

# class CollectionViewSet(ModelViewSet):
#     queryset=Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field='id'

#     def get_serializer_context(self):
#         return {'request': self.request}

#     def destroy(self,request,*args,**kwargs):
#         if collection.orderitems.count > 0:
#             return Response({'error':'Collection cannot be deleted because it includes one or more products.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         return super().destroy(request, *args,**kwargs)

    # def delete(self,request,id):    
    #     if collection.products.count() > 0:
    #         return Response({'error': 'Collection cannot be deleted because it includes one or more products.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     collection.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes= [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset= Product.objects.all()
        collection_id = self.request.query_params.get('collection_id')
        if collection_id is not None:
            queryset = queryset.filter(collection_id=collection_id)
        return queryset

    def get_serializer_context(self):
        return {'request': self.request}

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)

class CollectionViewSet(ModelViewSet):

    queryset = Collection.objects.annotate(
    products_count=Count('products')).all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Collection cannot be deleted because it includes one or more products.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}

class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerializer

class CartItemViewSet(ModelViewSet):
    serializer_class = CartItemSerializer
    http_method_names=['get','post','patch','delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        if self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer
    
    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}

    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk']).select_related('product')

class CustomerViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [FullDjangoModelPermissions]

    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [AllowAny()]
    #     return [IsAuthenticated()]    

    @action(detail= True, permission_classes = [ViewCustomerHistoryPermission])
    def history(self,request,pk):
        return Response('ok')

    @action(detail=False, methods=['GET', 'PUT'], permission_classes = [IsAuthenticated])
    def me(self,request):
        (customer, created) = Customer.objects.get_or_create(user__id = request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    # @action(detail=False)
    # def me(self, request):
    #     customer = Customer.objects.get(user_id=request.user.id)
    #     serializer = CustomerSerializer(customer)
    #     return Response(serializer.data)

class OrderViewSet(ModelViewSet):
    serializer_class= OrderSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Order.objects.all()

        (customer_id, created) = Customer.objects.only('id').get_or_create(user_id=user.id)
        return Order.objects.filter(customer_id=customer_id)