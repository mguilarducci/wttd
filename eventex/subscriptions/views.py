# coding: utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        form.full_clean()
        s = Subscription(**form.cleaned_data)
        s.save()
        return HttpResponseRedirect('/inscricao/%d/' % s.pk)
    else:
        return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})
