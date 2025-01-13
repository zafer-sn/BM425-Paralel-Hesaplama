import time

def x(id, reserve_start, reserve_end, crossings):
    intersections_to_lock = []
    for crossing in crossings:
        if reserve_end >= crossing.position >= reserve_start and crossing.intersection.locked_by != id:
            intersections_to_lock.append(crossing.intersection)
    intersections_to_lock = sorted(intersections_to_lock, key = lambda it : it.uid)
    for lock in intersections_to_lock:
        lock.mutex.acquire()
        lock.locked_by = id
        time.sleep(0.02)

def move_train(train, distance, crossings):
    while train.front < distance:
        train.front += 1
        for crossing in crossings:
            if train.front == crossing.position:
                x(train.uid, crossing.position, crossing.position + train.train_length, crossings)
                """crossing.intersection.mutex.acquire()
                crossing.intersection.locked_by = train.uid"""
            back = train.front - train.train_length
            if back == crossing.position:
                crossing.intersection.mutex.release()
                crossing.intersection.locked_by = -1
        time.sleep(0.01)
