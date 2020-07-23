#! python3

import time, pyperclip, pandas

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.'
      'Press Ctrl-c to quit.')


input()
print('Started')
start_time = time.time()
last_time = start_time
lap_num = 1
total_lap = []

# Start tracking the lap time
try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)

        lap = 'lap # {} {} {}'.format((str(lap_num) + ':').ljust(3),
                                       str(total_time).rjust(5),
                                       str(lap_time).rjust(6))

        print(lap, end='')

        lap_num += 1
        last_time = time.time() # Reset the last lap time
        # pyperclip.copy(lap)     # Copy lastest lap to clipboard
        total_lap.append(lap)



except KeyboardInterrupt:
    print('\nDone.')
    # Useing pandas to copy all data to clipboard
    pandas.DataFrame(total_lap).to_clipboard(excel=True, header=False, index=False)