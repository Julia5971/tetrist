import random
from typing import Optional
from .block import Block, BlockType
from .board import Board

class Game:
    """테트리스 게임 메인 클래스"""
    
    def __init__(self):
        """게임 초기화"""
        self.board = Board(12, 20)  # width를 12로 변경
        self.current_block: Optional[Block] = None
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.game_over = False
        self.drop_time = 0
        self.drop_interval = 1000  # 1초
    
    def spawn_new_block(self):
        """새 블록을 생성하고 보드 상단 중앙에 배치"""
        # 첫 번째 블록인 경우
        if self.current_block is None:
            # 현재 블록 생성
            block_type = random.choice(list(BlockType))
            self.current_block = Block(block_type, 4, 0)
            
            # 다음 블록도 생성
            block_type = random.choice(list(BlockType))
            self.next_block = Block(block_type, 4, 0)
        else:
            # 현재 블록이 있으면 다음 블록으로 교체
            self.current_block = self.next_block
            self.current_block.x = 4
            self.current_block.y = 0
            
            # 새로운 다음 블록 생성
            block_type = random.choice(list(BlockType))
            self.next_block = Block(block_type, 4, 0)
    
    def move_block_left(self):
        """현재 블록을 왼쪽으로 이동"""
        if self.current_block and self.can_move_block(-1, 0):
            self.current_block.move(-1, 0)
    
    def move_block_right(self):
        """현재 블록을 오른쪽으로 이동"""
        if self.current_block and self.can_move_block(1, 0):
            self.current_block.move(1, 0)
    
    def move_block_down(self):
        """현재 블록을 아래로 이동"""
        if self.current_block and self.can_move_block(0, 1):
            self.current_block.move(0, 1)
            return True
        else:
            # 더 이상 아래로 이동할 수 없으면 블록을 배치
            self.place_current_block()
            return False
    
    def rotate_block(self):
        """현재 블록을 회전"""
        if self.current_block and self.can_rotate_block():
            self.current_block.rotate()
    
    def drop_block_to_bottom(self):
        """현재 블록을 바닥까지 떨어뜨림"""
        if not self.current_block:
            return
        
        # 바닥이나 다른 블록에 닿을 때까지 아래로 이동
        while self.can_move_block(0, 1):
            self.current_block.move(0, 1)
        
        # 블록을 보드에 배치
        self.place_current_block()
    
    def can_move_block(self, dx: int, dy: int) -> bool:
        """블록이 지정된 방향으로 이동 가능한지 확인"""
        if not self.current_block:
            return False
        
        # 임시로 블록을 이동시켜서 충돌 확인
        original_x = self.current_block.x
        original_y = self.current_block.y
        
        self.current_block.x += dx
        self.current_block.y += dy
        
        can_move = not self.board.check_collision(self.current_block)
        
        # 블록 위치를 원래대로 복원
        self.current_block.x = original_x
        self.current_block.y = original_y
        
        return can_move
    
    def can_rotate_block(self) -> bool:
        """블록이 회전 가능한지 확인"""
        if not self.current_block:
            return False
        
        # 임시로 블록을 회전시켜서 충돌 확인
        original_rotation = self.current_block.rotation
        
        self.current_block.rotate()
        can_rotate = not self.board.check_collision(self.current_block)
        
        # 블록 회전을 원래대로 복원
        self.current_block.rotation = original_rotation
        
        return can_rotate
    
    def place_current_block(self):
        """현재 블록을 보드에 배치"""
        if not self.current_block:
            return
        
        # 블록을 보드에 배치
        self.board.place_block(self.current_block)
        
        # 줄 삭제 확인
        self.clear_full_lines()
        
        # 게임 오버 확인
        self.check_game_over()
        
        # 현재 블록을 다음 블록으로 교체
        if self.next_block:
            self.current_block = self.next_block
            self.current_block.x = 4
            self.current_block.y = 0
            # 새로운 다음 블록 생성
            block_type = random.choice(list(BlockType))
            self.next_block = Block(block_type, 4, 0)
        else:
            self.current_block = None
    
    def clear_full_lines(self):
        """가득 찬 줄들을 삭제하고 점수 업데이트"""
        full_lines = self.board.get_full_lines()
        
        if full_lines:
            # 줄 삭제
            self.board.clear_full_lines()
            
            # 점수 계산 (테트리스 표준 점수 시스템)
            lines_count = len(full_lines)
            if lines_count == 1:
                self.score += 100 * self.level
            elif lines_count == 2:
                self.score += 300 * self.level
            elif lines_count == 3:
                self.score += 500 * self.level
            elif lines_count == 4:  # 테트리스!
                self.score += 800 * self.level
            
            # 삭제된 줄 수 업데이트
            self.lines_cleared += lines_count
            
            # 레벨 업데이트
            self.update_level()
    
    def update_level(self):
        """레벨 업데이트 (10줄마다 레벨업)"""
        new_level = (self.lines_cleared // 10) + 1
        if new_level > self.level:
            self.level = new_level
    
    def check_game_over(self):
        """게임 오버 조건 확인"""
        # 맨 위 줄에 블록이 있으면 게임 오버
        if any(cell is not None for cell in self.board.grid[0]):
            self.game_over = True
            return
        
        # 현재 블록이 맨 위에서 시작할 수 없으면 게임 오버
        if self.current_block and self.current_block.y <= 0:
            self.game_over = True
    
    def get_next_block_preview(self) -> Optional[Block]:
        """다음 블록 미리보기 반환"""
        return self.next_block
    
    def get_drop_speed(self) -> float:
        """현재 레벨에 따른 블록 낙하 속도 반환"""
        # 레벨이 높을수록 빠르게 낙하
        return max(0.1, 1.0 - (self.level - 1) * 0.1)
    
    def reset_game(self):
        """게임을 초기 상태로 리셋"""
        self.board = Board()
        self.current_block = None
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.game_over = False
    
    def get_game_state(self) -> dict:
        """현재 게임 상태를 딕셔너리로 반환"""
        return {
            'score': self.score,
            'level': self.level,
            'lines_cleared': self.lines_cleared,
            'game_over': self.game_over,
            'current_block': self.current_block,
            'board': self.board.grid
        }
    
    def __str__(self) -> str:
        """게임의 문자열 표현"""
        return f"Game(score={self.score}, level={self.level}, lines_cleared={self.lines_cleared})"
    
    def __repr__(self) -> str:
        """게임의 디버그용 문자열 표현"""
        return self.__str__()
