import play_question
import recoding_answer
import FFT_processing
import comparing_processing

file_path = play_question.play_question() #랜덤한 문제 출력
recorded_path = recoding_answer.recoding_answer() #정답 녹음
question_spectrum = FFT_processing.fft(file_path) #문제 fft처리
answer_spectrum = FFT_processing.fft(recorded_path) #정답 fft처리
similarity = comparing_processing.compare_spectrum(question_spectrum, answer_spectrum) #유사도 비교

# 유사도에 따른 정답 처리
if similarity >= 0.7:
     print("correct! ( similarity = ",similarity,")")
else:
     print("wrong! ( similarity = ",similarity,")")
     
print("test")

     