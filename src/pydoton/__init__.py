from __future__ import annotations
from typing import Optional, TypeAlias
from types import NoneType
import json
import pathlib

DScalar: TypeAlias = str | int | float | bool | NoneType
DObject: TypeAlias = dict[str, "DType"]
DArray: TypeAlias = list["DType"]
DType: TypeAlias = DObject | DArray | DScalar

class Doton():
    """
    A utility class for allowing dot-notation with json data

    valid types: object, array, number, string, Boolean, or null
    """
    # @staticmethod
    # def intval(val: str) -> int:
    #     m = re.match(r"[0-9]+", str(val))
    #     if m and m.string == str(val):
    #         return int(val)
    #     return -1
    _json:DType
    
    def __init__(self, ddata:Optional[DType] = None, **kwargs: str):

        if ddata is None: 
            if 'file' in kwargs:
                ddata = json.loads(pathlib.Path(kwargs['file']).read_text())
            else:
                ddata = {}
        self.__dict__['_json'] = ddata

    def __repr__(self):
        if isinstance(self._json, dict):
            return json.dumps(self._json, indent=4)
        return str(self._json)
    
    def __str__(self):
        if isinstance(self._json, dict):
            return json.dumps(self._json, indent=4)
        return str(self._json)

    def __getitem__(self, key: str|int) -> Doton|DScalar:
        if str(key).startswith("__"):
            return getattr(self, str(key))
        # if (isinstance(key, int) and isinstance(self._json, list)) or (isinstance(key, str) and key in self._json):
        not_valid_key_for_dict = isinstance(self._json, dict) and (str(key) not in self._json)
        not_valid_key_for_list = isinstance(key, int) and (0 > key >= len(self._json))
        if not_valid_key_for_dict or not_valid_key_for_list:
            raise KeyError(f"'{key}' not found")
        val = self._json[key]
        if isinstance(val, DScalar):
            return self._json[key]
        return Doton(self._json[key])
    
    def __setitem__(self, key:str|int, value: DType):
        if isinstance(self._json, DScalar):
            raise Exception("can't subscript scalar value")
        if isinstance(self._json, list) and isinstance(key, int):
            self._json[key] = value
        elif isinstance(self._json, dict) and isinstance(key, str):
            self._json[key] = value

    def __eq__(self, value: DScalar) -> bool:
        return value == self._json

    def __iter__(self):
        if isinstance(self._json, DScalar):
            raise Exception("can't iterate over scalar value")
        for t in self._json:
            yield Doton(t)

    def __getattr__(self, key: str):
        if key in self.__dict__['_json']:
            if isinstance(self.__dict__['_json'][key], str|int|bool|float|NoneType):
                return self.__dict__['_json'][key]
            return Doton(self.__dict__['_json'][key])
        raise KeyError(f"{key} not found")

    def __setattr__(self, key:str, value:DType):
        self.__dict__['_json'][key] = value

    def __len__(self):
        if not (isinstance(self._json, dict) or \
                isinstance(self._json, list) or \
                isinstance(self._json, str)):
            raise Exception(f"{type(self._json)} value doesn't have a length")
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