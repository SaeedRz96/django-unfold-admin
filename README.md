![enter image description here](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green) ![enter image description here](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)


## RTL Unfold Django Admin Panel Theme
This project is forked from https://github.com/unfoldadmin/django-unfold with RTL support.
<hr>

![Screenshot1](https://github.com/SaeedRz96/django-unfold-admin/blob/master/screenshots/loginform.png)

## How to install?
1.using pip to install package
```bash
pip install django-unfold-admin
```
2.add `unfold` to *settings.py* `INSTALLED_APPS`:
```python
    # settings.py
    INSTALLED_APPS = [
        "unfold",  # before django.contrib.admin
        "django.contrib.admin",
        .
        .
        .
    ]
```


3.now you can use `ModelAdmin` class defined in `unfold.admin` in *admin.py* :
```python
    # admin.py
    
    from django.contrib import admin
    from unfold.admin import ModelAdmin
    
    @admin.register(MyModel)
    class CustomAdminClass(ModelAdmin):
        pass
```

thats that! 

## Features

 - RTL support
 - Dark mode is available
 - Persian font Vazir included
 - Responsive design


## ScreenShots
![Screenshot2](https://github.com/SaeedRz96/django-unfold-admin/blob/master/screenshots/lightmode.png)

![Screenshot3](https://github.com/SaeedRz96/django-unfold-admin/blob/master/screenshots/darkmode.png)
