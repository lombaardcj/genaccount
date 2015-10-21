from django.contrib import admin

from .models import Account, BasicJournal, JournalEntry

# Register your models here.
class JournalEntryInline(admin.TabularInline):
    model=JournalEntry
    
    #determine default number of choices to add automatically everytime admin form is opened to add/edit entry
    extra=0

class BasicJournalAdmin(admin.ModelAdmin):
    #define inline
    inlines=[JournalEntryInline]

    list_display = ('comment',)
    
    
    #Which field can be search on
    search_fields=['comment']
    
    #Own research. How to make fields editable in change list view
    list_editable =['comment']
    
    #Pagination. Items list per page
    list_per_page = 5
    
    #Limit the maximum amount of items to display. Protect the user against themselves
    list_max_show_all = 10
    

admin.site.register(Account)
#admin.site.register(BasicJournal)
admin.site.register(BasicJournal, BasicJournalAdmin)
