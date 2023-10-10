from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from . import celery_app


@celery_app.task(bind=True)
def say_hello(self):
    print("Hello >>>>>>>>>>>>>>")


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def healthcheck_view(request):
    say_hello.delay()
    return Response(status=status.HTTP_200_OK, data="Pokemon")
