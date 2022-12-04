from datetime import datetime
from operator import itemgetter

def can_schedule_all(unloading_times):
    """
    :param unloading_times: (list) The list of datetimes
    :returns: (bool) Returns True if the datetimes don't overlap else returns False
    """
    unloading_times_ = sorted(unloading_times, key=itemgetter("start", "end"))
    
    overlap = 0
    result = None
    for i in range(len(unloading_times_) - 1):
        startA = unloading_times_[i]['start']
        endA = unloading_times_[i]['end']
        
        startB = unloading_times_[i+1]['start']
        endB = unloading_times_[i+1]['end']
        
        if (startA <= endB) and (startB >= endA):
            pass
        else:
            overlap += 1
    
    if overlap == 0:
        result = True
    else:
        result = False
    return result

if __name__ == "__main__":
    unloading_times = [
      {"start": datetime(2020, 5, 3, 19, 0), "end": datetime(2020, 5, 3, 20, 30)},
      {"start": datetime(2020, 5, 3, 22, 10), "end": datetime(2020, 5, 3, 22, 30)},
      {"start": datetime(2020, 5, 3, 20, 30), "end": datetime(2020, 5, 3, 22, 0)}
    ]
    
    print(can_schedule_all(unloading_times))