# -*- coding:utf-8 -*-

# Stdlib imports


# Core Django imports
from django.contrib import admin
from django.utils.translation import ugettext as _

# Third-party app imports

# Realative imports of the 'app-name' package
from .models import Person, Contact


class ContactInline(admin.TabularInline):
    """
    Formulario de contatos em linha
    """
    model = Contact
    extra = 2


class PersonAdmin(admin.ModelAdmin):
    """
    Classe admin utilizada no django admin para oferecer as
    opcoes de CRUD da tabela pessoa
    """

    inlines = [ContactInline, ]

    # campos a serem exibidos na tabela
    list_display = (
        'name',
        'created'
    )

    date_hierarchy = 'created'

    # campos que utilizam buscas no model
    search_fields = ('name', 'created', )

    list_filter = ('created', )

    fieldsets = (
        (
            _(u'Dados da Pessoa'),
            {
                'fields': (
                    'name',
                ),
                'description': _(u'Dados'),
                'classes': [],
            }
        ),
    )


class ContactAdmin(admin.ModelAdmin):
    """
    Classe admin utilizada no django admin para oferecer as
    opcoes de CRUD da tabela de contatos
    """

    # campos a serem exibidos na tabela
    list_display = (
        'kind',
        'value',
        'created'
    )

    date_hierarchy = 'created'

    # campos que utilizam buscas no model
    search_fields = ('kind', 'value', 'created', )

    list_filter = ('created', )

    fieldsets = (
        (
            _(u'Dados de contatos'),
            {
                'fields': (
                    'kind',
                    'value'
                ),
                'description': _(u'Dados'),
                'classes': [],
            }
        ),
    )


admin.site.register(Person, PersonAdmin)
admin.site.register(Contact, ContactAdmin)
