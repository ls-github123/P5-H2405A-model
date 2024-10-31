# faiss_service.py  
  
import faiss  
import numpy as np  
  
class FaissService:  
    def __init__(self, dimension):  
        self.dimension = dimension  
        self.index = self.create_index()  
  
    def create_index(self):  
        quantizer = faiss.IndexFlatL2(self.dimension)  
        index = faiss.IndexIVFFlat(quantizer, self.dimension, 100)  # 假设使用100个聚类  
        return index  
  
    def add_vectors_from_file(self, file_path):  
        with open(file_path, 'r') as file:  
            for line in file:  
                vector_str = line.strip().split()  
                if len(vector_str) == self.dimension:  
                    vector = np.array(vector_str, dtype='float32')  
                    self.index.add(vector.reshape(1, -1))  
  
    def search_vectors(self, query_vectors, k=5):  
        distances, labels = self.index.search(query_vectors, k)  
        return distances, labels  
  
# 假设在项目启动时加载向量（这里只是示例，实际项目中可能需要更复杂的逻辑）  
faiss_service = FaissService(dimension=64)  
# faiss_service.add_vectors_from_file('doc/1.txt')