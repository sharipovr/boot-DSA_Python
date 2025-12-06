from queue import Queue


def matchmake(queue, user):
    if user[1] == 'leave':
        queue.search_and_remove(user[0])
    if user[1] == 'join':
        queue.push(user[0]) 
    if queue.size() >= 4:
        user1 = queue.pop()
        user2 = queue.pop()
        return f"{user1} matched {user2}!"   
    return "No match found"
