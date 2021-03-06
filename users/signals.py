from django.contrib.auth.models import User
from .models import Profile

# https://docs.djangoproject.com/en/4.0/topics/signals/
# Import Django Signals
from django.db.models.signals import post_save
from django.db.models.signals import post_delete


# Signal Reciever Function (post_save)
# Create a Profile when any user Registered
def createProfile(sender , instance , created , **kwargs ):
    if created:
        newUser = instance
        newProfile = Profile.objects.create(
            user = newUser,
            username = newUser.username,
            email = newUser.email,
            name = newUser.first_name
        )

post_save.connect(createProfile , sender=User)



# Signal Reciever Function (post_save)
# Update User Info when his Profile Updated 
def updateUser(sender , instance , created , **kwargs ):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()

post_save.connect(updateUser , sender=Profile)



# Signal Reciever Function (post_delete)
# Delete User if his Profile Deleted
def deleteUser (sender , instance ,**kwargs):
    deletedUser = instance.user
    deletedUser.delete()

post_delete.connect(deleteUser , sender=Profile)