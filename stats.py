
def words_in_string(text:str)->int:
    word_list = text.split()
    return len(word_list)

def char_counter(text:str)->dict[str,int]:
    res:dict[str,int] = {}
    for char in text:
        c = char.lower()
        if res.get(c) is None:
            res[c] = 1
        else:
            res[c] += 1
    return res

def sort_dict_by_val(data:dict[str,int]) -> list[dict[str,str|int]]:
    res:list[dict[str,str|int]] = []
    for key,val in data.items():
        res.append({"char":key, "num":val})
    res.sort(reverse=True, key=lambda d:d["num"])
    return res


