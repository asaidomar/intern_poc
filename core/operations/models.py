from django.db import models


class Invoice(models.Model):
    status = models.CharField(max_length=255)  # draft, sent, etc ?
    creation_date = models.DateField(auto_now_add=True)
    number = models.CharField(unique=True, max_length=255)  # num de facture
    emit_date = models.DateField()
    days_delays = models.IntegerField(default=60)
    client = models.ForeignKey('accounts.Company', on_delete=models.DO_NOTHING)
    account = models.ForeignKey('accounts.Account', on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=19, decimal_places=10)

    def __str__(self):
        return f"{self.number} ({self.client})"


class Credit(models.Model):
    """ Avoir """
    creation_date = models.DateField(auto_now_add=True)
    number = models.CharField(unique=True, max_length=255)
    emit_date = models.DateField()
    client = models.ForeignKey('accounts.Company', on_delete=models.DO_NOTHING)
    account = models.ForeignKey('accounts.Account', on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=19, decimal_places=10)

    def __str__(self):
        return f"{self.number} ({self.client})"


class InvoiceDocument(models.Model):
    creation_date = models.DateField()
    name = models.CharField(max_length=255)
    file = models.FileField()
    invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, related_name="documents")

    def __str__(self):
        return f"{self.name}"


class Lettering(models.Model):
    creation_date = models.DateField(auto_now=True)
    code = models.CharField(max_length=255, unique=True)
    account = models.ForeignKey('accounts.Account', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.code


class Payment(models.Model):
    cash = 'cash'
    credit_cart = 'credit_cart'
    cheque = 'cheque'
    virement = 'virement'
    other = 'autre'

    payment_choice = [
        (cash, 'Comptant'),
        (credit_cart, 'Carte de credit'),
        (cheque, 'Cheque'),
        (virement, 'Virement'),
        (other, 'Autre'),
    ]
    account = models.ForeignKey('accounts.Account', on_delete=models.DO_NOTHING)
    payment_type = models.CharField(choices=payment_choice, max_length=250)
    payment_date = models.DateField(auto_now=True)
    amount = models.DecimalField(max_digits=19, decimal_places=10)

    def __str__(self):
        return str(self.amount)


class Misc(models.Model):
    account = models.ForeignKey('accounts.Account', on_delete=models.DO_NOTHING)
    creation_date = models.DateField(auto_created=True)
    credit_amount = models.DecimalField(max_digits=19, decimal_places=10)
    debit_amount = models.DecimalField(max_digits=19, decimal_places=10)


class Unpaid(models.Model):
    account = models.ForeignKey('accounts.Account', on_delete=models.DO_NOTHING)
    creation_date = models.DateField(auto_created=True)
    debit_amount = models.DecimalField(max_digits=19, decimal_places=10)


class PaymentDocument(models.Model):
    payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE, related_name="documents")


class OperationHistory(models.Model):
    operation = models.ForeignKey('Operation', on_delete=models.CASCADE)
    creation_date = models.DateField(auto_created=True)
    entry = models.TextField()
    owner = models.ForeignKey('accounts.Member', on_delete=models.CASCADE)


class Recovery(models.Model):
    account = models.ForeignKey('accounts.Account', on_delete=models.DO_NOTHING)
    creation_date = models.DateField(auto_created=True)
    invoice = models.ForeignKey('Invoice', on_delete=models.DO_NOTHING)
    owner = models.ForeignKey('accounts.Member', on_delete=models.DO_NOTHING)


class Action(models.Model):
    account = models.ForeignKey('accounts.Account', on_delete=models.DO_NOTHING)
    creation_date = models.DateField(auto_created=True)
    description = models.TextField()
    owner = models.ForeignKey('accounts.Member', on_delete=models.DO_NOTHING)


class Operation(models.Model):
    invoice_c = 'invoice'
    misc_c = "misc"
    payment_c = 'payment'
    credit_c = "credit"
    operation_type = [
        (invoice_c, "Facture"),
        (misc_c, "Facture"),
        (payment_c, "Paiement"),
        (credit_c, "Avoir")
    ]
    account = models.ForeignKey(
        'accounts.Account', on_delete=models.DO_NOTHING,
        related_name="operations")
    creation_date = models.DateField(auto_now=True)
    operation_type = models.CharField(choices=operation_type, max_length=255)
    credit_amount = models.DecimalField(max_digits=19, decimal_places=10)
    debit_amount = models.DecimalField(max_digits=19, decimal_places=10)
    contract_number = models.CharField(max_length=255)
    due_date = models.DateField(null=True, blank=True)
    action = models.ForeignKey(
        'Action', on_delete=models.DO_NOTHING, blank=True, null=True)
    lettering = models.ForeignKey(
        'Lettering', null=True, blank=True, on_delete=models.DO_NOTHING)
    invoice = models.ForeignKey(
        'Invoice', blank=True, null=True, on_delete=models.DO_NOTHING)
    recovery = models.ForeignKey(
        'Recovery', blank=True, null=True, on_delete=models.DO_NOTHING)
    payment = models.ForeignKey(
        'Payment', null=True, blank=True, on_delete=models.DO_NOTHING)
    credit = models.ForeignKey(
        'Credit', null=True, blank=True, on_delete=models.DO_NOTHING)
    misc_operation = models.ForeignKey(
        'Misc', null=True, blank=True, on_delete=models.DO_NOTHING)

    @property
    def document(self):
        if self.operation_type == self.invoice:
            return self.invoice.documents
        elif self.operation_type == self.payment:
            return self.payment.documents
