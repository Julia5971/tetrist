import pytest
from game.block import Block, BlockType
from game.board import Board


class TestBoard:
    """게임 보드 클래스 테스트"""
    
    def test_board_creation(self):
        """보드가 올바른 크기로 생성되는지 테스트"""
        # Given & When
        board = Board()
        
        # Then
        assert board.width == 10
        assert board.height == 20
        assert len(board.grid) == 20
        assert len(board.grid[0]) == 10
        assert all(all(cell is None for cell in row) for row in board.grid)
    
    def test_board_boundaries(self):
        """보드 경계값 테스트"""
        # Given
        board = Board()
        
        # When & Then
        assert board.is_valid_position(0, 0) == True
        assert board.is_valid_position(9, 19) == True
        assert board.is_valid_position(-1, 0) == False
        assert board.is_valid_position(10, 0) == False
        assert board.is_valid_position(0, -1) == False
        assert board.is_valid_position(0, 20) == False
    
    def test_place_block(self):
        """블록 배치 테스트"""
        # Given
        board = Board()
        block = Block(BlockType.O, 5, 5)
        
        # When
        board.place_block(block)
        
        # Then
        # O 블록은 2x2 정사각형이므로 (5,5), (6,5), (5,6), (6,6) 위치에 배치
        assert board.grid[5][5] is not None
        assert board.grid[5][6] is not None
        assert board.grid[6][5] is not None
        assert board.grid[6][6] is not None
    
    def test_collision_detection(self):
        """충돌 감지 테스트"""
        # Given
        board = Board()
        block1 = Block(BlockType.O, 5, 5)
        block2 = Block(BlockType.O, 6, 6)  # 겹치는 위치
        
        # When
        board.place_block(block1)
        
        # Then
        assert board.check_collision(block2) == True
    
    def test_no_collision(self):
        """충돌이 없는 경우 테스트"""
        # Given
        board = Board()
        block1 = Block(BlockType.O, 5, 5)
        block2 = Block(BlockType.O, 8, 8)  # 겹치지 않는 위치
        
        # When
        board.place_block(block1)
        
        # Then
        assert board.check_collision(block2) == False
    
    def test_remove_block(self):
        """블록 제거 테스트"""
        # Given
        board = Board()
        block = Block(BlockType.O, 5, 5)
        board.place_block(block)
        
        # When
        board.remove_block(block)
        
        # Then
        assert board.grid[5][5] is None
        assert board.grid[5][6] is None
        assert board.grid[6][5] is None
        assert board.grid[6][6] is None
    
    def test_block_out_of_bounds(self):
        """블록이 보드 밖으로 나가는 경우 테스트"""
        # Given
        board = Board()
        block = Block(BlockType.I, 8, 0)  # I 블록은 4칸이므로 x=8에서 시작하면 x=11까지 나감
        
        # When & Then
        assert board.check_collision(block) == True  # 경계를 벗어나므로 충돌
    
    def test_line_detection(self):
        """가득 찬 줄 감지 테스트"""
        # Given
        board = Board()
        
        # When - 19번째 줄을 가득 채움
        for x in range(10):
            board.grid[19][x] = "filled"
        
        # Then
        assert board.get_full_lines() == [19]
    
    def test_multiple_full_lines(self):
        """여러 줄이 가득 찬 경우 테스트"""
        # Given
        board = Board()
        
        # When - 18번째와 19번째 줄을 가득 채움
        for line in [18, 19]:
            for x in range(10):
                board.grid[line][x] = "filled"
        
        # Then
        full_lines = board.get_full_lines()
        assert len(full_lines) == 2
        assert 18 in full_lines
        assert 19 in full_lines
    
    def test_clear_lines(self):
        """줄 삭제 테스트"""
        # Given
        board = Board()
        
        # 19번째 줄을 가득 채우고 위에 블록 배치
        for x in range(10):
            board.grid[19][x] = "filled"
        board.grid[18][5] = "block"
        
        # When
        board.clear_full_lines()
        
        # Then
        # 19번째 줄이 삭제되고, 18번째 줄의 블록이 19번째 줄로 떨어짐
        assert board.grid[19][5] == "block"  # 블록이 아래로 떨어짐
        assert board.grid[18][5] is None     # 18번째 줄은 비어있음
