# DISABLE_SMART_IME
from manim import *
from manim._config import *

config["tex_template"] = "ctex"
# config.quality = "low_quality"

class Lipschitz(Scene):
    
    def construct(self):
        # self.MyLogo()
        
        self.Lipschitz()
        
        self.wait()
        
    def Lipschitz(self):
        axes = Axes(
            x_range=[-0.1, 3, 0.5],
            y_range=[-0.1, 2, 0.5],
            y_length=4.2,
            x_length=6.2,
            axis_config={"color": BLUE},  # 坐标轴颜色
            tips=True,  # 不显示坐标轴箭头
        ).to_corner(DR)
        
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        def DispFunc(x):
            return (1.5 + (x - 1.5) ** 3 - 1 * (x - 1.5)) * 0.4 + 0.3
        
        Curve = axes.plot(
            DispFunc, 
            color = RED_A,
            x_range=[-0.1, 3]
        )
        
        xOfMoving = ValueTracker(0.3)
        
        dotP = always_redraw(
            lambda: Dot(
                axes.c2p(xOfMoving.get_value(), DispFunc(xOfMoving.get_value())),
                color=RED_C
            )
        )
        
        LabelP = always_redraw(
            lambda: MathTex("P(x_0, f(x_0))", font_size=30).next_to(dotP, LEFT + UP * 0.2)
        )
        
        k = ValueTracker(3)
        
        def PositiveLineFunc(x):
            return k.get_value() * (x - xOfMoving.get_value()) + DispFunc(xOfMoving.get_value())
        
        def NegativeLineFunc(x):
            return -k.get_value() * (x - xOfMoving.get_value()) + DispFunc(xOfMoving.get_value())
        
        def LineGenerator(Func):
            xMin = xOfMoving.get_value() - 0.2
            xMax = xOfMoving.get_value() + 0.2
            
            return Line(
                start=axes.c2p(xMin, Func(xMin)),
                end=axes.c2p(xMax, Func(xMax)),
                color=GREEN
            )
        
        PositiveLine = always_redraw(lambda: LineGenerator(PositiveLineFunc))
        NegativeLine = always_redraw(lambda: LineGenerator(NegativeLineFunc))
        
        ShadowTriangleLeft = always_redraw(
            lambda: Polygon(
                PositiveLine.get_start(), NegativeLine.get_start(), dotP.get_center(),
                color=GREEN,
                stroke_width=0
            ).set_opacity(.3)
        )
        
        
        ShadowTriangleRight = always_redraw(
            lambda: Polygon(
                PositiveLine.get_end(), NegativeLine.get_end(), dotP.get_center(),
                color=GREEN,
                stroke_width=0
            ).set_opacity(.3)
        )

        self.play(
            Create(axes), Write(labels),
            Create(Curve)
        )
        
        self.play(
            Create(dotP), Write(LabelP),
            Create(PositiveLine), Create(NegativeLine)
        )
        self.play(Create(ShadowTriangleLeft), Create(ShadowTriangleRight))
        
        self.play(xOfMoving.animate.set_value(0))
        self.play(xOfMoving.animate.set_value(3))
        self.play(xOfMoving.animate.set_value(1))
        
        
        
        
        
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
