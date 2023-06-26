import datetime # datetime is library

# Get the current date and time
current_datetime = datetime.datetime.now()

# Format the current date and time as a string
current_datetime_str = current_datetime.strftime("%y-%m-%d %H:%M:%S")
#strftime method is used to format the current_datetime object as a string. The format string "%y-%m-%d %H:%M:%S" specifies the desired format for the date and time representation.

# Print the current date and time
print("Current date and time:", current_datetime_str)
