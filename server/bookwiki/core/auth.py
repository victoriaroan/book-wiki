from django.contrib.auth.backends import ModelBackend

class ObjectOwnerPermissionBackend (object):
    def has_perm(self, user_obj, perm, obj=None, owner_field='owner'):
        if not obj:
            return False
        
        if getattr(obj, owner_field) == user_obj.pk:
            return True
        else:
            return False
