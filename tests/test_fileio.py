import json
import pathlib
from pydoton import Doton


def test_reading_writing_consistency():
    print("")
    json_test_file = pathlib.Path("test.json")
    json_string = json.dumps(json.loads(json_test_file.read_text()))
    print(f"loaded from disk: {json_string}")
    jd = Doton(file=json_test_file)
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

    new_json_string = json.dumps(jd._json)
    print(f"constructed using dot notation: {new_json_string}")
    assert new_json_string == json_string
    print("")
    # # print(new_json_string)
    # pass