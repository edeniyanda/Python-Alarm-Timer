import pygame
from func import alarm_timer


# Initialize the pygame library
pygame.init()

# Load the audio file
audio_file = pygame.mixer.Sound('Alarm-Fast-A1.mp3')


# Collect duration information
hours = int(input("Enter a number of hours: "))
minutes = int(input("Enter a number of minutes: "))
seconds = int(input("Enter a number of seconds: "))
total_num_sec = hours * 3600 + minutes * 60 + seconds

# Initialize the time
alarm_timer(total_num_sec)


# Play the audio file
audio_file.play()

# Wait for the audio to finish playing
pygame.time.wait(int(audio_file.get_length() * 1000))

# Clean up the pygame library
pygame.quit()
