''' Given a hashmap associating each courseId key with a list of courseIds values, which represents that the prerequisites of courseId are courseIds. Return a sorted ordering of courses such that we can finish all courses.
Return null if there is no such ordering.
For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300']. '''

def sort_course_id(course_id):
    # create list of tuples from dictionary
    courses = [(k, len(v)) for k, v in course_id.items()]

    # sort by second item in tuple
    courses.sort(key=lambda x: x[1])

    # extract course ids
    sorted_courses = [course[0] for course in courses]

    return sorted_courses


course_id = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}

result = sort_course_id(course_id)
print(result)

