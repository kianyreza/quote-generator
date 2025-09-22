from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
# Create your views here.


@api_view(['GET'])
def get_random_quote(request):
    try:
        api_url = 'https://zenquotes.io/api/random'
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()[0]
        quote_data = {
            'content': data.get('q', 'محتوایی یافت نشد.'),
            'author': data.get('a', 'نویسنده نامشخص')
        }
        return Response(quote_data, status=status.HTTP_200_OK)
    except requests.exceptions.RequestException as e:
        error_message = {'error': 'خطا در واکشی نقل قول: {}'.format(str(e))}
        return Response(error_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



