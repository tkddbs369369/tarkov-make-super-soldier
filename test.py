import serial
import time

# 아두이노와 시리얼 통신 설정
arduino = serial.Serial('COM5', 9600, timeout=1)  # COM 포트는 환경에 따라 다를 수 있습니다.
time.sleep(2)  # 아두이노 연결 대기

def move_mouse(x, y):
    command = f"{x},{y}\n"
    arduino.write(command.encode())
    time.sleep(0.1)  # 명령 처리 대기

# 예제 사용
move_mouse(10, 0)  # x 좌표로 1만큼 이동


# 연결 종료
arduino.close()