from typing import List, Optional, Tuple
from game.block import Block

class Board:
    """테트리스 게임 보드 클래스"""
    
    def __init__(self, width: int = 12, height: int = 20):  # width를 12로 변경
        """보드 초기화"""
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
    
    def is_valid_position(self, x: int, y: int) -> bool:
        """
        주어진 위치가 보드 내부에 있는지 확인
        
        Args:
            x: x 좌표
            y: y 좌표
            
        Returns:
            bool: 유효한 위치면 True, 그렇지 않으면 False
        """
        return 0 <= x < self.width and 0 <= y < self.height
    
    def place_block(self, block: Block):
        """블록을 보드에 배치"""
        for x, y in block.get_coordinates():
            if 0 <= x < self.width and 0 <= y < self.height:
                # 블록 타입 정보를 함께 저장
                self.grid[y][x] = block.block_type
    
    def check_collision(self, block: Block) -> bool:
        """
        블록이 다른 블록이나 경계와 충돌하는지 확인
        
        Args:
            block: 확인할 블록
            
        Returns:
            bool: 충돌하면 True, 그렇지 않으면 False
        """
        coordinates = block.get_coordinates()
        
        for x, y in coordinates:
            # 경계 확인
            if not self.is_valid_position(x, y):
                return True
            
            # 다른 블록과의 충돌 확인
            if self.grid[y][x] is not None:
                return True
        
        return False
    
    def remove_block(self, block: Block):
        """
        블록을 보드에서 제거
        
        Args:
            block: 제거할 블록
        """
        coordinates = block.get_coordinates()
        for x, y in coordinates:
            if self.is_valid_position(x, y):
                self.grid[y][x] = None
    
    def get_full_lines(self) -> List[int]:
        """
        가득 찬 줄의 인덱스를 반환
        
        Returns:
            List[int]: 가득 찬 줄의 y 좌표 리스트
        """
        full_lines = []
        for y in range(self.height):
            if all(cell is not None for cell in self.grid[y]):
                full_lines.append(y)
        return full_lines
    
    def clear_full_lines(self):
        """가득 찬 줄들을 삭제하고 위의 블록들을 아래로 이동"""
        full_lines = self.get_full_lines()
        
        if full_lines:
            # 가득 찬 줄들을 삭제
            for line in full_lines:
                del self.grid[line]
                # 맨 위에 빈 줄 추가
                self.grid.insert(0, [None] * self.width)
        
        return len(full_lines)
    
    def is_empty(self, x: int, y: int) -> bool:
        """
        주어진 위치가 비어있는지 확인
        
        Args:
            x: x 좌표
            y: y 좌표
            
        Returns:
            bool: 비어있으면 True, 그렇지 않으면 False
        """
        if not self.is_valid_position(x, y):
            return False
        return self.grid[y][x] is None
    
    def visualize(self) -> str:
        """
        보드를 텍스트로 시각화
        
        Returns:
            str: 보드의 시각적 표현
        """
        result = "게임 보드:\n"
        result += "  " + "".join([str(i % 10) for i in range(self.width)]) + "\n"
        
        for y in range(self.height):
            result += f"{y:2d}"
            for x in range(self.width):
                if self.grid[y][x] is None:
                    result += "."
                else:
                    result += self.grid[y][x]
            result += "\n"
        
        return result
    
    def __str__(self) -> str:
        """보드의 문자열 표현"""
        return f"Board({self.width}x{self.height})"
    
    def __repr__(self) -> str:
        """보드의 디버그용 문자열 표현"""
        return self.__str__()

# 데모용 함수들 추가
if __name__ == "__main__":
    import sys
    import os
    
    # 현재 디렉토리를 Python path에 추가
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    from game.block import Block, BlockType
    
    print("=== 테트리스 게임 보드 데모 ===\n")
    
    # 1. 빈 보드 생성
    board = Board()
    print("1. 빈 보드:")
    print(board.visualize())
    
    # 2. 블록 배치 데모
    print("2. O 블록 배치 (위치 3, 5):")
    block1 = Block(BlockType.O, 3, 5)
    board.place_block(block1)
    print(board.visualize())
    
    # 3. 다른 블록 배치
    print("3. I 블록 배치 (위치 0, 0):")
    block2 = Block(BlockType.I, 0, 0)
    board.place_block(block2)
    print(board.visualize())
    
    # 4. L 블록 회전 데모
    print("4. L 블록 회전 데모:")
    for rotation in range(4):
        print(f"L 블록 회전 {rotation * 90}도:")
        from game.block import visualize_block
        print(visualize_block(BlockType.L, rotation))
        print()
    
    # 5. 충돌 감지 데모
    print("5. 충돌 감지 데모:")
    collision_block = Block(BlockType.O, 4, 5)  # 기존 블록과 겹침
    print(f"블록 (4,5)에 O 블록 배치 시도: 충돌 = {board.check_collision(collision_block)}")
    
    no_collision_block = Block(BlockType.O, 7, 7)  # 겹치지 않음
    print(f"블록 (7,7)에 O 블록 배치 시도: 충돌 = {board.check_collision(no_collision_block)}")
    
    # 6. 줄 삭제 데모
    print("\n6. 줄 삭제 데모:")
    # 19번째 줄을 가득 채움
    for x in range(10):
        board.grid[19][x] = "X"
    print("19번째 줄을 가득 채운 후:")
    print(board.visualize())
    
    print("줄 삭제 후:")
    board.clear_full_lines()
    print(board.visualize())
