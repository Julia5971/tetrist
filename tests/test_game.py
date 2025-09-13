import pytest
from game.block import Block, BlockType
from game.board import Board
from game.game import Game

class TestGame:
    """게임 조작 시스템 테스트"""
    
    def test_game_creation(self):
        """게임이 올바르게 생성되는지 테스트"""
        # Given & When
        game = Game()
        
        # Then
        assert isinstance(game.board, Board)
        assert game.current_block is None
        assert game.score == 0
        assert game.level == 1
        assert game.lines_cleared == 0
        assert game.game_over == False
    
    def test_spawn_new_block(self):
        """새 블록이 생성되는지 테스트"""
        # Given
        game = Game()
        
        # When
        game.spawn_new_block()
        
        # Then
        assert game.current_block is not None
        assert isinstance(game.current_block, Block)
        assert game.current_block.x == 4  # 중앙에서 시작
        assert game.current_block.y == 0  # 맨 위에서 시작
    
    def test_move_block_left(self):
        """블록이 왼쪽으로 이동하는지 테스트"""
        # Given
        game = Game()
        game.spawn_new_block()
        initial_x = game.current_block.x
        
        # When
        game.move_block_left()
        
        # Then
        assert game.current_block.x == initial_x - 1
        assert game.current_block.y == 0
    
    def test_move_block_right(self):
        """블록이 오른쪽으로 이동하는지 테스트"""
        # Given
        game = Game()
        game.spawn_new_block()
        initial_x = game.current_block.x
        
        # When
        game.move_block_right()
        
        # Then
        assert game.current_block.x == initial_x + 1
        assert game.current_block.y == 0
    
    def test_move_block_down(self):
        """블록이 아래로 이동하는지 테스트"""
        # Given
        game = Game()
        game.spawn_new_block()
        initial_y = game.current_block.y
        
        # When
        game.move_block_down()
        
        # Then
        assert game.current_block.y == initial_y + 1
        assert game.current_block.x == 4
    
    def test_rotate_block(self):
        """블록이 회전하는지 테스트"""
        # Given
        game = Game()
        game.spawn_new_block()
        initial_rotation = game.current_block.rotation
        
        # When
        game.rotate_block()
        
        # Then
        assert game.current_block.rotation == (initial_rotation + 1) % 4
    
    def test_collision_detection_movement(self):
        """이동 시 충돌 감지 테스트"""
        # Given
        game = Game()
        game.spawn_new_block()
        
        # 블록을 맨 아래로 이동
        for _ in range(19):
            game.move_block_down()
        
        # When - 더 이상 아래로 이동할 수 없음
        can_move = game.can_move_block(0, 1)
        
        # Then
        assert can_move == False
    
    def test_place_block_on_board(self):
        """블록이 보드에 배치되는지 테스트"""
        # Given
        game = Game()
        game.spawn_new_block()
        
        # 블록을 맨 아래로 이동
        for _ in range(19):
            game.move_block_down()
        
        # When
        game.place_current_block()
        
        # Then
        assert game.current_block is None
        # 보드에 블록이 배치되었는지 확인
        assert any(any(cell is not None for cell in row) for row in game.board.grid)
    
    def test_line_clearing(self):
        """줄 삭제 기능 테스트"""
        # Given
        game = Game()
        
        # 19번째 줄을 가득 채움
        for x in range(10):
            game.board.grid[19][x] = "filled"
        
        initial_score = game.score
        
        # When
        game.clear_full_lines()
        
        # Then
        assert game.lines_cleared > 0
        assert game.score > initial_score
        assert all(cell is None for cell in game.board.grid[19])
    
    def test_level_progression(self):
        """레벨 진행 테스트"""
        # Given
        game = Game()
        initial_level = game.level
        
        # 10줄을 삭제 (레벨업 조건)
        game.lines_cleared = 10
        
        # When
        game.update_level()
        
        # Then
        assert game.level == initial_level + 1
    
    def test_game_over_condition(self):
        """게임 오버 조건 테스트"""
        # Given
        game = Game()
        game.spawn_new_block()
        
        # 블록을 맨 위에서 시작하도록 설정
        game.current_block.y = 0
        
        # 맨 위 줄을 가득 채움
        for x in range(10):
            game.board.grid[0][x] = "filled"
        
        # When
        game.check_game_over()
        
        # Then
        assert game.game_over == True
    
    def test_drop_block_to_bottom(self):
        """블록을 바닥까지 떨어뜨리는 테스트"""
        # Given
        game = Game()
        game.spawn_new_block()
        initial_y = game.current_block.y
        
        # When
        game.drop_block_to_bottom()
        
        # Then
        # 블록이 바닥에 닿아서 보드에 배치되었는지 확인
        assert game.current_block is None  # 블록이 배치되어 None이 됨
        # 보드에 블록이 배치되었는지 확인
        assert any(any(cell is not None for cell in row) for row in game.board.grid)
    
    def test_can_move_block_boundary(self):
        """경계에서 이동 가능 여부 테스트"""
        # Given
        game = Game()
        game.spawn_new_block()
        
        # 블록을 맨 왼쪽으로 이동
        for _ in range(5):
            game.move_block_left()
        
        # When & Then
        assert game.can_move_block(-1, 0) == False  # 왼쪽으로 더 이동 불가
        assert game.can_move_block(1, 0) == True    # 오른쪽으로 이동 가능
        
        # 블록을 맨 오른쪽으로 이동
        for _ in range(8):
            game.move_block_right()
        
        assert game.can_move_block(1, 0) == False   # 오른쪽으로 더 이동 불가
        assert game.can_move_block(-1, 0) == True   # 왼쪽으로 이동 가능
