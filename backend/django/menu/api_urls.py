from rest_framework import routers
from phone_numbers.views import PhoneNumberViewSet

# Create new instance of routers.DefaultRouter class and assign it to router variable
router = routers.DefaultRouter()
# Call register method on the router instance to register our PhoneNumberViewSet with the router
# First argument specifies base URL, second argument is the view class we want to register with the router
router.register(r'phone-numbers', PhoneNumberViewSet)
# Set urlpatterns to routers.urls, which is a list of automatically generated URL patterns for our viewset
urlpatterns = router.urls
