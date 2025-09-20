#!/usr/bin/env python3
"""
테트리스 게임 메인 실행 파일
"""

from game.game import Game
from game.renderer import GameRenderer

def main():
    """메인 함수"""


    print("테트리스 게임을 시작합니다! 🎮")
    print("컨트롤:")
    print("  ← → : 블록 이동")
    print("  ↓ : 블록 빠른 낙하")
    print("  ↑ : 블록 회전")
    print("  스페이스 : 블록 즉시 낙하")
    print("  P : 일시정지")
    print("  R : 게임 재시작")
    print("  ESC : 게임 종료")
    print()
    
    # 게임 및 렌더러 초기화
    game = Game()
    renderer = GameRenderer(1536, 1152)  # 1024x768의 150%

    
    # 첫 블록 생성
    game.spawn_new_block()
    
    try:
        # 게임 루프 실행
        renderer.run_game_loop(game)
    except KeyboardInterrupt:


        print("\n게임이 종료되었습니다.")

    finally:
        renderer.cleanup()

if __name__ == "__main__":
    main()
