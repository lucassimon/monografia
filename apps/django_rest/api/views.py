# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports

# Third-party app imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics

# Imports from your apps
from .models import Person, Contact 
from .serializers import PersonSerializer, ContactSerializer


@api_view(['GET'])
def api_root(request, format=None):
    """
    Endpoint de toda a API REST
    """

    return Response(
        {
            'pessoas': reverse('person-list', request=request),
            'contatos': reverse('contact-list', request=request),
        }
    )

class PersonList(generics.ListCreateAPIView):
    """
    Endpoint que representa a lista de pessoas, e permite que novas
    pessoas sejam cadastrados.
    """
    model = Person
    serializer_class = PersonSerializer


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Endpoint que representa uma instancia de pessoa, e permite que novas
    pessoas sejam atualizados.
    '''
    model = Person
    serializer_class = PersonSerializer


class ContactList(generics.ListCreateAPIView):
    """
    Endpoint que representa a lista de contatos, e permite que novos
    contatos sejam cadastrados.
    """
    model = Contact
    serializer_class = ContactSerializer


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Endpoint que representa uma instancia de contato, e permite que novos
    contatos sejam atualizados.
    '''
    model = Contact
    serializer_class = ContactSerializer
