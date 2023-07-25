from django.shortcuts import render, redirect
from .models import PhoneNumber
from rest_framework import viewsets
from .serializers import PhoneNumberSerializer
from django.http import JsonResponse

# Declare view function for handling the submission of the form to add a new phone number
def add_phone_number(request):
    # Check if the request is a POST request
    if request.method == 'POST':
        # Get the phone number from the submitted form data
        number = request.POST.get('number')
        # Create a new PhoneNumber object with the submitted number
        phone_number = PhoneNumber(number=number)
        # Save the new phone number to the database
        phone_number.save()
        # Redirect the user back to the form
        return redirect('add_phone_number')
    # If the request is not a POST request, display the form
    return render(request, 'add_phone_number.html')

# Declare view function for displaying a list of all saved phone numbers
def list_phone_numbers(request):
    # Get all phone numbers from the database
    phone_numbers = PhoneNumber.objects.all()
    # Create a context dictionary to pass data to the template
    context = {'phone_numbers': phone_numbers}
    # Render the template with the context data
    return render(request, 'list_phone_numbers.html', context)

# Declare view function for deleting phone numbers 
def delete_phone_number(request, phone_number_id):
    # Get the phone number object from the database
    phone_number = PhoneNumber.objects.get(id=phone_number_id)
    # Delete the phone number
    phone_number.delete()
    # Redirect the user back to the list of phone numbers
    return redirect('list_phone_numbers')

# Declare view class for handling API requests
class PhoneNumberViewSet(viewsets.ModelViewSet):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer