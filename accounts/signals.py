from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import UserProfile, User

@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    print(created)
    if created: 
       UserProfile.objects.create(user=instance)
       print('user profile created')
    else:
        try:               
            profile=UserProfile.objects.get(user=instance)
            profile.save() 
        except UserProfile.DoesNotExist:
            UserProfile.objects.create(user=instance)
            print('user profile wasn\'t but i created one')
        print('user profile is updated')
        
@receiver(pre_save, sender=User)
def pre_save_user_profile(sender, instance, **kwargs):
    print(instance.username, 'this user is being saved')
         
    #     instance.userprofile.save()
@receiver(post_save, sender=User)
def post_save_user_profile(sender, instance, **kwargs):
    print(instance.username, 'this user has just been created')
