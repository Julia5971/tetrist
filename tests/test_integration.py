import pytest
import pygame
from game.game import Game
from game.renderer import GameRenderer

class TestGameIntegration:
    """게임 통합 테스트"""
    
    def test_full_game_integration(self):
        """전체 게임 통합 테스트"""
        # Given
        pygame.init()
        game = Game()
        renderer = GameRenderer()
        
        # When
        game.spawn_new_block()
        
        # Then
        assert game.current_block is not None
        assert not game.game_over
        
        pygame.quit()
    
    def test_game_controls_integration(self):
        """게임 컨트롤 통합 테스트"""
        # Given
        pygame.init()
        game = Game()
        renderer = GameRenderer()
        game.spawn_new_block()
        
        # When
        initial_x = game.current_block.x
        renderer.handle_key_press(pygame.K_LEFT, game)
        
        # Then
        assert game.current_block.x == initial_x - 1
        
        pygame.quit()
    
    def test_game_scoring_integration(self):
        """게임 점수 시스템 통합 테스트"""
        # Given
        pygame.init()
        game = Game()
        renderer = GameRenderer()
        
        # When - 1줄 삭제
        for x in range(10):
            game.board.grid[19][x] = "filled"
        game.clear_full_lines()
        
        # Then
        assert game.score > 0
        assert game.lines_cleared == 1
        
        pygame.quit()
