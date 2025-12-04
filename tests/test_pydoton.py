import json
import pathlib
from types import NoneType
from pydoton import Doton

test_folder_path = pathlib.Path(__file__).parent


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

    pjson.new_key.another_new_list.doton_value().extend([23,31,37])

    assert len(pjson.new_key.another_new_list) == 3
    assert len(pjson.chungis.prior) == 4
    assert pjson.chungis.prior.doton_type_test(list)
    assert not pjson.chungis.prior.doton_type_test(dict)
    assert isinstance(pjson.chungis.prior[0], int)
    assert isinstance(pjson.dingus.thingie.someval, str)
    assert type(pjson.new_key.some_new_key) == type(None)
    assert f"{pjson.new_key.some_new_key}" == "None"


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


def test_reading_writing_consistency():
    print("")
    writefile = pathlib.Path(test_folder_path / "writetest_deleteme.json")
    json_test_file = pathlib.Path(test_folder_path / "test.json")
    json_string = json.dumps(json.loads(json_test_file.read_text()))
    print(f"loaded from disk: {json_string}")

    # testing JSON attribute-based construction
    jd = Doton()
    jd.key_array = [1,2,3,4]
    jd.subobject = {
        "string_val": "some string value"
    }
    jd.subobject.third_level = {
        "another_string": "value goes here",
        "list_of_some_primes": [3,5,7,23,37]
    }
    jd.a_float = 1.23
    jd.an_int = 1
    jd.a_boolean = True
    jd.a_null = None
    jd.tailstring = "last key"

    # writing JSON to disk
    jd.doton_writefile(writefile)

    # reading and serializing
    new_json_string = json.dumps(Doton(file=str(writefile)).doton_dict())

    # clean after testing
    writefile.unlink()

    print(f"constructed using dot notation: {new_json_string}")
    assert new_json_string == json_string
    print("")


def test_parse_maxpatcher():
    def dfj(path: str) -> dict:
        return json.loads(pathlib.Path(path).read_text())

    maxasm = Doton(None, file=str(test_folder_path / "max_patcher/asm2.maxpat"))

    # dependencies = Doton({
    #     f"{'.'.join(str(x.name).split('.')[0:-1])}":dfj(f"max_patcher/{x.patcherrelativepath}/{x.name}") for x in maxasm.patcher.dependency_cache
    #     }) 

    def parse_args(candidate: str) -> list[str|int|float]:
        args = candidate.split(' ')[1:]
        def try_parse(c: str) -> str|int|float:
            try:
                i = int(c)
                return i
            except:
                try:
                    f = float(candidate)
                    return f
                except:
                    return c
        return [try_parse(c) for c in args]
        

    def get_name_from_id(id: str) -> str:
        nc, *_ = [str(n.box.text).split(" ")[0] for n in maxasm.patcher.boxes if n.box.id == id]
        return nc

    def get_args_from_id(id: str) -> list[str|int|float]:
        nc, *_ = [parse_args(str(n.box.text)) for n in maxasm.patcher.boxes if n.box.id == id]
        return nc


    for box in maxasm.patcher.boxes:
        obj = box.box
        args = get_args_from_id(str(obj.id))
        print(f"({obj.id}) {get_name_from_id(str(obj.id))} {args if args else ''}")


    for edge in maxasm.patcher.lines:
        print(len(edge.patchline.source))
        src, outlet, *_ = edge.patchline.source
        dest, inlet, *_ = edge.patchline.destination
        print(f"----> ({src}) {get_name_from_id(str(src))},{outlet} ----> ({dest}) {get_name_from_id(str(dest))}, {inlet}")


def test_for_loop():
    l1 = [2,3,5,7,11,13,17,19]
    o1 = {
        "first_key": "first value",
        "second_key": "second value",
        "third_key": "third value",
    }

    print()
    d1 = Doton({
        "an_array": [2,3,5,7,11,13,17,19],
        "an_object": {
            "first_key": "first value",
            "second_key": "second value",
            "third_key": "third value",
        }
    })
    
    for list_item, li in zip(d1.an_array, l1):
        print(f"{list_item} == {li}")
        assert list_item == li

    for dict_key, dk in zip(d1.an_object, o1):
        print(f"{dict_key} == {dk}")
        assert dict_key == dk
    
    print()


def test_deletion():
    print()
    d1 = Doton({
        "del_by_item": 1,
        "del_by_attr": 2,
        "remaining": "key"
    })

    del d1.del_by_attr
    del d1['del_by_item']

    print(d1)

    assert 'del_by_attr' not in d1
    assert 'del_by_attr' not in d1
    print()


