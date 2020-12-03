<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-listview-queryset.svg?maxAge=3600)](https://pypi.org/project/django-listview-queryset/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-listview-queryset.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-listview-queryset.py/actions)

### Installation
```bash
$ [sudo] pip install django-listview-queryset
```

#### Pros
+   custom `count()`

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
    <a href="https://readme42.com/">readme42.com</a>
</p>
