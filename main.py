import sys
import re


DIRECTIONS = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)


def load_puzzle(path):
    with open(path, "r", encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file]

    dimension_line = lines[0].strip()
    rows, cols = map(int, re.split(r"[xX]", dimension_line, maxsplit=1))
    board = []
    for index in range(1, rows + 1):
        board.append([cell.upper() for cell in lines[index].split()])

    words = [line for line in lines[rows + 1 :] if line.strip()]
    return rows, cols, board, words


def find_word(board, rows, cols, word):
    normalized_word = word.replace(" ", "").upper()
    if not normalized_word:
        return None

    length = len(normalized_word)

    for row in range(rows):
        for col in range(cols):
            if board[row][col] != normalized_word[0]:
                continue
            for row_step, col_step in DIRECTIONS:
                end_row = row + (length - 1) * row_step
                end_col = col + (length - 1) * col_step
                if end_row < 0 or end_row >= rows or end_col < 0 or end_col >= cols:
                    continue

                matched = True
                for index in range(length):
                    next_row = row + index * row_step
                    next_col = col + index * col_step
                    if board[next_row][next_col] != normalized_word[index]:
                        matched = False
                        break
                if matched:
                    return row, col, end_row, end_col
    return None


def solve(path):
    rows, cols, board, words = load_puzzle(path)
    for word in words:
        found = find_word(board, rows, cols, word)
        if found is not None:
            start_row, start_col, end_row, end_col = found
            print(f"{word} {start_row}:{start_col} {end_row}:{end_col}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input-file>")
        sys.exit(1)
    solve(sys.argv[1])


if __name__ == "__main__":
    main()
