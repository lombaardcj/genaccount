import datetime

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


# Create your models here.

class Account(models.Model):
    ASSET = 1
    LIABILITY = 2
    EQUITY = 3
    INCOME = 4
    COST_OF_SALES = 5
    EXPENSE = 6
    OTHER_INCOME = 7
    OTHER_EXPENSE = 8
        
    TYPE_CHOICES = (
        (ASSET, 'Asset'),
        (LIABILITY, 'Liability'),
        (EQUITY, 'Equity'),
        (INCOME, 'Income'),
        (COST_OF_SALES, 'Cost of Sales'),
        (EXPENSE, 'Expense'),
        (OTHER_INCOME, 'Other Income'),
        (OTHER_EXPENSE, 'Other Expense')
    )
    
    author = models.ForeignKey('auth.User')
    
    name = models.CharField(max_length=50, unique=True, db_index=True)
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, blank=True)    

    comment = models.CharField(max_length=50,blank=True, null=True)
    
    balance = models.DecimalField(max_digits=10,decimal_places=2,default='0.00')

    created_on = models.DateTimeField(default=timezone.now,editable=False)
    updated_on = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        ASSET = 1
        LIABILITY = 2
        EQUITY = 3
        INCOME = 4
        COST_OF_SALES = 5
        EXPENSE = 6
        OTHER_INCOME = 7
        OTHER_EXPENSE = 8
            
        TYPE_CHOICES = (
            (ASSET, 'Asset'),
            (LIABILITY, 'Liability'),
            (EQUITY, 'Equity'),
            (INCOME, 'Income'),
            (COST_OF_SALES, 'Cost of Sales'),
            (EXPENSE, 'Expense'),
            (OTHER_INCOME, 'Other Income'),
            (OTHER_EXPENSE, 'Other Expense')
        )
        return str(self.type) + '-' + str(self.id) + ' ' + self.name + ' - (' + TYPE_CHOICES[self.type][1]+')'

    def get_absolute_url(self):
        return reverse('genaccount:account_detail', args=[str(self.id)])


class BasicJournal(models.Model):
    author = models.ForeignKey('auth.User')
    postdate = models.DateTimeField(default=timezone.now, help_text="When Journal was posted")

    comment = models.CharField(max_length=50,help_text="Short comment on journal action", db_index=True)
    
    created_on = models.DateTimeField(default=timezone.now,editable=False)
    updated_on = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.comment + ' (' + str(self.id) + ')'


class JournalEntry(models.Model):
    author = models.ForeignKey('auth.User')

    basic_journal = models.ForeignKey(BasicJournal)
    
    account = models.ForeignKey('genaccount.Account', on_delete=models.PROTECT)
    
    descr = models.CharField(max_length=50, blank=True, help_text="Description of the journal transaction entry", db_index=True)

    balance = models.DecimalField(max_digits=10,decimal_places=2,default='0.00', help_text="Postive balance always debit, negative balance always credit")
    
    created_on = models.DateTimeField(default=timezone.now,editable=False)
    updated_on = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.descr + ' (' + str(self.id) + ')'
