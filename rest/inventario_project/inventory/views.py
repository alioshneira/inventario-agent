from rest_framework import generics, status
from rest_framework.response import Response
from .models import Server
from .serializers import ServerSerializer

class ServerCreateView(generics.CreateAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

    def create(self, request, *args, **kwargs):
        hostname = request.data.get('hostname')
        instance = Server.objects.filter(hostname=hostname).first()

        # Extract devices and mounts data from the request
        devices_data = request.data.get('devices')
        mounts_data = request.data.get('mounts')

        # Prepare data for the serializer
        data = request.data.copy()
        if devices_data:
            data['devices_data'] = devices_data
        if mounts_data:
            data['mounts_data'] = mounts_data


        serializer = self.get_serializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED if not instance else status.HTTP_200_OK, headers=headers)