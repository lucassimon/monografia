# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.http import HttpResponse

# Third-party app imports

# Imports from your apps


def loaderio(request):
    content = 'loaderio-a11d9dfdb04fa7b965e4464c87cd8576'
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Length'] = len(content)
    return response
