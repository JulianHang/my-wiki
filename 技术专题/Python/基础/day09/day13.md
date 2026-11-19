# 案例

```python
class Game(object):
    # 定义类属性top_score
    top_scoe = 0
    
    def __init__(self, player_name):
        self.player_name = player_name
        
    # 定义静态方法, 用于输出游戏帮助信息
    @staticmethod
    def show_help():
        print('游戏帮助信息')
        
    @classmethod
    def show_top_score(cls):
        print(f'本游戏历史最高分:{cls.top_scoe}')

    def start_game(self):
        print(f'{self.player_name}, 游戏开始了, 你准备好了么')

# 实例化类生成实例对象
mario = Game('马里奥')
mario.start_game()

# 显示历史最高分
Game.show_top_score()

# 弹出帮助信息
Game.show_help()



```