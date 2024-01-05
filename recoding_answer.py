import os
import pyaudio
import wave

def recoding_answer():
    duration = 5
    sample_rate = 44100
    channels = 1
    format = pyaudio.paInt16

    # 상대 경로로 변경된 디렉토리
    directory_path = 'answer'

    # 현재 작업 디렉토리를 얻음
    current_directory = os.getcwd()

    file_name = 'answer.wav'
    file_path = os.path.join(current_directory, directory_path, file_name)

    # PyAudio 객체 생성
    p = pyaudio.PyAudio()

    # 녹음 설정
    stream = p.open(format=format,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=1024)

    print("Recording...")

    frames = []

    # 녹음 진행
    for i in range(0, int(sample_rate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    print("Recording finished.")

    # 스트림과 PyAudio 객체 닫기
    stream.stop_stream()
    stream.close()
    p.terminate()

    # 기존 파일이 있으면 덮어쓰기
    if os.path.exists(file_path):
        print("Overwriting existing file.")
    
    # WAV 파일로 저장
    wf = wave.open(file_path, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(pyaudio.PyAudio().get_sample_size(format))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    return file_path


#record_audio()

