from django.shortcuts import render, redirect, reverse
from subscribe.models import Subscribe
from subscribe.forms import SubscribeForm


# Create your views here.
def subscribe(request):
    subscribe_form = SubscribeForm()
    if request.method == "POST":
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            # first_name = subscribe_form.cleaned_data['first_name']
            # last_name = subscribe_form.cleaned_data['last_name']
            # email = subscribe_form.cleaned_data['email']
            # Subscribe.objects.create(first_name=first_name, last_name=last_name, email=email)
            return redirect(reverse('thank_you'))
    return render(request, 'subscribe/subscribe.html',
                  context={'form': subscribe_form})


def thank_you(request):
    return render(request, template_name="subscribe/thank_you.html")
