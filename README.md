## Django TalkTo

[![Updates](https://pyup.io/repos/github/sirrobot01/djangotalkto/shield.svg)](https://pyup.io/repos/github/sirrobot01/djangotalkto/)
[![Python 3](https://pyup.io/repos/github/sirrobot01/djangotalkto/python-3-shield.svg)](https://pyup.io/repos/github/sirrobot01/djangotalkto/)


### Overview

Django TalkTo allows you to consume RESTful APIs seamlessly without need to create database

##### Model
- **TalkToModel**, inherits the django Model class, but won't create any migration files, :smiley:
- **APIManager**, inherits Django Manager(I won't touch your DB i promise :yum: )

##### ModelForm
- **TalkToModelForm**, inherits Django ModelForm.

##### Views

- **TalkToWriteView** which makes `POST/PUT` request to an endpoint (Django CreateView and UpdateView in one pot :wink: )

- **TalkToListView** which makes `GET` request to an endpoint (Django ListView, no bigs)

- **TalkToDetailView** which makes `GET` request with a parameter (Django DetailView)


#### [Django Rest Framework](https://www.django-rest-framework.org/) support

You can also use Django TalkTo with [Django Rest Framework](https://www.django-rest-framework.org/)



###### Serializer

- **TalkToModelSerializer**, inherits DRF ModelSerializer, that won't touch the DB, cool right?


###### View

- **TalkToAPIView** which makes `POST`, `GET` and `PUT` requests. `DELETE` requests coming soon.


***

### Installation

Install using pip

    pip install djangotalkto

**Notes to [Django Rest Framework](https://www.django-rest-framework.org/) users**
 
You need to have djangorestframework installed and added to **INSTALLED_APPS** in settings. You can install it with djangotalkto using
 
    pip install djangotalkto[rest]
    

***

### Usage

Start a new django project

    pip install django
    django-admin startproject newproj .
    pip install djangotalkto
    

Add `'talkto'` to `INSTALLED_APPS` in your project settings

Then create TALKTO dict in your settings with the following properties


    TALKTO = {
        'default': {
            'URL': 'your-api-base-url', #Important!
            'HEADERS': {key: value}, # You can add your Authorization here
        }
    
    }
    

##### Creating your Model

    from talkto.models import TalkToModel, APIManager
    from django.db import models
    class SampleModel(TalkToModel):
        name = models.CharField(max_length=255)
        age = models.IntegerField()
        
        # Then add your APIManager with the variable name 'api'
        
        api = APIManager(path='user/')
        
        # 'path' in this case is the path you will be making your request which is 
        # concatenated with the URL set in TALKTO config in settings.py
        
        
        

##### Creating your ModelForm is much like the same.

    from talkto.forms import TalkToModelForm
    
    
    class SampleForm(TalkToModelForm):
        class Meta:
            model = SampleModel
            fields = '__all__'
        
  
##### Views
    from talkto.views import TalkToWriteView, TalkToDetailView, TalkToListView

    class TestCreate(TalkToWriteView):
        form_class = SampleForm
        model = SampleModel
        success_url = reverse_lazy('books')
        template_name = 'index.html'
      
    # Detail view
      
    class SampleDetail(TalkToDetailView):
        model = SampleModel
        template_name = 'detail.html'
        
        
    # List view
    
    class SampleList(TalkToListView):
        model = SampleModel
        template_name = 'detail.html'
        
    
**URLConf works the same.**

##### Django Rest Framework

###### Serializer
    from talkto.serializer import TalkToModelSerializer
    
    class SampleSerializer(TalkToModelSerializer):
        class Meta:
            model = SampleModel
            fields = '__all__'
            
###### API View

    class SampleView(TalkToAPIView):
        model = SampleModel
        serializer_class = SampleSerializer
        
        
**URLConf works the same.**


***

### CONTRIBUTING

coming soon....

***

### Supports

As this is still in it's early project there might be some use cases that are not covered.
Therefore you can contact me using the following channels.

- Follow me on [Twitter](https://twitter.com/sirrobot01)
- Follow me on [Reddit](https://www.reddit.com/user/sirrobot01)

