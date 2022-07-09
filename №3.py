def appearance(intervals):
    tutor_on_lesson = []
    for i in range(0, len(intervals['tutor']), 2):
        if intervals['lesson'][0] < intervals['tutor'][i] < intervals['lesson'][1] and\
                intervals['lesson'][0] < intervals['tutor'][i + 1] < intervals['lesson'][1]:
            tutor_on_lesson.append(intervals['tutor'][i])
            tutor_on_lesson.append(intervals['tutor'][i + 1])
        # компенсация отсутствия правой границы
        elif intervals['lesson'][0] < intervals['tutor'][i] < intervals['lesson'][1]:
            tutor_on_lesson.append(intervals['tutor'][i])
            tutor_on_lesson.append(intervals['lesson'][1])
        # компенсация отсутствия левой границы
        elif intervals['lesson'][0] < intervals['tutor'][i + 1] < intervals['lesson'][1]:
            tutor_on_lesson.append(intervals['tutor'][i + 1])
            tutor_on_lesson.append(intervals['lesson'][0])
    tutor_on_lesson.sort()
    pupil_on_tutor = []
    if len(intervals['tutor']) < len(intervals['pupil']):  # опорником должен быть тот у кого меньше промежутков
        for j in range(0, len(tutor_on_lesson), 2):
            for i in range(0, len(intervals['pupil']), 2):
                if tutor_on_lesson[j] < intervals['pupil'][i] < tutor_on_lesson[j + 1] and\
                        tutor_on_lesson[j] < intervals['pupil'][i + 1] < tutor_on_lesson[j + 1]:
                    pupil_on_tutor.append(intervals['pupil'][i])
                    pupil_on_tutor.append(intervals['pupil'][i + 1])
                elif tutor_on_lesson[j] < intervals['pupil'][i] < tutor_on_lesson[j + 1]:
                    pupil_on_tutor.append(intervals['pupil'][i])
                    pupil_on_tutor.append(tutor_on_lesson[j + 1])
                elif tutor_on_lesson[j] < intervals['pupil'][i + 1] < tutor_on_lesson[j + 1]:
                    pupil_on_tutor.append(intervals['pupil'][i + 1])
                    pupil_on_tutor.append(tutor_on_lesson[j])
    else:
        for j in range(0, len(intervals['pupil']), 2):
            for i in range(0, len(tutor_on_lesson), 2):
                if intervals['pupil'][j] < tutor_on_lesson[i] < intervals['pupil'][j + 1] and\
                        intervals['pupil'][j] < tutor_on_lesson[i + 1] < intervals['pupil'][j + 1]:
                    pupil_on_tutor.append(tutor_on_lesson[i])
                    pupil_on_tutor.append(tutor_on_lesson[i + 1])
                elif intervals['pupil'][j] < tutor_on_lesson[i] < intervals['pupil'][j + 1]:
                    pupil_on_tutor.append(tutor_on_lesson[i])
                    pupil_on_tutor.append(intervals['pupil'][j + 1])
                elif intervals['pupil'][j] < tutor_on_lesson[i + 1] < intervals['pupil'][j + 1]:
                    pupil_on_tutor.append(tutor_on_lesson[i + 1])
                    pupil_on_tutor.append(intervals['pupil'][j])
    pupil_on_tutor.sort()
    summa = 0
    for i in range(0, len(pupil_on_tutor), 2):
        summa += (abs(pupil_on_tutor[i] - pupil_on_tutor[i + 1]))

    return summa


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    # {'data': {'lesson': [1594702800, 1594706400],
    #           'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
    #                     1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
    #                     1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
    #                     1594706524, 1594706524, 1594706579, 1594706641],
    #           'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    #  'answer': 3577
    #  },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
