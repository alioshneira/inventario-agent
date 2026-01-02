from rest_framework import serializers
from .models import Server, Device, Mount

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        exclude = ('server',)

class MountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mount
        exclude = ('server',)

class ServerSerializer(serializers.ModelSerializer):
    devices = DeviceSerializer(many=True, read_only=True)
    mounts = MountSerializer(many=True, read_only=True)
    devices_data = serializers.JSONField(write_only=True, required=False)
    mounts_data = serializers.JSONField(write_only=True, required=False)

    class Meta:
        model = Server
        fields = '__all__'

    def create(self, validated_data):
        devices_data = validated_data.pop('devices_data', [])
        mounts_data = validated_data.pop('mounts_data', [])

        server = Server.objects.create(**validated_data)

        for device_name, device_data in devices_data.items():
            Device.objects.create(
                server=server,
                name=device_name,
                size=device_data.get('size'),
                vendor=device_data.get('vendor'),
                model=device_data.get('model'),
                partitions=device_data.get('partitions', {})
            )

        for mount_data in mounts_data:
            mount_fields = [field.name for field in Mount._meta.get_fields()]
            filtered_mount_data = {k: v for k, v in mount_data.items() if k in mount_fields}
            Mount.objects.create(server=server, **filtered_mount_data)

        return server

    def update(self, instance, validated_data):
        devices_data = validated_data.pop('devices_data', [])
        mounts_data = validated_data.pop('mounts_data', [])

        instance = super().update(instance, validated_data)

        # Clear existing devices and mounts
        instance.devices.all().delete()
        instance.mounts.all().delete()

        for device_name, device_data in devices_data.items():
            device_fields = [field.name for field in Device._meta.get_fields()]
            filtered_device_data = {k: v for k, v in device_data.items() if k in device_fields}
            Device.objects.create(
                server=instance,
                name=device_name,
                **filtered_device_data
            )

        for mount_data in mounts_data:
            mount_fields = [field.name for field in Mount._meta.get_fields()]
            filtered_mount_data = {k: v for k, v in mount_data.items() if k in mount_fields}
            Mount.objects.create(server=instance, **filtered_mount_data)

        return instance
