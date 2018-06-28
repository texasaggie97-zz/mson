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
