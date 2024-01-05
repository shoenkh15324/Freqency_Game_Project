import os
import random
import pygame

def play_question():
    pygame.init()
    
    # 문제가 저장된 디렉토리의 상대 경로
    directory_path = 'question' 

    # 현재 작업 디렉토리를 얻음
    current_directory = os.getcwd()

    # 디렉토리 내의 모든 파일 목록을 얻음
    all_files = os.listdir(os.path.join(current_directory, directory_path))
    
    # 음원 파일 목록을 추출 (확장자가 .mp3, .wav 등)
    music_files = [file for file in all_files if file.endswith(('.mp3', '.wav'))]
    
    if not music_files:
        return None  # 음원 파일이 없을 경우 None 반환
    
    # 랜덤으로 음원 파일 선택
    selected_music = random.choice(music_files)
    
    # 선택된 음원 파일의 전체 경로 생성
    music_path = os.path.join(current_directory, directory_path, selected_music)
    
    # Pygame을 사용하여 음원 재생
    print("Playing...")
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play()
    
    # 재생이 끝날 때까지 대기 (이 부분을 제거하면 프로그램이 바로 종료됩니다)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.quit()
    
    return music_path

# play_random_music()


##play_random_music()
