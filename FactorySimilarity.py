from NBsimilarity import NbSimilarity
from enum import Enum
from CosSimilarity import CosSim


class SIMILARITY(Enum):
    NbSimilarity = 0
    Cosinus = 1


class SimilarityFactory():
    @staticmethod
    def create_pizza(similarity_type ,Garph1 ,Graph2):
        if similarity_type == SIMILARITY.NbSimilarity:
            return NbSimilarity(Garph1, Graph2, 0.0001)
        elif similarity_type == SIMILARITY.Cosinus:
            return CosSim(Garph1, Graph2)
