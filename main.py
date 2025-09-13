#!/usr/bin/env python3
"""
테트리스 게임 메인 실행 파일
"""

from game.game import Game
from game.renderer import GameRenderer

def main():
    """메인 함수"""
    print("Starting Tetris Game!")
    print("Screen Size: 1536x1152 (150% enlarged)")
    print("Controls:")
    print("  ← → : Move Block")
    print("  ↓ : Fast Drop")
    print("  ↑ : Rotate Block")
    print("  Space : Instant Drop")
    print("  P : Pause")
    print("  R : Restart")
    print("  ESC : Exit")
    print()
    
    # 게임 및 렌더러 초기화 (1536x1152 화면)
    game = Game()
    renderer = GameRenderer(1536, 1152)  # 1024x768의 150%
    
    # 첫 블록 생성
    game.spawn_new_block()
    
    try:
        # 게임 루프 실행
        renderer.run_game_loop(game)
    except KeyboardInterrupt:
        print("\nGame ended.")
    finally:
        renderer.cleanup()

if __name__ == "__main__":
    main()
