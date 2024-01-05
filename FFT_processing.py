import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def fft(file_path):
    # 변환할 시간대 설정
    start_time=0
    end_time=None
    
    # 오디오 파일 경로
    audio_file= file_path
    
    # 오디오 파일 읽기
    sample_rate, data = wavfile.read(audio_file)
    
    # 선택한 시간 범위에 해당하는 데이터 추출
    start_index = int(start_time * sample_rate)
    end_index = None if end_time is None else int(end_time * sample_rate)
    audio_data = data[start_index:end_index]

    # FFT 계산
    fft_result = np.fft.fft(audio_data)
    fft_freq = np.fft.fftfreq(len(fft_result), 1/sample_rate)

    # FFT 결과를 시각화
    plt.figure(figsize=(10, 6))
    plt.plot(fft_freq, np.abs(fft_result))
    plt.title('FFT of Audio Signal')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()
    
    return fft_result

#plot_fft()