from __future__ import annotations
from typing import Optional, Any
from types import NoneType
import json
import pathlib

class Doton():
    """
    A utility class for allowing dot-notation with json data
    """
    # @staticmethod
    # def intval(val: str) -> int:
    #     m = re.match(r"[0-9]+", str(val))
    #     if m and m.string == str(val):
    #         return int(val)
    #     return -1
    
    def __init__(self, _json_obj:Optional[Any] = None, **kwargs: str):
        if _json_obj is None and 'file' in kwargs:
            _json_obj = json.loads(pathlib.Path(kwargs['file']).read_text())
        elif _json_obj is None:
            _json_obj = {}
        self.__dict__['_json'] = _json_obj

    def __repr__(self):
        if isinstance(self._json, dict):
            return json.dumps(self._json, indent=4)
        return str(self._json)
    
    def __str__(self):
        if isinstance(self._json, dict):
            return json.dumps(self._json, indent=4)
        return str(self._json)

    def __getitem__(self, key: str|int) -> Doton|str|int|float|bool|NoneType:
        if str(key).startswith("__"):
            return getattr(self, str(key))
        # if (isinstance(key, int) and isinstance(self._json, list)) or (isinstance(key, str) and key in self._json):
        not_valid_key_for_dict = isinstance(self._json, dict) and (str(key) not in self._json)
        not_valid_key_for_list = isinstance(key, int) and (0 > key >= len(self._json))
        if not_valid_key_for_dict or not_valid_key_for_list:
            raise KeyError(f"{key} not found")
        val = self._json[key]
        if isinstance(val, str|int|float|bool|NoneType):
            return self._json[key]
        return Doton(self._json[key])
    
    def __setitem__(self, key, value):
        self._json[key] = value

    def __eq__(self, value):
        return value == self._json

    def __iter__(self):
        for t in self._json:
            yield Doton(t)

    def __getattr__(self, key: str):
        if key in self.__dict__['_json']:
            if isinstance(self.__dict__['_json'][key], str|int|bool|float|NoneType):
                return self.__dict__['_json'][key]
            return Doton(self.__dict__['_json'][key])
        raise KeyError(f"{key} not found")

    def __setattr__(self, key, value):
        self.__dict__['_json'][key] = value

    def __len__(self):
        return len(self._json)

    def value(self):
        return self._json

    def get_type(self):
        return type(self._json)
    
    def to_dict(self):
        return self.__dict__['_json']

    def is_type(self, compare_type: type) -> bool:
        return type(self._json) == compare_type

    def loadf(self, file: pathlib.Path | str):
        file = pathlib.Path(file)
        self.__dict__['_json'] = json.loads(file.read_text())
    
    def writef(self, file: pathlib.Path|str):
        file = pathlib.Path(file)
        file.write_text(self.__dict__['_json'])


__all__ = ['Doton']