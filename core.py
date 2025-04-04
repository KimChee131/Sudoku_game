import random
import time

class Sudoku:
    def __init__(self, difficulty=0.5):
        """
        Khởi tạo trạng thái ban đầu cho game Sudoku
        """
        # Bảng gốc và bảng giải
        self.board = [[0] * 9 for _ in range(9)] # Bảng gốc (câu đố)
        self.solution = [[0] * 9 for _ in range(9)]  # Bảng giải (đáp án)
        
        # Trạng thái người chơi
        self.user_input = [[0] * 9 for _ in range(9)]  # Bảng nhập liệu của người chơi
        self.notes = [[[False] * 9 for _ in range(9)] for _ in range(9)] # Bảng ghi chú 
        self.incorrect_cells = set() # Tập hợp các ô nhập sai 
        self.selected = None # Ô đang được chọn
        
        # Thống kê game
        self.start_time = time.time() # Thời gian bắt đầu game
        self.elapsed_time = 0  # Thời gian đã chơi (tính bằng giây)
        self.mistakes = 0 # Số lần nhập sai
        self.game_over = False # Trạng thái game - True nếu đã hoàn thành puzzle
        
        # Cài đặt game
        self.difficulty = difficulty # Độ khó (0-1): 0.5 = 50% ô trống (dễ), 0.6 = 60% (trung bình), 0.7 = 70% (khó)
        self.history = []  # Lịch sử các nước đi

        # self.generate_board(difficulty)  # Sẽ được triển khai trong branch feature/diagonal-note
    def is_valid(self, board, row, col, num):
        # Check row
        if num in board[row]:
            return False
        
        # Check column
        for i in range(9):
            if board[i][col] == num:
                return False
        
        # Check 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        
        return True
    
    def solve_board(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in random.sample(range(1, 10), 9):  # Try numbers in random order
                        if self.is_valid(board, row, col, num):
                            board[row][col] = num
                            if self.solve_board(board):
                                return True
                            board[row][col] = 0
                    return False
        return True
    
    # def generate_board():
    # def fill_diagonal():
    # def place_number(): 
    # def toggle_note():      
    # def clear_notes():
    # def save_state():   
    # def undo():          
    # def is_complete():          
    # def save_score():       
    # def load_scores():
    
    def update_time(self):
        if not self.game_over:
            self.elapsed_time = time.time() - self.start_time


