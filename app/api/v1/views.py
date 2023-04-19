from django.db.models import Sum, Count
from django.core.cache import cache
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.response import Response
from rest_framework.views import APIView
import csv

from app.models import Deal


class FileAPIView(APIView):
    def get(self, request):
        cache_response = cache.get('top5')
        if not cache_response:
            response = []
            top_5_clients = Deal.objects.values('customer') \
                         .annotate(total_spent=Sum('total')) \
                         .order_by('-total_spent')[:5]

            for client in top_5_clients:
                client_username = client['customer']
                client_deals = Deal.objects.filter(customer=client_username)
                gems = Deal.objects.filter(total__gt=0, item__in=client_deals.values('item')
                                           .annotate(count=Count('item'))
                                           .filter(count__gte=2)
                                           .values_list('item', flat=True))
                client['gems'] = gems.values_list('item', flat=True)

            for client in top_5_clients:
                client_data = {
                    'username': client['customer'],
                    'spent_money': client['total_spent'],
                    'gems': set(client['gems'])
                }
                response.append(client_data)
            cache.set('top5', response, 30)
        else:
            response = cache.get('top5')
        return Response({"response": response})

    def post(self, request):
        try:
            file = request.FILES['deals']
            decoded_file = file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                Deal.objects.create(**row)
            return Response({'OK': 'Файл успешно обработан!'})
        except MultiValueDictKeyError as err:
            return Response({"ERR": "Файл не был отправлен"})
        cache.delete('top5')
