from enum import Enum
from typing import List, Tuple

class BlockType(Enum):
    """테트리스 블록 타입 열거형"""
    I = "I"
    O = "O"
    T = "T"
    S = "S"
    Z = "Z"
    J = "J"
    L = "L"

# 7가지 테트리스 블록의 모든 회전 상태 정의
BLOCK_SHAPES = {
    BlockType.I: [
        [(0, 0), (1, 0), (2, 0), (3, 0)],  # 0도
        [(0, 0), (0, 1), (0, 2), (0, 3)],  # 90도
        [(0, 0), (1, 0), (2, 0), (3, 0)],  # 180도
        [(0, 0), (0, 1), (0, 2), (0, 3)]   # 270도
    ],
    BlockType.O: [
        [(0, 0), (1, 0), (0, 1), (1, 1)],  # O 블록: 모든 회전이 동일
        [(0, 0), (1, 0), (0, 1), (1, 1)],
        [(0, 0), (1, 0), (0, 1), (1, 1)],
        [(0, 0), (1, 0), (0, 1), (1, 1)]
    ],
    BlockType.T: [
        [(1, 0), (0, 1), (1, 1), (2, 1)],  # 0도
        [(0, 0), (0, 1), (1, 1), (0, 2)],  # 90도
        [(0, 0), (1, 0), (2, 0), (1, 1)],  # 180도
        [(1, 0), (0, 1), (1, 1), (1, 2)]   # 270도
    ],
    BlockType.S: [
        [(1, 0), (2, 0), (0, 1), (1, 1)],  # 0도
        [(0, 0), (0, 1), (1, 1), (1, 2)],  # 90도
        [(1, 0), (2, 0), (0, 1), (1, 1)],  # 180도
        [(0, 0), (0, 1), (1, 1), (1, 2)]   # 270도
    ],
    BlockType.Z: [
        [(0, 0), (1, 0), (1, 1), (2, 1)],  # 0도
        [(1, 0), (0, 1), (1, 1), (0, 2)],  # 90도
        [(0, 0), (1, 0), (1, 1), (2, 1)],  # 180도
        [(1, 0), (0, 1), (1, 1), (0, 2)]   # 270도
    ],
    BlockType.J: [
        [(0, 0), (0, 1), (1, 1), (2, 1)],  # 0도
        [(1, 0), (1, 1), (0, 2), (1, 2)],  # 90도
        [(0, 0), (1, 0), (2, 0), (2, 1)],  # 180도
        [(0, 0), (1, 0), (0, 1), (0, 2)]   # 270도
    ],
    BlockType.L: [
        [(2, 0), (0, 1), (1, 1), (2, 1)],  # 0도
        [(0, 0), (0, 1), (0, 2), (1, 2)],  # 90도
        [(0, 0), (1, 0), (2, 0), (0, 1)],  # 180도
        [(0, 0), (1, 0), (1, 1), (1, 2)]   # 270도
    ]
}

class Block:
    """테트리스 블록 클래스"""
    
    def __init__(self, block_type: BlockType, x: int, y: int):
        """
        블록 초기화
        
        Args:
            block_type: 블록 타입 (I, O, T, S, Z, J, L)
            x: 블록의 x 좌표
            y: 블록의 y 좌표
        """
        self.block_type = block_type
        self.x = x
        self.y = y
        self.rotation = 0  # 회전 상태 (0, 1, 2, 3)
    
    def get_coordinates(self) -> List[Tuple[int, int]]:
        """
        현재 회전 상태에서 블록의 모든 칸의 좌표를 반환
        
        Returns:
            List[Tuple[int, int]]: 블록의 각 칸의 (x, y) 좌표 리스트
        """
        # 현재 회전 상태에 맞는 모양 가져오기
        base_shape = BLOCK_SHAPES[self.block_type][self.rotation]
        
        # 블록의 실제 위치에 맞게 좌표 조정
        coordinates = []
        for rel_x, rel_y in base_shape:
            abs_x = self.x + rel_x
            abs_y = self.y + rel_y
            coordinates.append((abs_x, abs_y))
        
        return coordinates
    
    def rotate(self):
        """블록을 90도 시계방향으로 회전"""
        self.rotation = (self.rotation + 1) % 4
    
    def move(self, dx: int, dy: int):
        """
        블록을 지정된 거리만큼 이동
        
        Args:
            dx: x축 이동 거리
            dy: y축 이동 거리
        """
        self.x += dx
        self.y += dy
    
    def get_rotated_coordinates(self) -> List[Tuple[int, int]]:
        """
        회전된 상태의 좌표를 반환
        
        Returns:
            List[Tuple[int, int]]: 회전된 블록의 좌표 리스트
        """
        return self.get_coordinates()
    
    def __str__(self) -> str:
        """블록의 문자열 표현"""
        return f"Block({self.block_type.value}, x={self.x}, y={self.y}, rotation={self.rotation})"
    
    def __repr__(self) -> str:
        """블록의 디버그용 문자열 표현"""
        return self.__str__()

def visualize_block(block_type: BlockType, rotation: int = 0, size: int = 4) -> str:
    """
    블록을 텍스트로 시각화
    
    Args:
        block_type: 블록 타입
        rotation: 회전 상태 (0-3)
        size: 표시할 격자 크기
    
    Returns:
        str: 블록의 시각적 표현
    """
    # 빈 격자 생성
    grid = [['.' for _ in range(size)] for _ in range(size)]
    
    # 블록 좌표 가져오기
    shape = BLOCK_SHAPES[block_type][rotation]
    
    # 블록 표시
    for x, y in shape:
        if 0 <= x < size and 0 <= y < size:
            grid[y][x] = '█'
    
    # 문자열로 변환
    result = f"{block_type.value} 블록 (회전 {rotation * 90}도):\n"
    for row in grid:
        result += ' '.join(row) + '\n'
    
    return result

def show_all_blocks():
    """모든 블록의 모든 회전 상태를 표시"""
    result = "=== 모든 테트리스 블록 모양 ===\n\n"
    
    for block_type in BlockType:
        result += f"--- {block_type.value} 블록 ---\n"
        for rotation in range(4):
            result += visualize_block(block_type, rotation) + "\n"
        result += "\n"
    
    return result

# 테스트용 함수
if __name__ == "__main__":
    print(show_all_blocks())
