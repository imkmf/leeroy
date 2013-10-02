Leeroy
===

Leeroy is a WIP status page for Jenkins builds written in Django.

I don't know Django.

So this will be fun.

Install
---

I like using [virtualenvwrapper][venvw] (and, of course, [virtualenv][venv]).

```
mkvirtualenv leeroy
workon leeroy
pip install -r requirements
```

Heyo! We have lift-off. Let's get this party started.

```
python manage.py syncdb
python manage.py runserver
```

If you use [tmuxinator], you might find this [config file][muxfile] useful.

[venvw]: http://virtualenvwrapper.readthedocs.org/en/latest/
[venv]: https://pypi.python.org/pypi/virtualenv
[tmuxinator]: https://github.com/aziz/tmuxinator
[muxfile]: https://github.com/imkmf/leeroy/blob/master/leeroy.yml
