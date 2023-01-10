def main():
    number_of_classes = input('How many classes are you taking this semester? ')
    class_list  = [] # creates an empty list
    for number in range(int(number_of_classes)):
        class_name = input('Enter the name of the class number ' + str(number+1) + ': ')
        class_list.append(class_name)
    
    for index,name in enumerate(class_list):
        print(f'Class {index + 1}: {name}')
    
main()