tic_tac_toe = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x_positions = []
o_positions = []
winning_positions = [[1, 2, 3],
[1, 3, 2],
[2, 1, 3],
[2, 3, 1],
[3, 1, 2],
[3, 2, 1],
[4, 5, 6],
[4, 6, 5],
[5, 4, 6],
[5, 6, 4],
[6, 4, 5],
[6, 5, 4],
[7, 8, 9],
[7, 9, 8],
[8, 7, 9],
[8, 9, 7],
[9, 7, 8],
[9, 8, 7],
[1, 4, 7],
[1, 7, 4],
[4, 1, 7],
[4, 7, 1],
[7, 1, 4],
[7, 4, 1],
[2, 5, 8],
[2, 8, 5],
[5, 2, 8],
[5, 8, 2],
[8, 2, 5],
[8, 5, 2],
[3, 6, 9],
[3, 9, 6],
[6, 3, 9],
[6, 9, 3],
[9, 3, 6],
[9, 6, 3],
[3, 5, 7],
[3, 7, 5],
[5, 3, 7],
[5, 7, 3],
[7, 3, 5],
[7, 5, 3],

]
for m in range(9):
    if m % 2 == 0:
        answer = int(input('enter Xs position: '))
        if answer <= 3:
            x_positions.append(tic_tac_toe[0][answer - 1])
            tic_tac_toe[0][answer - 1] = 'X'

        elif answer > 3:
            answer = answer - 3
            x_positions.append(tic_tac_toe[1][answer - 1])
            tic_tac_toe[1][answer - 1] = 'x'
        else:
            answer -= 6
            x_positions.append(tic_tac_toe[1][answer - 1])
            tic_tac_toe[1][answer - 1] = 'O'

        for _ in winning_positions:
            if _ in x_positions:
                print('X Won')
                break
    else:
        answer = int(input('enter Os position: '))
        if answer <= 3:
            o_positions.append(tic_tac_toe[0][answer - 1])
            tic_tac_toe[0][answer - 1] = 'O'

        elif answer > 3:
            answer -= 3
            o_positions.append(tic_tac_toe[1][answer - 1])
            tic_tac_toe[1][answer - 1] = 'O'
        else:
            answer -= 6
            o_positions.append(tic_tac_toe[2][answer - 1])
            tic_tac_toe[2][answer - 1] = 'O'
        for n in winning_positions:
            if n in o_positions:
                print('O Won')
                break

    for i in tic_tac_toe:
        print("--------")
        print(i)
