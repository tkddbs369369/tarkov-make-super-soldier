import serial
import time

# 시리얼 포트 설정
arduino_port = "COM5"
baud_rate = 9600

# 시리얼 포트 열기
ser = serial.Serial(arduino_port, baud_rate)

# 아두이노로 신호 보내기
signal = "x1"  # x 좌표로 100만큼 이동
ser.write(signal.encode())

for i in range(5):
    signal = "x-125"  # y 좌표로 200만큼 이동
    ser.write(signal.encode())
    time.sleep(0.001)


# 시리얼 포트 닫기
ser.close()