# DISABLE_SMART_IME
from manim import *

from manim._config import *

config["tex_template"] = "ctex"

class ConvexFunction(Scene):
    
    def construct(self):
        
        # 片头
        self.MyLogo()
        
        self.DefineConvexFunction_1()
        
    def DefineConvexFunction_1(self):
        DefOfConvexFunction = MathTex(
            r"& \text{对于函数 }\ f(x) \text{ 定义域内任意两数 } x_1 < x_2, \text{ 有任意 } \lambda \in [0, 1], \text{ 满足} \\",
            r"& f(\lambda x_1 + (1 - \lambda) x_2) \leq \lambda f(x_1) + (1 - \lambda) f(x_2) \\",
            r"& \text{则 }\ f(x) \text{ 为其定义区间上的下凸函数.}",
            tex_environment="align*"            
        )
        
        DefOfConvexFunction.shift(UP * 2 + LEFT * 2).font_size = 30
        
        self.play(Write(DefOfConvexFunction))
        
        self.DefineConvexFunctionGraph()
        
        # 淡出所有对象
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        
        self.wait(3)
        
    def DefineConvexFunctionGraph(self):
        # 创建一个小型坐标轴
        axes = Axes(
            x_range=[-0.1, 3, 0.5],  # 设置 x 轴范围 [-2, 2]，步长为 1
            y_range=[-0.1, 2, 0.5],  # 设置 y 轴范围 [-1, 1]，步长为 0.5
            y_length=4.2,
            x_length=6.2,
            axis_config={"color": BLUE},  # 坐标轴颜色
            tips=True,  # 不显示坐标轴箭头
        ).to_corner(DR)
        
        # 添加坐标轴标签
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        def ConvexFunc(x):
            return 0.25 * x ** 3 - 0.75 * x + 0.8
        
        ConvexFuncGraph = axes.plot(
            ConvexFunc,
            color = RED_A,
            x_range=[-0.1, 2.3],
        )
                        
        dotA = Dot(
            axes.c2p(0, ConvexFunc(0)),
            color=GREEN
        )
        dotB = Dot(
            axes.c2p(2.25, ConvexFunc(2.25)),
            color=GREEN
        )
        
        line = Line(
            start=dotA.get_center(),
            end=dotB.get_center(),
            color=GREEN
        )
        
        # 比例
        t = ValueTracker(0.6)
        MovingDotColor = RED_C

        MovingDotOnLine = always_redraw(
            lambda: Dot(
                line.point_from_proportion(t.get_value()),
                color=MovingDotColor
            )
        )
        
        MovingDotOnCurve = always_redraw(
            lambda: Dot(
                axes.c2p(t.get_value() * 2.25, ConvexFunc(t.get_value() * 2.25)),
                color=MovingDotColor
            )
        )
        
        VerticalLine = always_redraw(
            lambda: DashedLine(
                start=MovingDotOnCurve, end=MovingDotOnLine,
                color=MovingDotColor
            ).set_stroke(width=3)
        )
        
        # lambda 标题
        LambdaInGraph = always_redraw(
            lambda: MathTex(
                r"\lambda = ",
                font_size=30
            ).next_to(VerticalLine, direction=RIGHT)
        )
        NumberInGraph = always_redraw(
            lambda: DecimalNumber(
                t.get_value(),
                num_decimal_places=2,
                font_size=30
            ).next_to(LambdaInGraph, direction=RIGHT)
        )
        
        # 将坐标轴与标签一起渲染
        self.play(
            Create(axes), Write(labels),
            Create(ConvexFuncGraph), 
            Create(dotA), Create(dotB),
        )
        self.play(Create(line), run_time=0.7)
        self.play(
            FadeIn(MovingDotOnLine), FadeIn(MovingDotOnCurve),
            Create(VerticalLine),
            Write(LambdaInGraph), Write(NumberInGraph),
            run_time=0.5
        )
        self.play(t.animate.set_value(1))
        self.play(t.animate.set_value(0))
        self.play(t.animate.set_value(0.4))
        
        self.wait(2)
        
    # def DefineConvexFunction_2(self):
        
        
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
        self.play(
            DrawBorderThenFill(circle[0], run_time=0.9), 
            DrawBorderThenFill(circle[1], run_time=0.9), 
            DrawBorderThenFill(circle[2], run_time=0.9)
        )
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
