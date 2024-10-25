from elasticsearch import Elasticsearch, helpers  
import datetime  
  
# 连接到 Elasticsearch 客户端  
es = Elasticsearch(["http://localhost:9200"])  
  
# 定义索引名称  
index_name = "your_index_name"  
  
# 定义查询函数  
def multi_condition_query(time=None, name=None, gender=None):  
    query = {  
        "query": {  
            "bool": {  
                "must": [],  
                "should": []  
            }  
        }  
    }  
      
    # 添加时间条件（假设时间字段为 'timestamp' 且格式为 ISO 8601）  
    if time:  
        time_range_query = {  
            "range": {  
                "timestamp": {  
                    "gte": time.strftime('%Y-%m-%dT%H:%M:%S'),  # 开始时间  
                    "lte": (time + datetime.timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S')  # 结束时间（到下一天的同一时间）  
                }  
            }  
        }  
        query["query"]["bool"]["must"].append(time_range_query)  
      
    # 添加姓名条件  
    if name:  
        name_query = {  
            "match": {  
                "name": name  
            }  
        }  
        query["query"]["bool"]["must"].append(name_query)  
      
    # 添加性别条件  
    if gender:  
        gender_query = {  
            "match": {  
                "gender": gender  
            }  
        }  
        query["query"]["bool"]["must"].append(gender_query)  
      
    # 如果没有 must 条件，则查询所有（可选）  
    if not query["query"]["bool"]["must"]:  
        query["query"]["match_all"] = {}  
        del query["query"]["bool"]  
      
    return query  
  
# 示例查询  
time_condition = datetime.datetime(2023, 10, 1)  # 可选，设置时间条件  
name_condition = "John Doe"  # 可选，设置姓名条件  
gender_condition = "male"  # 可选，设置性别条件  
  
query = multi_condition_query(time_condition, name_condition, gender_condition)  
  
# 打印查询语句  
print(query)  
  
# 执行查询  
response = es.search(index=index_name, body=query)  
  
# 打印查询结果  
print(response)