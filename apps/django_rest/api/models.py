# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.db import models
from django.utils.translation import ugettext as _
# Third-party app imports

# Imports from your apps
from core.models import TimeStampedModel


class Person(TimeStampedModel):
    """
    Classe abstrata para comportar campos em comum
    com os as apps de pessoas,
    """

    name = models.CharField(
        verbose_name=_(u'Nome'),
        max_length=255
    )
    """
    Atributo da classe Person para
    setar um nome a pessoa

    Caracteristicas:
    CharField
    verbose name: Nome
    max length: 255
    """

    class Meta:
        """
        Seta a ordenação da listagem pelo campo `created` ascendente
        Nome da app no singular e plural
        """
        ordering = ['created']
        verbose_name = _(u'Pessoa')
        verbose_name_plural = _(u'Pessoas')

    def __unicode__(self):
        """
        Retorna o nome da pessoa
        como unicode.
        """
        return u'%s' % (self.name)


class Contact(TimeStampedModel):
    """
    Classe model para cadastrar os contatos
    de uma pessoa
    """

    person = models.ForeignKey(
        'Person',
        verbose_name=_('Pessoas'),
        related_name='contacts'
    )
    """
    Atributo da classe KindContact para referenciar
    ao objeto da classe speaker
    """

    KINDS = (
        ('PH', _('Telefone')),
        ('E', _('E-mail')),
        ('FX', _('Fax')),
        ('FB', _('Facebook')),
        ('TT', _('Twitter')),
        ('GH', _('Github')),
        ('GG', _('Google')),
    )

    kind = models.CharField(
        _(u'Tipo'),
        max_length=2,
        choices=KINDS
    )
    """
    Atributo da classe Contact para escolher as
    opções setada na tupla KINDS

    Caracteristicas:
    CharField
    max length: 2
    """

    value = models.CharField(
        _(u'Valor'),
        max_length=255
    )
    """
    Atributo da classe Contact para setar o
    valor da opção escolhida

    Caracteristicas:
    CharField
    max length: 255
    """

    class Meta:
        """
        Seta a ordenação da listagem pelo campo `created` ascendente
        Nome da app no singular e plural
        """
        ordering = ['created']
        verbose_name = _(u'Contato')
        verbose_name_plural = _(u'Contatos')

    def __unicode__(self):
        """
        Retorna o tipo e valor
        como unicode.
        """
        return u'%s, %s' % (self.kind, self.value)
