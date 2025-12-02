import sys
import json
import re

"""
goal: to understand python better

vehicle: to see if a class can be constructed that 
will take a slash-path into a json object, so that;

# given
json_object = {
    "dingus": {
        "thingie": {
            "someval": "yes, this"
        }
    }
}

# and
someval = json_object / "dingus" / "thingie" / "someval"

# then
assert someval=="yes, this"

"""

def intval(val: str) -> int:
    m = re.match(r"[0-9]+", str(val))
    if m and m.string == str(val):
        return int(val)
    return -1


class DotJson:
    def __init__(self, _json_obj):
        self.__dict__['_json'] = _json_obj
        pass

    def __truediv__(self, other):
        if other == str(intval(other)):
            other = int(other)

        if isinstance(other, str):
            token, *rest = other.split("/")
            if len(rest):
                return DotJson(self._json[token]).__truediv__("/".join(rest))

        if isinstance(self._json[other], dict) or \
            isinstance(self._json[other], list):
            return DotJson(self._json[other])
        
        return self._json[other]

    def __repr__(self):
        if isinstance(self._json, dict):
            return json.dumps(self._json, indent=4)
        return str(self._json)
    
    def __str__(self):
        if isinstance(self._json, dict):
            return json.dumps(self._json, indent=4)
        return str(self._json)

    def __getitem__(self, key):
        if str(key).startswith("__"):
            return getattr(self, key)
        return DotJson(self._json[key])
    
    def __setitem__(self, key, value):
        self._json[key] = value

    def __eq__(self, value):
        return value == self._json

    def get_value(self):
        return self._json

    def get_type(self):
        return type(self._json)
    
    def to_dict(self):
        return self.__dict__['_json']

    def is_type(self, compare_type):
        return type(self._json) == compare_type

    def __setattr__(self, key, value):
        self.__dict__['_json'][key] = value

    def __getattr__(self, key):
        if key in self.__dict__['_json']:
            return DotJson(self.__dict__['_json'][key])
        raise KeyError(f"{key} not found")

    def __len__(self):
        return len(self._json)



pjson = DotJson({
    "dingus": {
        "thingie": {
            "someval": "yes, this",
            "old_scalar": 5
        }
    },
    "chungis": {
        "prior": [1, 2, 3, 4]
    }
})


someval = pjson / "dingus" / "thingie"
assert (pjson / 'chungis' / 'prior' / 3) == 4
assert (isinstance((pjson / 'dingus'), DotJson))
assert (isinstance((pjson / 'chungis' / 'prior').get_value(), list))
prior_list = pjson / 'chungis' / 'prior'
assert (prior_list.get_type() == list)
assert (type(pjson / 'dingus' / 'thingie' / 'someval') == str)
# print(type(json_object / 'chungis' / 'prior'))
# print(list)
# assert (isinstance((json_object / 'chungis' / 'prior'), list))
# print(thingie)
# thingie["someval"] = "another yes"
# print(json_object['dingus'] / 'thingie')
# print(json_object)
# print(json_object / 'chungis' / 'prior' / 3)

someval = pjson / 'dingus' / 'thingie' / 'someval' # yes, this
assert someval == 'yes, this'
# print(f"someval: {json_object / 'dingus' / }")
# print(json_object["__div__"])

pjson.new_key = {
    "some_new_key": "new value",
    "new_scalar": 5,
    "new_list": [5, 7, 11],
    "another_new_list": []
}

assert prior_list.get_type() == (pjson / 'new_key' / 'new_list').get_type()

assert (pjson/'new_key/new_list/2') == (pjson / 'new_key' / 'new_list' / 2) # 11
assert (pjson/'dingus/thingie/old_scalar') == (pjson / 'new_key' / 'new_scalar') # 5
assert (pjson/'dingus/thingie/old_scalar') == pjson.new_key.new_scalar
is_not_a_nice_syntax = "sure isn't"

# prior_list
# pjson.new_key.new_list[0] = 13
# pjson.new_key.new_list[1] = 17
# pjson.new_key.new_list[2] = 19

pjson.new_key.another_new_list = [23,31,37]
# print(pjson)

assert (pjson / 'new_key/another_new_list/0') == 23
assert (pjson / 'new_key/another_new_list/1') == 31
assert (pjson / 'new_key/another_new_list/2') == 37

assert len(pjson.new_key.another_new_list) == 3
assert len(pjson.chungis.prior) == 4

assert pjson.chungis.prior.is_type(list)

assert not pjson.chungis.prior.is_type(dict)

assert pjson.chungis.prior[0].is_type(int)

assert pjson.new_key.some_new_key.is_type(str)

assert f"{pjson.new_key.some_new_key}" == "new value"

# (json_object)
# print(json_object)

"""

preliminary conclusion:
- while easier to read, it may lead to clumsier syntax and semantics when assigning
- square bracket operator (getitem / setitem) has the advantage of consistency
...

midliminary conclusion:
- it may still be possible without resorting to some clumsy syntax/semantics with __getattr__/__setattr__

TODO:
- handle all data types in JSON
- deal with limitations (certain names on json keys, like __*)
- implement name conversion (snake to camel to snake to camel?)


"""