import time


def alarm_timer(sec):
    elapsed = 0
    
    # print(CLEAR)
    while elapsed < sec:
        time.sleep(1)
        elapsed += 1
        
        total_sec_left = sec - elapsed
        hours_left = total_sec_left // 3600
        min_left = total_sec_left % 3600 // 60
        sec_left = total_sec_left % 60
        
        time_str = f"{hours_left:02d}:{min_left:02d}:{sec_left:02d}"
        
        print(f"\rAlarm will sound in {time_str}", end="", flush=True)