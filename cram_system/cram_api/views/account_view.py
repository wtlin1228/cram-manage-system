from django.http import HttpResponse
from rest_framework import generics
from cram_api.models.account_model import Account
from cram_api.serializers.account_serializer import AccountSerializer
from rest_framework.decorators import api_view


class AccountList(generics.ListCreateAPIView):
    """
    List all account, or create a new account.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a user.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


@api_view(['GET'])
def cram_index(request):
    return HttpResponse('Hello cram system')
