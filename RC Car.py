import RPi.GPIO as GPIO
import time

# GPIO pin numbers
motor1_in1 = 17
motor1_in2 = 18
motor2_in1 = 22
motor2_in2 = 23

# Set GPIO mode and setup pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1_in1, GPIO.OUT)
GPIO.setup(motor1_in2, GPIO.OUT)
GPIO.setup(motor2_in1, GPIO.OUT)
GPIO.setup(motor2_in2, GPIO.OUT)

# Function to move the RC car forward
def move_forward():
    GPIO.output(motor1_in1, GPIO.HIGH)
    GPIO.output(motor1_in2, GPIO.LOW)
    GPIO.output(motor2_in1, GPIO.HIGH)
    GPIO.output(motor2_in2, GPIO.LOW)

# Function to move the RC car backward
def move_backward():
    GPIO.output(motor1_in1, GPIO.LOW)
    GPIO.output(motor1_in2, GPIO.HIGH)
    GPIO.output(motor2_in1, GPIO.LOW)
    GPIO.output(motor2_in2, GPIO.HIGH)

# Function to turn the RC car left
def turn_left():
    GPIO.output(motor1_in1, GPIO.LOW)
    GPIO.output(motor1_in2, GPIO.HIGH)
    GPIO.output(motor2_in1, GPIO.HIGH)
    GPIO.output(motor2_in2, GPIO.LOW)

# Function to turn the RC car right
def turn_right():
    GPIO.output(motor1_in1, GPIO.HIGH)
    GPIO.output(motor1_in2, GPIO.LOW)
    GPIO.output(motor2_in1, GPIO.LOW)
    GPIO.output(motor2_in2, GPIO.HIGH)

# Function to stop the RC car
def stop():
    GPIO.output(motor1_in1, GPIO.LOW)
    GPIO.output(motor1_in2, GPIO.LOW)
    GPIO.output(motor2_in1, GPIO.LOW)
    GPIO.output(motor2_in2, GPIO.LOW)

# Main loop to control the RC car
if __name__ == "__main__":
    try:
        while True:
            # Move forward for 1 second
            move_forward()
            time.sleep(1)

            # Move backward for 1 second
            move_backward()
            time.sleep(1)

            # Turn left for 1 second
            turn_left()
            time.sleep(1)

            # Turn right for 1 second
            turn_right()
            time.sleep(1)

            # Stop for 1 second
            stop()
            time.sleep(1)

    except KeyboardInterrupt:
        # Clean up GPIO on keyboard interrupt
        GPIO.cleanup()