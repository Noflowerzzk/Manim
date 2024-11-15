from manim import *

from manim._config import *

config["tex_template"] = "ctex"

# DISABLE_SMART_IME

# Line_template = TexTemplate.from_file(r".\tex_template\Line_template.tex")
# Formula_template = TexTemplate.from_file(r".\tex_template\Formula_template.tex")
# Ch_tex_template = TexTemplate()

# Ch_tex_template.engine = "xelatex"
# Ch_tex_template.add_to_preamble(r"\usepackage[UTF8]{ctex}")
# Ch_tex_template.add_to_preamble(r"\setCJKmainfont{SimSun}")  # 指定字体


class Test_Video(Scene):
    
    def construct(self):
        
        # txt_1 = Text("This is a test")
        # txt_1.set_color(PINK)
        # txt_1.to_edge(UP)

        # self.wait()

        # self.add(txt_1)
        
        # self.play(Write(txt_1))
        # self.wait()
        # self.play(FadeOut(txt_1))
        
        # sqrt = MathTex(r"\sqrt{a^2 + b^2} = c")
        # self.play(Write(sqrt))
        # self.wait(2)
        # self.play(FadeOut(sqrt))
        
        self.MyLogo()
                
        # LaTexLable = MathTex(r"\text{\LaTeX}")
        
        # self.wait(0.5)
        # self.play(Write(LaTexLable))
        # self.play(FadeOut(LaTexLable))
        
        # self.ShowHolder()
                
                
    def MyLogo(self):
        # 三个圆
        circle = [0, 0, 0]
            
        circle[0] = Circle(radius=1, color=BLUE).set_fill(color=BLUE, opacity=.3)  # 半径为 1，颜色为蓝色
        circle[1] = Circle(radius=1.5, color=GREEN).set_fill(color=GREEN, opacity=.3)   # 半径为 2，颜色为红色
        circle[2] = Circle(radius=0.5, color=GOLD).set_fill(color=GOLD, opacity=.3) # 半径为 0.5，颜色为绿色
        
        # 设置它们的位置
        circle[0].move_to(LEFT * 2.1 + DOWN * 1)  # 将第一个圆形移动到左侧
        circle[1].move_to(UP * 1.5 + RIGHT * 0.2)    # 将第二个圆形移动到屏幕中央
        circle[2].move_to(RIGHT * 1.9 + DOWN * 1.7) # 将第三个圆形移动到右侧
        
        
        self.wait(.5)
        # 播放动画，显示三个圆形
        self.play(Create(circle[0]), Create(circle[1]), Create(circle[2]))
        # 等待
        self.wait(.5)
        
        # 标题
        # 创建文字 "TriCirc"
        tri = Text("Tri", font_size=96, color=BLUE)  # 大小为96的蓝色 "Tri"
        circ = Text("Circ", font_size=72, color=GREEN)  # 较小的红色 "Circ"
        
        # 调整位置，稍微错开
        tri.shift(LEFT * .5 + DOWN * .5)  # "Tri" 向上微调
        circ.next_to(tri, RIGHT * 0.5)  # "Circ" 位于 "Tri" 的右侧
        
        tri.set_stroke(color=BLUE)
        circ.set_stroke(color=GREEN)
                
        # 渲染文字
        self.play(Write(tri), Write(circ))
        self.wait(.7)
        
        self.play(FadeOut(circle[0], circle[1], circle[2], tri, circ))
        # # 三条根轴
        # # 设置直线的颜色
        # line_color = BLUE
        
        # # 对应的根轴方程： y = 1.087x + 1.283, y = -0.175x - 1.368, y = -1.882x + 1.876
        # def line1_func(x):
        #     return -0.92 * x + 0.874

        # def line2_func(x):
        #     return 5.71 * x + 1.31

        # def line3_func(x):
        #     return 0.531 * x - 0.97

        
        # # 创建三条根轴直线
        # line1 = Line(start=LEFT * 4 + UP * line1_func(-4), end=RIGHT * 4 + UP * line1_func(4), color=line_color)
        # line2 = Line(start=LEFT * 4 + UP * line2_func(-4), end=RIGHT * 4 + UP * line2_func(4), color=line_color)
        # line3 = Line(start=LEFT * 4 + UP * line3_func(-4), end=RIGHT * 4 + UP * line3_func(4), color=line_color)


        # # 渲染三条直线
        # self.play(Create(line1))
        # self.play(Create(line2))
        # self.play(Create(line3))

                    
        
    def ShowHolder(self):
        Thrm = MathTex(
            r"& p, q \neq 0 \text{ 或 } 1, \frac{1}{p} + \frac{1}{q} = 1, \\",
            r"& \text{则对任意正数数列 } \{a_k\}_{k=1}^n, \{b_k\}_{k=1}^n, \text{ 有} \\",
            r"& \sum_{i = 1}^n a_ib_i \leqslant \left(\sum_{i = 1}^{n}a_i^p\right)^{\frac{1}{p}} \cdot \left(\sum_{i = 1}^{n}b_i^q\right)^{\frac{1}{q}}  \quad p > 1 \\",
            r"& \sum_{i = 1}^n a_ib_i \geqslant \left(\sum_{i = 1}^{n}a_i^p\right)^{\frac{1}{p}} \cdot \left(\sum_{i = 1}^{n}b_i^q\right)^{\frac{1}{q}}  \quad p < 1",
            tex_environment="align*",
        )
        Thrm.font_size = 24

        # 将文本左对齐并居中
        Thrm.to_corner(UL)  
        # 渲染动画
        self.play(Write(Thrm))
        self.wait(2)        
        