import json
from types import NoneType
from .pydoton import Doton


def test_pydoton_json_parsing_and_integrity():
    pjson = Doton({
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

    pjson.new_key = {
        "some_new_key": None,
        "new_scalar": 5,
        "new_list": [5, 7, 11],
        "another_new_list": []
    }

    pjson.new_key.another_new_list.value().extend([23,31,37])

    assert len(pjson.new_key.another_new_list) == 3
    assert len(pjson.chungis.prior) == 4
    assert pjson.chungis.prior.is_type(list)
    assert not pjson.chungis.prior.is_type(dict)
    assert isinstance(pjson.chungis.prior[0], int)
    assert isinstance(pjson.dingus.thingie.someval, str)
    assert type(pjson.new_key.some_new_key) == type(None)
    assert f"{pjson.new_key.some_new_key}" == "None"

    # pjson.new_key.another_new_list.append(1)
    # pjson.new_key.another_new_list.append(2)
    # pjson.new_key.another_new_list.append(7)

    # print(pjson)

def test_object_construction_and_types():
    v = Doton()
    v.first = "yes this"
    v.second = "another this"
    v.nonetype = None
    v.booltype = True
    v.inttype = 123
    v.floattype = 123.123
    v.stringtype = "string here"
    v.third = {}
    v.third.dingus = "some value"
    vv = json.loads(str(v))

    print(v)
    assert vv['first'] == v.first
    assert vv['second'] == v.second
    assert vv['third']['dingus'] == v.third.dingus
    assert isinstance(v.nonetype, NoneType)
    assert isinstance(v.booltype, bool)
    assert isinstance(v.inttype, int)
    assert isinstance(v.floattype, float)
    assert isinstance(v.stringtype, str)
    assert isinstance(vv['nonetype'], NoneType)
    assert isinstance(vv['booltype'], bool)
    assert isinstance(vv['inttype'], int)
    assert isinstance(vv['floattype'], float)
    assert isinstance(vv['stringtype'], str)



def test_abuse():
    v = Doton()
    v.first = "some string"
    v.second = [1,2,3]
    v.third = {}
    v.third.item1 = "some bunk"
    v.third.item2 = "some bunkerz"
    print("")
    did_fail = False
    try:
        print("expects 'subkey not found':")
        print(v.second.subkey)
    except KeyError as ke:
        print(ke)
        did_fail = True
    assert did_fail

    did_fail = False
    try:
        print("expects '0 not found'")
        print(v.third[0])
    except KeyError as ke:
        print(ke)
        did_fail = True
    assert did_fail
    print("")