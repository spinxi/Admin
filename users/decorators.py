from functools import wraps
from django.shortcuts import redirect
from django.http import HttpResponse


def driver_access(user):
	if user.is_driver:
		return True
	return False

# def teacher_test_function(user):
# 	if user.is_accountant:
# 		return True
# 	return False


# def principal_test_function(user):
# 	if user.is_dispatcher:
# 		return True
# 	return False


def driver_access_only():
	def decorator(view):
		@wraps(view)
		def _wrapped_view(request, *args, **kwargs):
			if not driver_access(request.user):
				return HttpResponse("You are not a student and \
						you are not allowed to access this page !")
			return view(request, *args, **kwargs)
		return _wrapped_view
	return decorator


# def teacher_access_only(view_to_return="user_urls:home-page"):
# 	def decorator(view):
# 		@wraps(view)
# 		def _wrapped_view(request, *args, **kwargs):
# 			if not teacher_test_function(request.user):
# 				messages.error(request, "You cannot access \
# 								the teachers page !")
# 				return redirect(view_to_return)
# 			return view(request, *args, **kwargs)
# 		return _wrapped_view
# 	return decorator


# def principal_access_only(message_to_deliver="Not allowed to \
# 			access the principal's page , login as principal !"):
# 	def decorator(view):
# 		@wraps(view)
# 		def _wrapped_view(request, *args, **kwargs):
# 			if not principal_test_function(request.user):
# 				messages.error(request, message_to_deliver)
# 				return redirect("user_urls:login-user")
# 			return view(request, *args, **kwargs)
# 		return _wrapped_view
# 	return decorator
