from django.shortcuts import redirect

class AccountsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        
        restricted_paths = ("/accounts/login/", "/accounts/register/")
        # path = request.path
        if request.user.is_authenticated and request.path in restricted_paths:
            return redirect("app:dashboard")       
        
        response = self.get_response(request)
        return response
