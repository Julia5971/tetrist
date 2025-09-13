import pygame
from typing import Tuple, Optional
from .game import Game
from .block import Block, BlockType
from .board import Board
import random

class GameRenderer:
    """테트리스 게임 렌더링 클래스"""
    
    def __init__(self, width: int = 800, height: int = 600):
        """렌더러 초기화"""
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("테트리스 게임")
        
        # 일시정지 상태 추가
        self.paused = False  # 최소한의 구현
        
        # 다채로운 색상 정의
        self.colors = {
            'background': (15, 15, 35),  # 어두운 네이비 배경
            'grid': (40, 40, 60),  # 어두운 회색 그리드
            'block': (255, 255, 255),  # 흰색 블록 (기본)
            'text': (255, 255, 255),  # 흰색 텍스트
            'red': (255, 80, 80),  # 밝은 빨간색
            'yellow': (255, 255, 100),  # 밝은 노란색
            'green': (80, 255, 80),  # 밝은 초록색
            'blue': (80, 80, 255),  # 밝은 파란색
            'orange': (255, 180, 80),  # 밝은 주황색
            'purple': (200, 80, 255),  # 밝은 보라색
            'cyan': (80, 255, 255),  # 밝은 청록색
            'pink': (255, 150, 200),  # 핑크색
            'lime': (150, 255, 150),  # 라임색
            'gold': (255, 215, 0),  # 금색
            'silver': (192, 192, 192),  # 은색
        }
        
        # 폰트 초기화
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # 게임 보드 크기 및 위치
        self.board_width = 10
        self.board_height = 20
        self.cell_size = 30
        self.board_x = 50
        self.board_y = 50
    
    def render_game(self, game: Game):
        """전체 게임 화면 렌더링"""
        # 배경 그리기
        self.screen.fill(self.colors['background'])
        
        # 게임 보드 그리기
        self.render_board(game.board)
        
        # 현재 블록 그리기
        if game.current_block:
            self.render_block(game.current_block)
        
        # UI 요소 그리기
        self.render_ui(game)
        
        # 일시정지 화면 그리기
        if self.paused:
            self.render_pause_screen()
        
        # 화면 업데이트
        pygame.display.flip()
    
    def render_board(self, board: Board):
        """게임 보드 렌더링"""
        # 보드 배경 그리기
        board_rect = pygame.Rect(
            self.board_x, 
            self.board_y, 
            self.board_width * self.cell_size, 
            self.board_height * self.cell_size
        )
        pygame.draw.rect(self.screen, self.colors['grid'], board_rect)
        
        # 보드 그리드 그리기
        for x in range(self.board_width + 1):
            start_pos = (self.board_x + x * self.cell_size, self.board_y)
            end_pos = (self.board_x + x * self.cell_size, self.board_y + self.board_height * self.cell_size)
            pygame.draw.line(self.screen, self.colors['grid'], start_pos, end_pos, 1)
        
        for y in range(self.board_height + 1):
            start_pos = (self.board_x, self.board_y + y * self.cell_size)
            end_pos = (self.board_x + self.board_width * self.cell_size, self.board_y + y * self.cell_size)
            pygame.draw.line(self.screen, self.colors['grid'], start_pos, end_pos, 1)
        
        # 배치된 블록들 그리기 (색상 유지)
        for y in range(self.board_height):
            for x in range(self.board_width):
                if board.grid[y][x] is not None:
                    self.render_cell(x, y, board.grid[y][x])
    
    def get_block_color(self, block_type):
        """블록 타입에 따른 색상 반환"""
        color_map = {
            BlockType.I: self.colors['cyan'],  # I 블록: 밝은 청록색
            BlockType.O: self.colors['yellow'],  # O 블록: 밝은 노란색
            BlockType.T: self.colors['purple'],  # T 블록: 밝은 보라색
            BlockType.S: self.colors['green'],  # S 블록: 밝은 초록색
            BlockType.Z: self.colors['red'],  # Z 블록: 밝은 빨간색
            BlockType.J: self.colors['blue'],  # J 블록: 밝은 파란색
            BlockType.L: self.colors['orange'],  # L 블록: 밝은 주황색
        }
        return color_map.get(block_type, self.colors['block'])
    
    def render_block(self, block: Block):
        """현재 블록 렌더링"""
        block_color = self.get_block_color(block.block_type)
        
        # 블록의 각 셀을 그리기
        for x, y in block.get_cells():
            screen_x = self.board_x + (block.x + x) * self.cell_size
            screen_y = self.board_y + (block.y + y) * self.cell_size
            
            # 블록이 보드 범위 내에 있을 때만 그리기
            if 0 <= block.x + x < self.board_width and 0 <= block.y + y < self.board_height:
                cell_rect = pygame.Rect(screen_x, screen_y, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, block_color, cell_rect)
                pygame.draw.rect(self.screen, self.colors['grid'], cell_rect, 1)
    
    def render_cell(self, x: int, y: int, cell_value):
        """개별 셀 렌더링 (배치된 블록)"""
        # 블록 타입에 따른 색상 적용
        if isinstance(cell_value, BlockType):
            block_color = self.get_block_color(cell_value)
        else:
            block_color = self.colors['block']  # 기본 흰색
        
        cell_rect = pygame.Rect(
            self.board_x + x * self.cell_size, 
            self.board_y + y * self.cell_size, 
            self.cell_size, 
            self.cell_size
        )
        pygame.draw.rect(self.screen, block_color, cell_rect)
        pygame.draw.rect(self.screen, self.colors['grid'], cell_rect, 1)
    
    def render_ui(self, game: Game):
        """UI 요소 렌더링"""
        # 점수 표시 (금색)
        score_text = self.font.render(f"점수: {game.score}", True, self.colors['gold'])
        self.screen.blit(score_text, (400, 50))
        
        # 레벨 표시 (파란색)
        level_text = self.font.render(f"레벨: {game.level}", True, self.colors['blue'])
        self.screen.blit(level_text, (400, 100))
        
        # 삭제된 줄 수 표시 (라임색)
        lines_text = self.font.render(f"줄: {game.lines_cleared}", True, self.colors['lime'])
        self.screen.blit(lines_text, (400, 150))
        
        # 다음 블록 미리보기
        self.render_next_block_preview(game)
        
        # 게임 오버 메시지
        if game.game_over:
            self.render_game_over_screen()
    
    def render_next_block_preview(self, game: Game):
        """다음 블록 미리보기 렌더링"""
        # 다음 블록 미리보기 영역
        preview_x = 400
        preview_y = 200
        
        # 미리보기 제목 (은색)
        preview_title = self.small_font.render("다음 블록:", True, self.colors['silver'])
        self.screen.blit(preview_title, (preview_x, preview_y))
        
        # 다음 블록 그리기
        next_block = game.get_next_block_preview()
        if next_block:
            # 미리보기 블록을 중앙에 배치
            preview_cell_size = 25
            block_width = max([x for x, y in next_block.get_cells()]) + 1
            block_height = max([y for x, y in next_block.get_cells()]) + 1
            
            center_x = preview_x + (4 * preview_cell_size - block_width * preview_cell_size) // 2
            center_y = preview_y + 40
            
            self.render_preview_block(next_block, center_x, center_y, preview_cell_size)
    
    def render_preview_block(self, block: Block, x: int, y: int, cell_size: int = 20):
        """미리보기 블록 렌더링"""
        block_color = self.get_block_color(block.block_type)
        
        for block_x, block_y in block.get_cells():
            screen_x = x + block_x * cell_size
            screen_y = y + block_y * cell_size
            
            cell_rect = pygame.Rect(screen_x, screen_y, cell_size, cell_size)
            pygame.draw.rect(self.screen, block_color, cell_rect)
            pygame.draw.rect(self.screen, self.colors['grid'], cell_rect, 1)
    
    def render_game_over_screen(self):
        """게임 오버 화면 렌더링"""
        # 반투명 오버레이
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        # 게임 오버 메시지 (빨간색)
        game_over_text = self.font.render("게임 오버!", True, self.colors['red'])
        text_rect = game_over_text.get_rect(center=(self.width // 2, self.height // 2 - 50))
        self.screen.blit(game_over_text, text_rect)
        
        # 재시작 안내 (핑크색)
        restart_text = self.small_font.render("R키를 눌러 재시작", True, self.colors['pink'])
        restart_rect = restart_text.get_rect(center=(self.width // 2, self.height // 2 + 20))
        self.screen.blit(restart_text, restart_rect)
    
    def cleanup(self):
        """리소스 정리"""
        pygame.quit()
    
    def handle_key_press(self, key: int, game: Game):
        """키 입력 처리"""
        if game.game_over:
            if key == pygame.K_r:
                game.reset_game()
            return
        
        # 게임 컨트롤
        if key == pygame.K_LEFT:
            game.move_block_left()
        elif key == pygame.K_RIGHT:
            game.move_block_right()
        elif key == pygame.K_DOWN:
            game.move_block_down()
        elif key == pygame.K_UP:
            game.rotate_block()
        elif key == pygame.K_SPACE:
            game.drop_block_to_bottom()
        elif key == pygame.K_p:
            self.paused = not self.paused  # 최소한의 구현
        elif key == pygame.K_r:
            game.reset_game()
        elif key == pygame.K_ESCAPE:
            # ESC 키로 게임 종료
            return False  # False를 반환하여 게임 루프 종료
    
    def handle_events(self, game: Game):
        """키보드 이벤트 처리"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                result = self.handle_key_press(event.key, game)
                if result is False:  # ESC 키나 다른 종료 조건
                    return False
        
        return True
    
    def render_pause_screen(self):
        """일시정지 화면 렌더링 (완전한 구현)"""
        # 반투명 오버레이
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        # 일시정지 메시지
        pause_text = self.font.render("일시정지", True, self.colors['yellow'])
        text_rect = pause_text.get_rect(center=(self.width // 2, self.height // 2 - 50))
        self.screen.blit(pause_text, text_rect)
        
        # 재개 안내
        resume_text = self.small_font.render("P키를 눌러 재개", True, self.colors['green'])
        resume_rect = resume_text.get_rect(center=(self.width // 2, self.height // 2 + 20))
        self.screen.blit(resume_text, resume_rect)
    
    def run_game_loop(self, game: Game):
        """메인 게임 루프 실행"""
        clock = pygame.time.Clock()
        running = True
        last_drop_time = pygame.time.get_ticks()
        
        while running:
            current_time = pygame.time.get_ticks()
            
            # 이벤트 처리
            running = self.handle_events(game)
            
            # 게임 로직 업데이트 (일시정지가 아닐 때만)
            if not game.game_over and not self.paused:
                self.update_game_logic(game, current_time, last_drop_time)
                last_drop_time = current_time
            
            # 화면 렌더링
            self.render_game(game)
            
            # FPS 제한
            clock.tick(60)
        
        self.cleanup()
    
    def update_game_logic(self, game: Game, current_time: int, last_drop_time: int):
        """게임 로직 업데이트"""
        # 블록 자동 낙하
        drop_interval = int(1000 / game.get_drop_speed())  # 밀리초 단위
        
        if current_time - last_drop_time >= drop_interval:
            if not game.move_block_down():
                # 블록이 바닥에 닿았으면 새 블록 생성
                game.spawn_new_block()
                if game.current_block and game.board.check_collision(game.current_block):
                    game.game_over = True
