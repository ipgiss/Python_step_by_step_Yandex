while True:
    try:
        numb1 = int(input('Введите первое число: '))
        numb2 = int(input('Введите второе число: '))
    except ValueError:
        print('Введите только число!! Попробуйте еще раз.')
        continue  # вот это важно, а то цикл не закончится ))

    result = numb1 * numb2
    print(f'Результат = {result}')
    break
