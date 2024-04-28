
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Bank , Branch , User





class ShowBank(LoginRequiredMixin,ListView):
    model=Bank
    template_name='Bank/showbank.html'
    context_object_name='bank'

    def get_queryset(self):
        return Bank.objects.filter(owner=self.request.user)


class bankdetail(LoginRequiredMixin ,DetailView):
    model=Bank
    template_name='Bank/bankdetail.html'
    context_object_name='bank'

class branchdetail(LoginRequiredMixin,DetailView):
    model=Branch
    template_name='Bank/branchdetail.html'
    context_object_name='branch'

    # def get_object(self, queryset=None):
    #     obj = super().get_object(queryset=queryset)
    #     if obj.bank.owner != self.request.user:
    #         raise Http404('You do not have access to this page.')
    #     return obj
class addbank( LoginRequiredMixin,CreateView):
    model=Bank
    fields=['name' , 'swift_code' , 'institution_number' , 'discription'] 
    template_name='Bank/addbank.html'
    def get_success_url(self):
        return reverse_lazy('showbank', kwargs={'pk': self.object.pk})

    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    def get_queryset(self):
        return Bank.objects.all()
    


class addbranch(LoginRequiredMixin, CreateView):
    model = Branch
    fields = ['name', 'transition_number', 'address', 'email', 'capacity']
    template_name = 'Bank/addbranch.html'

    def get_success_url(self):
        return reverse_lazy('bankdetails', kwargs={'pk': self.kwargs['pk']})
    
    def form_valid(self, form):
        bank_id = self.kwargs['pk']
        bank = Bank.objects.get(pk=bank_id)
        form.instance.bank = bank
        return super().form_valid(form)


class aditbranch(LoginRequiredMixin , UpdateView):
    model=Branch
    template_name='Bank/editbranch.html'
    fields=['name' , 'transition_number' , 'address' , 'email' , 'capacity']

    def get_success_url(self):
        return reverse_lazy('bankdetails' , kwargs={'pk':self.object.bank_id})

        
# class Userprofile(LoginRequiredMixin , DetailView):
#     model=User
#     template_name='Bank/show_profile.html'
#     context_object_name='user'

#     def get_object(self ) :
#         return User.objects.filter(owned_banks=self.request.user)