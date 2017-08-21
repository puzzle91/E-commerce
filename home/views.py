from django.shortcuts import render
from .models import Contact

# Create your views here.
def get_index(request):
    return render(request, 'index.html')

def delete_contact(request, id):
    contact = get_object_or_404(Contact, pk=id)
    contact.delete()
    return render(request, 'index.html')


def do_search(request):
    contacts = Contact.objects.filter(name__contains=request.GET['q'])
    return render(request, 'results.html', {'contacts': contacts})