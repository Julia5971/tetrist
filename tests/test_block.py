import pytest
from game.block import Block, BlockType, BLOCK_SHAPES

class TestBlock:
    """블록 클래스 테스트"""
    
    def test_block_creation(self):
        """블록이 올바른 모양으로 생성되는지 테스트"""
        # Given
        block_type = BlockType.I
        x, y = 5, 0
        
        # When
        block = Block(block_type, x, y)
        
        # Then
        assert block.block_type == BlockType.I
        assert block.x == 5
        assert block.y == 0
        assert block.rotation == 0
        assert len(block.get_coordinates()) == 4  # I 블록은 4칸
    
    def test_block_rotation(self):
        """블록이 90도씩 올바르게 회전하는지 테스트"""
        # Given
        block = Block(BlockType.L, 0, 0)
        initial_coords = block.get_coordinates()
        
        # When
        block.rotate()
        
        # Then
        rotated_coords = block.get_coordinates()
        assert rotated_coords != initial_coords
        assert block.rotation == 1
        
        # 4번 회전하면 원래 모양으로 돌아와야 함
        for _ in range(3):
            block.rotate()
        final_coords = block.get_coordinates()
        assert final_coords == initial_coords
    
    def test_block_move(self):
        """블록이 올바르게 이동하는지 테스트"""
        # Given
        block = Block(BlockType.O, 3, 4)
        
        # When
        block.move(1, 1)  # 오른쪽으로 1, 아래로 1
        
        # Then
        assert block.x == 4
        assert block.y == 5
    
    def test_i_block_shape(self):
        """I 블록의 모양이 올바른지 테스트"""
        # Given
        block = Block(BlockType.I, 0, 0)
        
        # When
        coords = block.get_coordinates()
        
        # Then
        expected_coords = [(0, 0), (1, 0), (2, 0), (3, 0)]
        assert set(coords) == set(expected_coords)
    
    def test_l_block_rotation_coordinates(self):
        """L 블록의 회전 후 좌표가 올바른지 테스트"""
        # Given
        block = Block(BlockType.L, 5, 5)
        
        # When - 첫 번째 회전
        block.rotate()
        coords_90 = block.get_coordinates()
        
        # When - 두 번째 회전
        block.rotate()
        coords_180 = block.get_coordinates()
        
        # Then - 회전된 좌표들이 다르고 올바른 개수여야 함
        assert len(coords_90) == 4
        assert len(coords_180) == 4
        assert coords_90 != coords_180
    
    def test_all_block_types_creation(self):
        """모든 블록 타입이 올바르게 생성되는지 테스트"""
        # Given
        block_types = [BlockType.I, BlockType.O, BlockType.T, 
                      BlockType.S, BlockType.Z, BlockType.J, BlockType.L]
        
        # When & Then
        for block_type in block_types:
            block = Block(block_type, 0, 0)
            assert block.block_type == block_type
            assert block.get_coordinates() is not None
            assert len(block.get_coordinates()) == 4
    
    def test_block_coordinates_include_position(self):
        """블록 좌표에 위치가 올바르게 반영되는지 테스트"""
        # Given
        block = Block(BlockType.O, 10, 20)
        
        # When
        coords = block.get_coordinates()
        
        # Then - 모든 좌표가 x=10, y=20 기준으로 계산되어야 함
        base_x, base_y = block.x, block.y
        for coord in coords:
            assert coord[0] >= base_x  # x 좌표는 기준점 이상
            assert coord[1] >= base_y  # y 좌표는 기준점 이상
