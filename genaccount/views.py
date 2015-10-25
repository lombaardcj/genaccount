from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views import generic

#from django.views.generic.dates import WeekArchiveView

from .models import Account, BasicJournal, JournalEntry


class AccountList(generic.ListView):
    model = Account


class AccountDetail(generic.DetailView):
    model = Account


class AccountCreate(generic.CreateView):
    model = Account
    fields = ['author', 'name', 'type', 'comment','balance','updated_on']


class AccountUpdate(generic.UpdateView):
    model = Account
    fields = ['author', 'name', 'type', 'comment','balance','updated_on']


class AccountDelete(generic.DeleteView):
    model = Account
    success_url = reverse_lazy('genaccount:account_list')


#TODO: Requires pytz to work properly. Disable USE_TZ in settings.py to allow this method to run
#FIXME: This requirement need to be fixed - 20151025
class ArticleWeekArchiveView(WeekArchiveView):
    queryset = Account.objects.all()
    date_field = "updated_on"
    week_format = "%W"
    allow_future = True


#from .forms import ShowAccountForm



#def index(request):
    #return render(request,'genaccount/index.html','')

#def accountlist(request):
    #account_list=Account.objects.all()
    #context={'account_list':account_list}
    #return render(request,'genaccount/accountlist.html',context)

#def detail(request, account_id):
    #account=get_object_or_404(Account, pk=account_id)
    #return render(request,'genaccount/detail.html',{'account':account})


#def IndexView(generic.ListView):
    #template_name = 'genaccount/index.html'
    #context_object_name = 'account_list'

    #def get_queryset(self):
        #"""Return all customer accounts."""
        #return Account.objects.all()

#def showaccount(request,pk):
    ##return render(request,'genaccount/index.html','')
    ## if this is a POST request we need to process the form data
    #if request.method=='POST':
        ## create a form instance and populate it with data from the request:
        #form=ShowAccountForm(request.POST)
        ## check whether it's valid:
        #if form.is_valid():
            ## process the data in form.cleaned_data as required
            ## ...
            ## redirect to a new URL:
            #return HttpResponseRedirect('/')

        ## if a GET (or any other method) we'll create a blank form
    #else:
        #form=ShowAccountForm()

        #return render(request,'genaccount/detail.html',{'form':form})



