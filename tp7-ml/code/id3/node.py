class Node():
    def __init__(self,feature_index = None,threshold = None,
                 left = None,right = None,info_gain = None,value = None):
        
        # Para los nodos de decisión
        self.feature_index = feature_index
        self.threshold = threshold
        self.left = left
        self.right = right
        self.info_gain = info_gain

        # Para los nodos hoja
        self.value = value