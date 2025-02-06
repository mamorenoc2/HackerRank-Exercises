'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example
s = '12:01:00PM'

Return '12:01:00'.

s = '12:01:00AM'

Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in 12 hour format
Returns

string: the time in 24 hour format

Sample Input

07:05:45PM
Sample Output

19:05:45
'''

def time_conversion(time):
    period = time[-2:]
    time = time[:-2]
    hh,mm,ss = time.split(':')
    if period == 'PM':
        if hh != '12':
            hh = str(int(hh) + 12)
    else:
        if hh == '12':
            hh = '00'
    militar_time = f"{hh}:{mm}:{ss}"
    return militar_time
        

time = '07:05:45PM'
print(time_conversion(time))