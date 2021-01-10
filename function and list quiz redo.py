def main():
    teacher_name = get_valid_name("Please enter your name: ")
    greeting = message(teacher_name)
    print (greeting)
    
    class_size = get_valid_number("Please Enter your class size: ")
    
    i = 0
    student_names = []
    student_marks = []
    while i < class_size:
        name = get_valid_name("Please enter student name: ")
        student_names.append(name)

        mark = get_valid_number(f"What is {name}'s mark? ")
        student_marks.append(mark)
        
        i += 1

    display_report(student_names, student_marks)

    failing = count_failing(student_marks)
    print(f"There are {failing} students that are failing.")


def get_valid_name(prompt):
    while True:
        try:
            name = input(prompt)
            if name.isnumeric():
                raise TypeError
            if len(name) < 2 or len(name) > 15:
                raise ValueError
            break
        except (TypeError, ValueError):
            print("Invalid")
    return name

def get_valid_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number < 1:
                raise IndexError
            break
        except (ValueError, IndexError):
            print("Invalid")
    return number

def message(name):
    return f"Hello, {name}. Welcome to the Markbook."

def display_report(student_names, student_marks):
    i = 0
    while i < len(student_names):
        print(student_names[i], student_marks[i])
        i += 1

def count_failing(marks):
    count = 0
    for m in marks:
        if m < 50:
            count += 1
    return count


if __name__ == "__main__":
    main()
