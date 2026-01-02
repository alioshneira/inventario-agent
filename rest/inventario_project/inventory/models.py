from django.db import models

class Server(models.Model):
    hostname = models.CharField(max_length=255, unique=True)
    ip_address = models.GenericIPAddressField()
    distribution = models.CharField(max_length=255)
    distribution_version = models.CharField(max_length=255)
    os_family = models.CharField(max_length=255)
    cpu_cores = models.IntegerField()
    memory_mb = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hostname

class Device(models.Model):
    server = models.ForeignKey(Server, related_name='devices', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    vendor = models.CharField(max_length=255, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    partitions = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.server.hostname} - {self.name}"

class Mount(models.Model):
    server = models.ForeignKey(Server, related_name='mounts', on_delete=models.CASCADE)
    mount = models.CharField(max_length=255)
    device = models.CharField(max_length=255)
    fstype = models.CharField(max_length=255)
    options = models.CharField(max_length=255)
    size_total = models.BigIntegerField()
    size_available = models.BigIntegerField()
    uuid = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.server.hostname} - {self.mount}"