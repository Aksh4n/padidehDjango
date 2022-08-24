from rest_framework.response import Response
from rest_framework.decorators import api_view
from yaml import serialize
from store.models import *
from store.utils import cartData
from .serializers import OrderItemSerializer 



@api_view(['GET'])
def orderItem(request):
    data = cartData(request)
    cartItems = data['cartItems']
    items = data['items']
    for i in items:
        q = OrderItem.objects.get(id=i.id)
        

        serializer = OrderItemSerializer(q)

        return Response(serializer.data)




