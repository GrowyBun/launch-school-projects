from lesson_2.calculator_messages import messages_dict

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

def calculator():
    while True:
        prompt(messages_dict['number1'])
        number1 = input()

        while invalid_number(number1):
            prompt(messages_dict['invalid_numb'])
            number1 = input()

        prompt(messages_dict['number2'])
        number2 = input()

        while invalid_number(number2):
            prompt(messages_dict['invalid_numb'])
            number2 = input()

        prompt(messages_dict['operation'])
        operation = input()

        while operation not in ["1", "2", "3", "4"]:
            prompt(messages_dict['chose'])
            operation = input()

        match operation:
            case "1":
                output = int(number1) + int(number2)
            case "2":
                output = int(number1) - int(number2)
            case "3":
                output = int(number1) * int(number2)
            case "4":
                output = int(number1) / int(number2)

        prompt(f"The result is {output}")

        prompt(messages_dict['new_calc'])
        rerun = input()
        if rerun and rerun[0].lower() != 'y':
            break

prompt('Welcome to Calculator!')

calculator()