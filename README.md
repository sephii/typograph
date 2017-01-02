Typograph
=========

Typograph is a Python library that allows you to automatically fix typography mistakes that are commonly done when
writing content on the web. Typograph allows you to define sets of rules for different languages. The current version
only supports french and does the following:

* Replace straight quotes by guillemets
* Add narrow non-breaking spaces before and after specific punctuation

Installation
------------

Simply install it with PyPI:

```bash
pip install typograph
```

As a standalone Python module
-----------------------------

To use the default set of regular expressions, just call `get_typograph` with the language to use for transformations:

```python
>>> from typograph import get_typograph
>>> formatter = get_typograph('fr')
>>> formatter('"bonjour le monde!")
'«\u202fbonjour le monde\u202f!\u202f»'
```

You can also specify the regular expressions you want to use:

```python
>>> from typograph import get_typograph
>>> formatter = get_typograph('fr', base_regexps=[(r'bonjour', 'bonsoir')])
>>> formatter('bonjour le monde')
'bonsoir le monde'
```

Finally you can also override the language-specific regular expressions:

```python
>>> from typograph import get_typograph
>>> formatter = get_typograph('fr', i18n_regexps={'fr': [(r'bonjour', 'bonsoir')]})
>>> formatter('bonjour le monde')
'bonsoir le monde'
```

If your input string is HTML, make sure to specify it so that your HTML doesn't get messed up.

**Don't do that!**

```python
>>> from typograph import get_typograph
>>> formatter = get_typograph('fr')
>>> formatter('<p class="large">Hello world!</p>')
'<p class=«\u202flarge\u202f»>Hello world\u202f!</p>'
```

**Instead, set the `is_html` parameter to `True`:**

```python
>>> from typograph import get_typograph
>>> formatter = get_typograph('fr')
>>> formatter('<p class="large">Hello world!</p>', is_html=True)
'<p class="large">Hello world\u202f!</p>'
```

You can set either a partial language code, eg. *fr*, or a language code along with a variant, eg. *fr-ch*. This is
true for both the `language` parameter of the `get_typograph` function and for the list of language-specific regular
expressions, allowing you to use different rules for variations of the same language.

```python
>>> from typograph import get_typograph
>>> from typograph.regexps import I18N_REGEXPS
>>> formatter = get_typograph('fr-ch')
>>> formatter('hello world!') # this will use the regexps from the 'fr' set
'hello world\u202f!'
>>> new_i18n_regexps = I18N_REGEXPS.copy()
>>> new_i18n_regexps['fr-ch'] = [(r'^(\w)', lambda match: match.group(1).upper())]
>>> formatter('hello world!', i18n_regexps=new_i18n_regexps)
'Hello world\u202f!'
```

On the other side, regular expressions from a specific variant (eg. *fr-ch*) won't be applied if the input has either a
different variant or no variant at all:

```python
>>> from typograph import get_typograph
>>> formatter = get_typograph('fr', i18n_regexps={'fr-ch': [(r'hello', 'bonjour')]})
>>> formatter('hello world!')
'hello world!'
```

As a Django app
---------------

Add `typograph` to your `INSTALLED_APPS` in your settings file (its position doesn't matter):

```python
INSTALLED_APPS = (
    # ...
    'typograph',
)
```

You can now use the `typograph_text` and `typograph_html` filters in your templates. The following will output `hello
world !` if the current language is french.

```jinja
{% load typograph %}
{{ "hello world!"|typograph_text }}
```

You should use `typograph_html` when you expect your content to be HTML. Its text will then be extracted so that the
contents of the tags themselves are not changed.

The following settings are available:

**TYPOGRAPH_BASE_REGEXPS**

Regular expressions that will be applied to all input strings, no matter the language.

Default: `[]`.

**TYPOGRAPH_I18N_REGEXPS**

Regular expressions that will be applied depending on the input language.

Default:
```python
{
    'fr': [
        REPLACE_STRAIGHT_QUOTES_BY_GUILLEMETS, ADD_NBSP_BEFORE_PUNCTUATION,
        ADD_NBSP_AFTER_PUNCTUATION,
    ]
}
```

**TYPOGRAPH_HTML_PARSER**

HTML parser to use when processing HTML. It is recommended to use the `lxml` parser. To see the list of
supported HTML parsers, refer to the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#specifying-the-parser-to-use) documentation.

Default: `html.parser`.

As a DjangoCMS plugin processor
-------------------------------

To get the content from all your DjangoCMS text plugins processed by Typograph, set the following in your settings
file:

```python
CMS_PLUGIN_PROCESSORS = (
    'typograph.cms_plugins_processors.typograph_plugin',
)
```
