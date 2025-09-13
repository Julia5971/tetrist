import pytest
from game.block import Block, BlockType
from game.board import Board
from game.game import Game

class TestGameLogic:
    """게임 로직 테스트"""
    
    def test_scoring_system(self):
        """점수 계산 시스템 테스트"""
        # Given
        game = Game()
        
        # When - 1줄 삭제
        for x in range(10):
            game.board.grid[19][x] = "filled"
        game.clear_full_lines()
        
        # Then
        assert game.score == 100 * game.level  # 1줄 = 100 * 레벨
        assert game.lines_cleared == 1
    
    def test_scoring_system_multiple_lines(self):
        """여러 줄 삭제 시 점수 계산 테스트"""
        # Given
        game = Game()
        
        # When - 2줄 삭제
        for line in [18, 19]:
            for x in range(10):
                game.board.grid[line][x] = "filled"
        game.clear_full_lines()
        
        # Then
        assert game.score == 300 * game.level  # 2줄 = 300 * 레벨
        assert game.lines_cleared == 2
    
    def test_tetris_scoring(self):
        """테트리스(4줄 동시 삭제) 점수 계산 테스트"""
        # Given
        game = Game()
        
        # When - 4줄 동시 삭제
        for line in [16, 17, 18, 19]:
            for x in range(10):
                game.board.grid[line][x] = "filled"
        game.clear_full_lines()
        
        # Then
        assert game.score == 800 * game.level  # 4줄 = 800 * 레벨
        assert game.lines_cleared == 4
    
    def test_level_progression_system(self):
        """레벨 진행 시스템 테스트"""
        # Given
        game = Game()
        initial_level = game.level
        
        # When - 10줄 삭제
        game.lines_cleared = 10
        game.update_level()
        
        # Then
        assert game.level == initial_level + 1
        
        # When - 20줄 삭제
        game.lines_cleared = 20
        game.update_level()
        
        # Then
        assert game.level == initial_level + 2
    
    def test_drop_speed_by_level(self):
        """레벨에 따른 낙하 속도 테스트"""
        # Given
        game = Game()
        
        # When & Then
        game.level = 1
        assert game.get_drop_speed() == 1.0
        
        game.level = 2
        assert game.get_drop_speed() == 0.9
        
        game.level = 5
        assert game.get_drop_speed() == 0.6
        
        game.level = 10
        assert game.get_drop_speed() == 0.1  # 최소 속도
    
    def test_game_over_top_line(self):
        """맨 위 줄에 블록이 있으면 게임 오버 테스트"""
        # Given
        game = Game()
        
        # When - 맨 위 줄을 가득 채움
        for x in range(10):
            game.board.grid[0][x] = "filled"
        
        game.check_game_over()
        
        # Then
        assert game.game_over == True
    
    def test_game_over_block_spawn(self):
        """새 블록이 생성될 수 없으면 게임 오버 테스트"""
        # Given
        game = Game()
        
        # 맨 위 3줄을 가득 채움
        for y in range(3):
            for x in range(10):
                game.board.grid[y][x] = "filled"
        
        # When
        game.spawn_new_block()
        game.check_game_over()
        
        # Then
        assert game.game_over == True
    
    def test_line_clearing_with_blocks_above(self):
        """위에 블록이 있는 상태에서 줄 삭제 테스트"""
        # Given
        game = Game()
        
        # 19번째 줄을 가득 채움
        for x in range(10):
            game.board.grid[19][x] = "filled"
        
        # 18번째 줄에 블록 배치
        game.board.grid[18][5] = "X"
        
        # When
        game.clear_full_lines()
        
        # Then
        assert game.lines_cleared == 1
        assert game.board.grid[19][5] == "X"  # 블록이 아래로 떨어짐
        assert all(cell is None for cell in game.board.grid[18])  # 18번째 줄은 비어있음
    
    def test_multiple_line_clearing_order(self):
        """여러 줄이 삭제될 때 순서 테스트"""
        # Given
        game = Game()
        
        # 17, 18, 19번째 줄을 가득 채움
        for line in [17, 18, 19]:
            for x in range(10):
                game.board.grid[line][x] = "filled"
        
        # 16번째 줄에 블록 배치
        game.board.grid[16][5] = "X"
        
        # When
        game.clear_full_lines()
        
        # Then
        assert game.lines_cleared == 3
        assert game.score == 500 * game.level  # 3줄 = 500 * 레벨
        assert game.board.grid[18][5] == "X"  # 블록이 아래로 떨어짐
    
    def test_score_calculation_by_level(self):
        """레벨에 따른 점수 계산 테스트"""
        # Given
        game = Game()
        game.level = 3  # 레벨 3으로 설정
        
        # When - 1줄 삭제
        for x in range(10):
            game.board.grid[19][x] = "filled"
        game.clear_full_lines()
        
        # Then
        assert game.score == 100 * 3  # 100 * 레벨 3 = 300
    
    def test_game_reset(self):
        """게임 리셋 기능 테스트"""
        # Given
        game = Game()
        game.score = 1000
        game.level = 5
        game.lines_cleared = 50
        game.game_over = True
        
        # When
        game.reset_game()
        
        # Then
        assert game.score == 0
        assert game.level == 1
        assert game.lines_cleared == 0
        assert game.game_over == False
        assert game.current_block is None
        assert all(all(cell is None for cell in row) for row in game.board.grid)
    
    def test_game_state_tracking(self):
        """게임 상태 추적 테스트"""
        # Given
        game = Game()
        game.spawn_new_block()
        
        # When
        state = game.get_game_state()
        
        # Then
        assert state['score'] == 0
        assert state['level'] == 1
        assert state['lines_cleared'] == 0
        assert state['game_over'] == False
        assert state['current_block'] is not None
        assert len(state['board']) == 20  # 보드 높이
        assert len(state['board'][0]) == 10  # 보드 너비
