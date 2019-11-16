<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
https://pypi.org/project/django-readme-generator/
-->

[![](https://img.shields.io/badge/language-Python-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/django-listview-queryset.svg?maxAge=3600)](https://pypi.org/project/django-listview-queryset/)
[![Travis](https://api.travis-ci.org/andrewp-as-is/django-listview-queryset.py.svg?branch=master)](https://travis-ci.org/andrewp-as-is/django-listview-queryset.py/)

#### Installation
```bash
$ [sudo] pip install django-listview-queryset
```

#### Pros
+   custom `count()`

#### Classes
class|`__doc__`
-|-
`django_listview_queryset.ListViewQuerySet` |
`django_listview_queryset.ListViewRawQuerySet` |

#### Examples
`ListViewQuerySet`

```python
from django_listview_queryset import ListViewQuerySet

class Name(models.Model):
    objects = ListViewQuerySet.as_manager()
```
```python
q = Name.objects.filter().order_by().setcount(42)
```

`ListViewRawQuerySet`

```python
from django_listview_queryset import ListViewRawQuerySet

class Name(models.Model):
    objects = ListViewRawQuerySet.as_manager()
```
```python
q = Name.objects.raw('select * from table').setcount(42)
```

<p align="center">
    <a href="https://pypi.org/project/django-readme-generator/">django-readme-generator</a>
</p>