from jiwer import wer

def compute_wer(refs, preds):
    return wer(refs, preds)