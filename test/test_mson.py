"""
Tests for `mson` module.
"""
from decimal import Decimal
from io import StringIO
import pytest
import mson


def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct


def encode_complex(obj):
    if isinstance(obj, complex):
        return [obj.real, obj.imag]
    raise TypeError('Object of type {} is not JSON serializable'.format(obj.__class__.__name__))


class TestMson(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_basic(self):
        assert mson.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]) == '["foo", {"bar": ["baz", null, 1.0, 2]}]'
        # assert mson.dumps('\"foo/bar') == '\"foo/bar'
        # assert mson.dumps('\u1234') == "\u1234"
        # assert mson.dumps('\\') == "\\"
        assert mson.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True) == '{"a": 0, "b": 0, "c": 0}'
        io = StringIO()
        mson.dump(['streaming API'], io)
        assert io.getvalue() == '["streaming API"]'

    def test_basic_encoding(self):
        mydict = {'4': 5, '6': 7}
        assert mson.dumps([1,2,3,mydict], separators=(',', ':')) == '[1,2,3,{"4":5,"6":7}]'

    def test_basic_decoding(self):
        obj = ['foo', {'bar': ['baz', None, 1.0, 2]}]
        assert mson.loads('["foo", {"bar":["baz", null, 1.0, 2]}]') == obj
        assert mson.loads('"\\"foo\\bar"') == '"foo\x08ar'
        io = StringIO('["streaming API"]')
        assert mson.load(io)[0] == 'streaming API'


    def test_specialized_decoding(self):
        assert mson.loads('{"__complex__": true, "real": 1, "imag": 2}', object_hook=as_complex) == (1+2j)
        assert mson.loads('1.1', parse_float=Decimal) == Decimal('1.1')


    def test_specialized_encoding(self):
        assert mson.dumps(2 + 1j, default=encode_complex) == '[2.0, 1.0]'
        assert mson.JSONEncoder(default=encode_complex).encode(2 + 1j) == '[2.0, 1.0]'
        assert ''.join(mson.JSONEncoder(default=encode_complex).iterencode(2 + 1j)) == '[2.0, 1.0]'


    @classmethod
    def teardown_class(cls):
        pass
