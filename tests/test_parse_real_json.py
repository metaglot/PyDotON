import sys
import json
import pathlib
from pydoton import Doton

# class Graph

# exit(0)

# class Assembler:
#     def __init__(self) -> None:
#         self.assembly = []


def dfj(path: str) -> dict:
    return json.loads(pathlib.Path(path).read_text())

maxasm = Doton(None, file="max_patcher/asm2.maxpat")

dependencies = Doton({
    f"{'.'.join(str(x.name).split('.')[0:-1])}":dfj(f"max_patcher/{x.patcherrelativepath}/{x.name}") for x in maxasm.patcher.dependency_cache
    }) 

# print(dependencies[[str(dep) for dep in dependencies][0]])
# print(maxasm)


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




def test_parse_maxpatcher():
    for box in maxasm.patcher.boxes:
        obj = box.box
        args = get_args_from_id(str(obj.id))
        print(f"({obj.id}) {get_name_from_id(str(obj.id))} {args if args else ''}")


    for edge in maxasm.patcher.lines:
        print(len(edge.patchline.source))
        src, outlet, *_ = edge.patchline.source
        dest, inlet, *_ = edge.patchline.destination
        print(f"----> ({src}) {get_name_from_id(str(src))},{outlet} ----> ({dest}) {get_name_from_id(str(dest))}, {inlet}")

# maxp = Doton(None, file="max_patcher/maxpatcher.json")
# p = maxp.patcher
# ver = p.appversion
# print(f"Max version: {ver.major}.{ver.minor}.{ver.revision}")
# for boxcontainer in p.boxes:
#     boxid = boxcontainer.box.id
#     if 'text' in boxcontainer.box:
#         print(f"({boxid}) {boxcontainer.box.text}")
#     else:
#         print(f"({boxid}) {{{boxcontainer.box.maxclass}}}")

# dac_id = [box.box.id for box in p.boxes if 'text' in box.box and box.box.text == "dac~"]

# print(dac_id)

# # print(object_ids)


# # for p in maxp._json:
# #     print(p)