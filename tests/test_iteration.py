from pydoton import Doton

l1 = [2,3,5,7,11,13,17,19]
o1 = {
    "first_key": "first value",
    "second_key": "second value",
    "third_key": "third value",
}

def test_for_loop():
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