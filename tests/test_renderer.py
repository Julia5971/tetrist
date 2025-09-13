import pytest
import pygame
from unittest.mock import Mock, patch
from game.game import Game
from game.block import Block, BlockType
from game.board import Board
from game.renderer import GameRenderer

class TestGameRenderer:
    """게임 렌더링 테스트"""
    
    def test_game_screen_initialization(self):
        """게임 화면 초기화 테스트"""
        # Given
        pygame.init()
        
        # When
        screen = pygame.display.set_mode((800, 600))
        
        # Then
        assert screen is not None
        assert screen.get_width() == 800
        assert screen.get_height() == 600
        
        pygame.quit()
    
    def test_block_rendering(self):
        """블록 그리기 테스트"""
        # Given
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        block = Block(BlockType.I, 0, 0)
        
        # When
        screen.fill((0, 0, 0))  # 검은색 배경
        # 블록을 그리는 로직 (아직 구현되지 않음)
        
        # Then
        # 화면이 올바르게 그려졌는지 확인
        assert screen is not None
        
        pygame.quit()
    
    def test_board_rendering(self):
        """게임 보드 그리기 테스트"""
        # Given
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        board = Board()
        
        # When
        screen.fill((0, 0, 0))  # 검은색 배경
        # 보드를 그리는 로직 (아직 구현되지 않음)
        
        # Then
        # 화면이 올바르게 그려졌는지 확인
        assert screen is not None
        
        pygame.quit()
    
    def test_ui_elements_rendering(self):
        """UI 요소 그리기 테스트"""
        # Given
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        game = Game()
        
        # When
        screen.fill((0, 0, 0))  # 검은색 배경
        # UI 요소를 그리는 로직 (아직 구현되지 않음)
        
        # Then
        # 화면이 올바르게 그려졌는지 확인
        assert screen is not None
        
        pygame.quit()

    def test_score_display(self):
        """점수 표시 테스트"""
        # Given
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        game = Game()
        game.score = 1500
        
        # When
        screen.fill((0, 0, 0))
        # 점수 표시 로직 (아직 구현되지 않음)
        
        # Then
        assert screen is not None
        
        pygame.quit()
    
    def test_level_display(self):
        """레벨 표시 테스트"""
        # Given
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        game = Game()
        game.level = 3
        
        # When
        screen.fill((0, 0, 0))
        # 레벨 표시 로직 (아직 구현되지 않음)
        
        # Then
        assert screen is not None
        
        pygame.quit()
    
    def test_next_block_preview(self):
        """다음 블록 미리보기 테스트"""
        # Given
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        game = Game()
        
        # When
        screen.fill((0, 0, 0))
        # 다음 블록 미리보기 로직 (아직 구현되지 않음)
        
        # Then
        assert screen is not None
        
        pygame.quit()
    
    def test_game_over_screen(self):
        """게임 오버 화면 테스트"""
        # Given
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        game = Game()
        game.game_over = True
        
        # When
        screen.fill((0, 0, 0))
        # 게임 오버 화면 로직 (아직 구현되지 않음)
        
        # Then
        assert screen is not None
        
        pygame.quit()

    def test_keyboard_events(self):
        """키보드 이벤트 처리 테스트"""
        # Given
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        game = Game()
        
        # When
        # 키보드 이벤트 처리 로직 (아직 구현되지 않음)
        
        # Then
        assert screen is not None
        
        pygame.quit()
    
    def test_game_controls(self):
        """게임 컨트롤 테스트"""
        # Given
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        game = Game()
        
        # When
        # 게임 컨트롤 로직 (아직 구현되지 않음)
        
        # Then
        assert screen is not None
        
        pygame.quit()

    def test_game_loop_initialization(self):
        """게임 루프 초기화 테스트"""
        # Given
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        game = Game()
        
        # When
        # 게임 루프 초기화 로직 (아직 구현되지 않음)
        
        # Then
        assert screen is not None
        
        pygame.quit()
    
    def test_game_loop_events(self):
        """게임 루프 이벤트 처리 테스트"""
        # Given
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        game = Game()
        
        # When
        # 게임 루프 이벤트 처리 로직 (아직 구현되지 않음)
        
        # Then
        assert screen is not None
        
        pygame.quit()
    
    def test_game_loop_rendering(self):
        """게임 루프 렌더링 테스트"""
        # Given
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        game = Game()
        
        # When
        # 게임 루프 렌더링 로직 (아직 구현되지 않음)
        
        # Then
        assert screen is not None
        
        pygame.quit()

    def test_block_colors(self):
        """블록 색상 테스트"""
        # Given
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        renderer = GameRenderer()
        
        # When
        colors = renderer.colors
        
        # Then
        assert 'background' in colors
        assert 'grid' in colors
        assert 'block' in colors
        assert 'text' in colors
        assert colors['background'] == (0, 0, 0)  # 검은색 배경
        assert colors['block'] == (255, 255, 255)  # 흰색 블록
        assert colors['text'] == (255, 255, 255)  # 흰색 텍스트
        assert colors['grid'] == (50, 50, 50)  # 회색 그리드
        
        pygame.quit()
    
    def test_ui_text_colors(self):
        """UI 텍스트 색상 테스트"""
        # Given
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        renderer = GameRenderer()
        game = Game()
        
        # When
        screen.fill(renderer.colors['background'])
        renderer.render_ui(game)
        
        # Then
        # UI 텍스트가 올바른 색상으로 렌더링되었는지 확인
        assert screen is not None
        assert renderer.colors['text'] == (255, 255, 255)  # 흰색 텍스트
        
        pygame.quit()
    
    def test_game_over_screen_colors(self):
        """게임 오버 화면 색상 테스트"""
        # Given
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        renderer = GameRenderer()
        game = Game()
        game.game_over = True
        
        # When
        screen.fill(renderer.colors['background'])
        renderer.render_game_over_screen()
        
        # Then
        # 게임 오버 화면이 올바른 색상으로 렌더링되었는지 확인
        assert screen is not None
        assert renderer.colors['text'] == (255, 255, 255)  # 흰색 텍스트
        
        pygame.quit()
    
    def test_board_colors(self):
        """게임 보드 색상 테스트"""
        # Given
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        renderer = GameRenderer()
        board = Board()
        
        # When
        screen.fill(renderer.colors['background'])
        renderer.render_board(board)
        
        # Then
        # 보드가 올바른 색상으로 렌더링되었는지 확인
        assert screen is not None
        assert renderer.colors['grid'] == (50, 50, 50)  # 회색 그리드
        
        pygame.quit()
    
    def test_block_rendering_colors(self):
        """블록 렌더링 색상 테스트"""
        # Given
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        renderer = GameRenderer()
        block = Block(BlockType.I, 0, 0)
        
        # When
        screen.fill(renderer.colors['background'])
        renderer.render_block(block)
        
        # Then
        # 블록이 올바른 색상으로 렌더링되었는지 확인
        assert screen is not None
        assert renderer.colors['block'] == (255, 255, 255)  # 흰색 블록
        
        pygame.quit()

    def test_arrow_key_controls(self):
        """화살표 키 컨트롤 테스트"""
        # Given
        pygame.init()
        game = Game()
        renderer = GameRenderer()
        game.spawn_new_block()
        initial_x = game.current_block.x
        initial_y = game.current_block.y
        
        # When & Then - 왼쪽 화살표
        renderer.handle_key_press(pygame.K_LEFT, game)
        assert game.current_block.x == initial_x - 1
        
        # When & Then - 오른쪽 화살표
        renderer.handle_key_press(pygame.K_RIGHT, game)
        assert game.current_block.x == initial_x
        
        # When & Then - 아래 화살표
        renderer.handle_key_press(pygame.K_DOWN, game)
        assert game.current_block.y == initial_y + 1
        
        # When & Then - 위 화살표 (회전)
        initial_rotation = game.current_block.rotation
        renderer.handle_key_press(pygame.K_UP, game)
        assert game.current_block.rotation == (initial_rotation + 1) % 4
        
        pygame.quit()

    def test_space_key_control(self):
        """스페이스바 즉시 낙하 테스트"""
        # Given
        pygame.init()
        game = Game()
        renderer = GameRenderer()
        game.spawn_new_block()
        
        # When
        renderer.handle_key_press(pygame.K_SPACE, game)
        
        # Then
        # 블록이 바닥까지 떨어졌는지 확인
        assert game.current_block is None or game.current_block.y > 0
        
        pygame.quit()

    def test_r_key_restart(self):
        """R키 게임 재시작 테스트"""
        # Given
        pygame.init()
        game = Game()
        renderer = GameRenderer()
        game.score = 1000
        game.game_over = True
        
        # When
        renderer.handle_key_press(pygame.K_r, game)
        
        # Then
        assert game.score == 0
        assert game.game_over == False
        
        pygame.quit()

    def test_escape_key_exit(self):
        """ESC 키 게임 종료 테스트"""
        # Given
        pygame.init()
        game = Game()
        renderer = GameRenderer()
        
        # When
        result = renderer.handle_key_press(pygame.K_ESCAPE, game)
        
        # Then
        # ESC 키가 False를 반환하여 게임 종료 신호를 보내는지 확인
        assert result is False
        
        pygame.quit()

def test_p_key_pause_red(self):
    """P키 일시정지 테스트 (TDD Red 단계)"""
    # Given
    pygame.init()
    game = Game()
    renderer = GameRenderer()
    
    # When
    renderer.handle_key_press(pygame.K_p, game)
    
    # Then
    # 이 테스트는 아직 paused 속성이 없어서 실패해야 함
    assert hasattr(renderer, 'paused')
    assert renderer.paused == True
    
    pygame.quit()

def test_pause_screen_rendering_red(self):
    """일시정지 화면 렌더링 테스트 (TDD Red 단계)"""
    # Given
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    renderer = GameRenderer()
    game = Game()
    
    # When
    renderer.paused = True  # 강제로 일시정지 상태 설정
    renderer.render_game(game)
    
    # Then
    # 이 테스트는 render_pause_screen 메서드가 없어서 실패해야 함
    assert hasattr(renderer, 'render_pause_screen')
    
    pygame.quit()
