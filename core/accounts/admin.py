from django.contrib import admin

# Register your models here.


from core.accounts.models import (
    Member, Role, Company, Account, CompanyAddress, CompanyPhone, Contract, ContractDocument
)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    pass


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(CompanyAddress)
class CompanyAddressAdmin(admin.ModelAdmin):
    pass


@admin.register(CompanyPhone)
class CompanyPhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    pass


@admin.register(ContractDocument)
class ContractDocumentAdmin(admin.ModelAdmin):
    pass