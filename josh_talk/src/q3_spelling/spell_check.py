from indicnlp.normalize.indic_normalize import IndicNormalizerFactory

factory = IndicNormalizerFactory()
normalizer = factory.get_normalizer("hi")

def check_word(word):
    norm = normalizer.normalize(word)

    if word == norm:
        return "correct", "high"
    else:
        return "incorrect", "medium"