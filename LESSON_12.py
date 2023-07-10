# 1. Write a decorator that ensures a function is only called by users with a specific role.
# Each function should have an user_type with a string type in kwargs. Example:

from functools import wraps

def is_admin(status):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user_type = kwargs.get('user_type')
            if user_type == status:
                return func(*args, **kwargs)
            else:
                raise ValueError("Unauthorized access: Permission denied.")
        return wrapper
    return decorator

@is_admin('admin')
def admin_func(**kwargs):
    print("This function can only be called by an admin.")

@is_admin('user')
def user_func(**kwargs):
    print("This function can only be called by a user.")

admin_func(user_type='admin')
user_func(user_type='user')

# 2. Write a decorator that wraps a function in a try-except block
# and prints an error if any type of error has happened.

def errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in function '{func.__name__}': {e}")
    return wrapper