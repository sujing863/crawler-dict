import jsonlines
import json


def deal_dict(file1, file2):
    f1 = open(file1, 'r', encoding='utf-8')
    f2 = open(file2, 'w', encoding='utf-8')
    items = jsonlines.Reader(f1)  # 按行读入文件
    final = []
    for item in items:
        temp = []
        str1 = item["more"]
        for idx, ch in enumerate(str1):
            if ch == "【":
                temp.append(str1[idx + 1])
        temp = set(temp)
        new_list = [i for i in temp]
        item["more"] = new_list
        final.append(item)
    json.dump(final, f2, ensure_ascii=False, indent=1)
    # print(final)
    f1.close()
    f2.close()


deal_dict("word.json", "dict.json")
