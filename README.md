# RePathing
Modify Django urlpatterns dynamically.

This class was created to make writing `urlpatterns` easier in the `Django` framework. But it is not possible to give a `name` parameter in a function.

Parameters:
- `urls (dict)`: The current `dict` of Django urls.

Returns:
`list`: The modified list of Django urls for `urlpatterns`

Example:
```
# Define your initial urlpatterns
urlpatterns = [
        path('home/', Home),
        path('home/<int:pk>/, Post)
]

# Use the Modify class to modify urlpatterns
urlpatterns = Modify({'home/': {"": Home, "<int:pk>/": Post}}).done()
```
