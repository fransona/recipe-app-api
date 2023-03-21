"""
Core views for app
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response


# Decorator use to simply access a api
@api_view(['GET'])
def health_check(request):
    """Return successfull response"""
    return Response({'healthy': True})
