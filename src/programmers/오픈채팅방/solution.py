def solution(record):
    answer = []
    id_nickname = {}

    for r in record:
        message = r.split(' ')
        if message[0] in ['Enter', 'Change']:
            id_nickname[message[1]] = message[2]

    for r in record:
        message = r.split(' ')
        if message[0] == 'Enter':
            answer.append(id_nickname[message[1]] + '님이 들어왔습니다.')
        elif message[0] == 'Leave':
            answer.append(id_nickname[message[1]] + '님이 나갔습니다.')

    return answer