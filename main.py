from FactorySimilarity import SimilarityFactory, SIMILARITY
import dnaToGraph as dna

print("==========================================")

similartyNB = SimilarityFactory.create_pizza(SIMILARITY.NbSimilarity, dna.H, dna.C)
print("NB benzerlik oranı", similartyNB.getSimilarity())

print("==========================================")

similartyCos = SimilarityFactory.create_pizza(SIMILARITY.Cosinus, dna.H, dna.C)
print("Cos benzerlik oranı", similartyCos.getSimilarity())

