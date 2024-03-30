from transformers import AutoFeatureExtractor, VanForImageClassification


feature_extractor = AutoFeatureExtractor.from_pretrained("as-cle-bert/CARPE-VAN")
model = VanForImageClassification.from_pretrained("as-cle-bert/CARPE-VAN")
