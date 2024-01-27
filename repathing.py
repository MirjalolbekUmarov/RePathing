from django.urls import path, include

class Modify:
    def __init__(self, urls: dict):
        """
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

        # Use the modify_urlpatterns function to modify urlpatterns
        urlpatterns = Modify({'home/': {"": Home, "<int:pk>/": Post}})
        ```
        """
        self.urls = urls
        
    def __repr__(self) -> list:
        def re_dict(input_dict, parent_key='', sep=''):
            output_dict = {}
            for key, value in input_dict.items():
                new_key = f"{parent_key}{key}{sep}" if parent_key else key
                if isinstance(value, dict):
                    output_dict.update(re_dict(value, new_key, sep=sep))
                else:
                    output_dict[new_key] = value
            return output_dict
        return [path(x, y) for x, y in re_dict(self.urls).items()]
