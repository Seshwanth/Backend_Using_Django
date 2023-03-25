from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views

router=DefaultRouter()
router.register('products',views.ProductViewSet, basename='products')
router.register('collection',views.CollectionViewSet)
router.register('carts',views.CartViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders',views.OrderViewSet, basename='orders')

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')

urlpatterns = router.urls + products_router.urls + carts_router.urls

# urlpatterns=[
#     path('products/', views.ProductViewSet.as_view()),
#     path('products/<int:id>/',views.ProductViewSet.as_view()),
#     path('collection/',views.CollectionViewSet.as_view()),  
#     path('collection/<int:id>/',views.collection_detail, name='collection-detail')
# ]