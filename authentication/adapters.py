# authentication/adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit=False)
        # Only set course/semester if this is a new user
        if not user.pk:
            user.course = None
            user.semester = None
        if commit:
            user.save()
        return user