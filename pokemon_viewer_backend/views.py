from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def healthcheck_view(request):
    return Response(status=status.HTTP_200_OK, data="Pokemon")
