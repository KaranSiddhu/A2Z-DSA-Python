marks = int(input('Enter your mark out of 100:'))

match marks:
    case 100:
        print('You did awesome!')

    case 70:
        print('You did amazing!')

    case 50:
        print('You did good!')

    case _:
        print('You can do better')
