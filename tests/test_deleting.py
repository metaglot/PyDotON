from pydoton import Doton


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