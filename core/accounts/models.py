from django.contrib.auth.models import User, Group
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey("Company", on_delete=models.CASCADE)
    # role possible only over company
    account = models.ForeignKey("Account", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.account})"


class CompanyGroup(models.Model):
    user = models.OneToOneField(Group, on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roles = models.ManyToManyField(Role, blank=True, null=True, related_name="members")

    def __str__(self):
        return str(self.user)


class Address(models.Model):
    main_address = models.BooleanField(default=False)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)

    def __str__(self):
        return self.address


class CompanyAddress(Address):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)


class MemberAddress(Address):
    member = models.ForeignKey('Member', on_delete=models.CASCADE)


class Company(models.Model):
    # holding
    parent = models.ForeignKey(
        'self', default=None, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    tva_number = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True)
    siret = models.CharField(max_length=20, unique=True)
    code_naf = models.CharField(max_length=20)
    activity = models.TextField()
    employee_number = models.IntegerField(default=1)
    creation_date = models.DateField()
    system_creation_date = models.DateField(auto_created=True)
    update_date = models.DateField(auto_now=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}({self.siret})'


class Phone(models.Model):

    class Meta:
        ordering = ['value']
    value = models.CharField(max_length=20)

    def __str__(self):
        return self.value


class MemberPhone(Phone):
    member = models.ForeignKey(
        'Member', on_delete=models.CASCADE, related_name="member_phones")


class CompanyPhone(Phone):
    company = models.ForeignKey(
        'Company', on_delete=models.CASCADE, related_name="companies_phones")


class ContractDocument(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField()
    contract = models.ForeignKey('Contract', on_delete=models.CASCADE)


class Contract(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    start_date = models.DateField(auto_created=True)
    update_date = models.DateField(auto_now=True)
    name = models.CharField(max_length=255)
    code = models.CharField(unique=True, max_length=255)


class Account(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    code = models.CharField(max_length=255, unique=True)
    iban = models.CharField(max_length=30, unique=True)
    bank = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.iban} ({self.company})"
