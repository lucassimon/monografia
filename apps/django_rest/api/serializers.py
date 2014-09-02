# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports

# Third-party app imports
from rest_framework import serializers

# Imports from your apps
from .models import Person, Contact 

class ContactSerializer(serializers.ModelSerializer):
    """
    Serializar o model KindContact
    """
    
    kind_display = serializers.Field(
        source='get_kind_display',
    )

    class Meta:
        model = Contact
        fields = ['id', 'person', 'kind', 'kind_display', 'value']


class PersonSerializer(serializers.ModelSerializer):
    """
    Serializar o model Speaker
    adicionando algumas funcionalidades
    na api
    """

    class Meta:
        """
        Seta definições para serializar
        o model
        """
        model = Person
        fields = ['id', 'name',]
