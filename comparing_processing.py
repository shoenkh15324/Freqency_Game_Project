import numpy as np
from scipy.stats import pearsonr

def compare_spectrum(question, answer):
     # 피어슨 상관계수 계산
     correlation_coefficient, _ = pearsonr(np.abs(question), np.abs(answer))
     return correlation_coefficient
