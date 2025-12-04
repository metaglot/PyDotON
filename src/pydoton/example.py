from pydoton import Doton

jdata = Doton({
    "an_array": [1,2,3,4],
    "an_object": {
        "string_key": "some string value",
        "another_object": {
            "another_string": "value goes here",
            "list_of_some_primes": [3,5,7,23,37]
        }
    },
    "a_float": 1.23,
    "an_int": 1,
    "a_boolean": True,
    "a_null": None,
    "tailstring": "last key"
})


def is_prime(pc: int):
    for i in range(2, -2 + int(pc)):
        if (((pc // i) * i) == pc):
            return False
    return True


assert jdata.an_array[0] == 1
jdata.an_array[0] = 11
assert jdata['an_array'][0] == 11

assert jdata.an_object.another_object.another_string == "value goes here"

for l in jdata.an_object.another_object.list_of_some_primes:
    print(l)
    assert is_prime(l)

# assert is_prime(37)