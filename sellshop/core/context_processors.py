from .forms import ContactForm, SubscribeForm

def contact_renderer(request):
    contact_form = ContactForm()
    context = {
        'contact_form':contact_form
        }
    return context

def subscribe_renderer(request):
    subscribe_form = SubscribeForm()
    context = {
        'subscribe_form':subscribe_form
        }
    return context