# Generation ID: Hutch_1764575368031_ee3rw5ocg (前半)

def myai(board, color):
    size = len(board)

    # 評価表の定義
    if size == 6:
        score_board = [
            [100, -10, 5, 5, -10, 100],
            [-10, -30, 3, 3, -30, -10],
            [5, 3, 0, 0, 3, 5],
            [5, 3, 0, 0, 3, 5],
            [-10, -30, 3, 3, -30, -10],
            [100, -10, 20, 20, -10, 100]
        ]
    else:  # size == 8
        score_board = [
            [100, -10, 5, 5, 5, 5, -10, 100],
            [-10, -30, 3, 3, 3, 3, -30, -10],
            [5, 3, 0, 0, 0, 0, 3, 5],
            [5, 3, 0, 0, 0, 0, 3, 5],
            [5, 3, 0, 0, 0, 0, 3, 5],
            [5, 3, 0, 0, 0, 0, 3, 5],
            [-10, -30, 3, 3, 3, 3, -30, -10],
            [100, -10, 5, 5, 5, 5, -10, 100]
        ]

    opponent = 3 - color
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def get_flips(board, row, col, color):
        if board[row][col] != 0:
            return 0

        total_flips = 0
        for dr, dc in directions:
            flips = 0
            r, c = row + dr, col + dc
            while 0 <= r < size and 0 <= c < size and board[r][c] == opponent:
                flips += 1
                r += dr
                c += dc

            if 0 <= r < size and 0 <= c < size and board[r][c] == color and flips > 0:
                total_flips += flips

        return total_flips

    def apply_move(board, row, col, color):
        new_board = [row[:] for row in board]
        new_board[row][col] = color

        for dr, dc in directions:
            flips = []
            r, c = row + dr, col + dc
            while 0 <= r < size and 0 <= c < size and new_board[r][c] == opponent:
                flips.append((r, c))
                r += dr
                c += dc

            if 0 <= r < size and 0 <= c < size and new_board[r][c] == color and flips:
                for fr, fc in flips:
                    new_board[fr][fc] = color

        return new_board

    best_move = None
    best_score = -float('inf')

    for row in range(size):
        for col in range(size):
            if board[row][col] == 0 and get_flips(board, row, col, color) > 0:
                future_board = apply_move(board, row, col, color)
                current_score = score_board[row][col]

                for next_row in range(size):
                    for next_col in range(size):
                        if future_board[next_row][next_col] == 0 and get_flips(future_board, next_row, next_col, opponent) > 0:
                            future_board2 = apply_move(future_board, next_row, next_col, opponent)
                            current_score -= score_board[next_row][next_col]

                if current_score > best_score:
                    best_score = current_score
                    best_move = (col, row)

    return best_move

# Generation ID: Hutch_1764575368031_ee3rw5ocg (後半)
