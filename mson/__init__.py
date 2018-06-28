# This comment block is from JSON source. Included here for tests.
r"""JSON (JavaScript Object Notation) <http://json.org> is a subset of
JavaScript syntax (ECMA-262 3rd edition) used as a lightweight data
interchange format.

:mod:`json` exposes an API familiar to users of the standard library
:mod:`marshal` and :mod:`pickle` modules.  It is derived from a
version of the externally maintained simplejson library.

Encoding basic Python object hierarchies::

    >>> import mson
    >>> mson.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    '["foo", {"bar": ["baz", null, 1.0, 2]}]'
    >>> print(mson.dumps("\"foo\bar"))
    "\"foo\bar"
    >>> print(mson.dumps('\u1234'))
    "\u1234"
    >>> print(mson.dumps('\\'))
    "\\"
    >>> print(mson.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
    {"a": 0, "b": 0, "c": 0}
    >>> from io import StringIO
    >>> io = StringIO()
    >>> mson.dump(['streaming API'], io)
    >>> io.getvalue()
    '["streaming API"]'

Compact encoding::

    >>> import mson
    >>> mydict = {'4': 5, '6': 7}
    >>> mson.dumps([1,2,3,mydict], separators=(',', ':'))
    '[1,2,3,{"4":5,"6":7}]'

Pretty printing::

    >>> import mson
    >>> print(mson.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
    {
        "4": 5,
        "6": 7
    }

Decoding JSON::

    >>> import mson
    >>> obj = ['foo', {'bar': ['baz', None, 1.0, 2]}]
    >>> mson.loads('["foo", {"bar":["baz", null, 1.0, 2]}]') == obj
    True
    >>> mson.loads('"\\"foo\\bar"') == '"foo\x08ar'
    True
    >>> from io import StringIO
    >>> io = StringIO('["streaming API"]')
    >>> mson.load(io)[0] == 'streaming API'
    True

Specializing JSON object decoding::

    >>> import mson
    >>> def as_complex(dct):
    ...     if '__complex__' in dct:
    ...         return complex(dct['real'], dct['imag'])
    ...     return dct
    ...
    >>> mson.loads('{"__complex__": true, "real": 1, "imag": 2}',
    ...     object_hook=as_complex)
    (1+2j)
    >>> from decimal import Decimal
    >>> mson.loads('1.1', parse_float=Decimal) == Decimal('1.1')
    True

Specializing JSON object encoding::

    >>> import mson
    >>> def encode_complex(obj):
    ...     if isinstance(obj, complex):
    ...         return [obj.real, obj.imag]
    ...     raise TypeError(f'Object of type {obj.__class__.__name__} '
    ...                     f'is not JSON serializable')
    ...
    >>> mson.dumps(2 + 1j, default=encode_complex)
    '[2.0, 1.0]'
    >>> mson.JSONEncoder(default=encode_complex).encode(2 + 1j)
    '[2.0, 1.0]'
    >>> ''.join(mson.JSONEncoder(default=encode_complex).iterencode(2 + 1j))
    '[2.0, 1.0]'


Using mson.tool from the shell to validate and pretty-print::

    $ echo '{"mson":"obj"}' | python -m mson.tool
    {
        "mson": "obj"
    }
    $ echo '{ 1.2:3.4}' | python -m mson.tool
    Expecting property name enclosed in double quotes: line 1 column 3 (char 2)
"""
__author__ = 'Mark Silva'
__email__ = 'github@markesilva.com'
__version__ = '0.1.0'


import json
from json.decoder import JSONDecoder  # noqa: F401
from json.encoder import JSONEncoder  # noqa: F401
import re

# whole line comment
comment_re = re.compile(r'^(\s*#.*$)')
comma_re = re.compile(r',(\s*[\}|\]])')


def detect_encoding(b):
    return json.detect_encoding(b)


def dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True,
         allow_nan=True, cls=None, indent=None, separators=None,
         encoding='utf-8', default=None, **kw):
    return json.dump(
        obj, fp, skipkeys, ensure_ascii, check_circular,
        allow_nan, cls, indent, separators,
        encoding, default, kw)


def dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True,
          allow_nan=True, cls=None, indent=None, separators=None,
          encoding='utf-8', default=None, **kw):
    return json.dumps(
        obj, skipkeys, ensure_ascii, check_circular,
        allow_nan, cls, indent, separators,
        encoding, default, kw)


def load(fp, encoding=None, cls=None, object_hook=None, parse_float=None,
         parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
    s = fp.read()
    return loads(
        s, encoding, cls, object_hook, parse_float,
        parse_int, parse_constant, object_pairs_hook, kw)


def loads(s, encoding=None, cls=None, object_hook=None, parse_float=None,
          parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
    return json.loads(
        s, encoding, cls, object_hook, parse_float,
        parse_int, parse_constant, object_pairs_hook, kw)
