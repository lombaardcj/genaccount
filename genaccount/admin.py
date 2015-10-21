from django.contrib import admin

from .models import Account, BasicJournal, JournalEntry

# Register your models here.

admin.site.register(Account)
admin.site.register(BasicJournal)
admin.site.register(JournalEntry)
