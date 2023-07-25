# Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes, which can then be
# converted into JSON, XML, or other content types. Serializers also provide deserialization, allowing parsed data to be converted back
# into complex types, after first validating the incoming data.

from rest_framework import serializers
from .models import PhoneNumber

# Define a new sterializer Class that inherits the default behavior of the ModelSerializer class
class PhoneNumberSerializer(serializers.ModelSerializer):
    # Define a nested Meta Class to specify metadata for the serializer
    class Meta:
        # Set the model attribute to PhoneNumber to specify that this serializer should handle instances of the PhoneNumber model
        model = PhoneNumber
        # Set the fields attribute to a list of field names to specify which fields should be included in the serialized representation of the model
        fields = ['id', 'number']