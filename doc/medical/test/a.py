import json   
def generate_tree(source, parent):
     tree = []     
     for item in source:
         if item["parent"] == parent:
             item["child"] = generate_tree(source, item["id"])
             tree.append(item)
     return tree 
 
 
def gettree(data,pid):
    tree =[]
    for item in data:
        if item['parent'] == pid:
           item['child'] = gettree(data,item['id'])
           tree.append(item)
    return tree

if __name__ == '__main__':
    permission_source = [{"id": 1, "name": '电器', "parent": 0},
         {"id": 2, "name": '水果', "parent": 0},
         {"id": 3, "name": '家用电器', "parent": 1},
         {"id": 13, "name": '1111家用电器', "parent": 3},
         {"id": 4, "name": '电吹风', "parent": 2},
         {"id": 5, "name": '电风扇', "parent": 3},
         {"id": 6, "name": '台灯', "parent": 3},
         {"id": 7, "name": '商用电器', "parent": 1},
         {"id": 8, "name": '大型电热锅', "parent": 7}]
    permission_tree = gettree(permission_source, 0)
    print(json.dumps(permission_tree, ensure_ascii=False)) 