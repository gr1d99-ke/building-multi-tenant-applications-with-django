from django.db import models


class Tenant(models.Model):
    name = models.Charfield(max_length=100)
    subdomain_prefix = models.Charfield(max_length=100, unique=True)


class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    class Meta:
        abstract = True

