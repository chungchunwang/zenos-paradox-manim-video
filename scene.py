from manim import * 
class Zeno(Scene):
    def titleScene(self):
      title = Text('Zeno\'s Paradox').scale(2).move_to(UP)
      subtitle = Text('Achilles and the Tortoise').move_to(DOWN *.5)
      self.play(Write(title), Write(subtitle))
      self.wait(3)
      self.clear()
    def zenosParadoxIntroductionScene(self):
      title = Text('What are Zeno\'s Paradoxes?', color=YELLOW).scale(1).to_edge(UP)
      details = Paragraph('Zeno’s paradoxes are a series of philosophical problems created',' by the Greek philosopher Zeno of Elea.','','They are mostly questions attempting to prove the motion is an','illusion. This is often achieved by Zeno using problems that','have infinitesimal components, and therefore his paradoxes','highlight some common misconceptions surrounding the field','of calculus.','','The most famous of these puzzles include:',' - The Dichotomy Paradox',' - The Achilles and the Tortoise Paradox',' - The Arrow Paradox').scale(0.5)
      action = Text("Let's investigate the Achilles and the Tortoise Paradox!", color = BLUE).scale(0.5).to_edge(DOWN)
      self.play(Write(title), Write(details))
      self.wait(32)
      self.play(Write(action))
      self.wait(5)
      self.clear()
    def problemIntroductionScene(self):
      problem = Paragraph('Suppose you have the hero Achilles taking part in a footrace against a tortoise.',' Achilles moves 2 units per second, while the tortoise moves 1 unit per second.',' The tortoise is 6 units ahead of Achilles. Will Achilles ever catch the tortoise?', alignment = "center").scale(0.5).move_to(UP * 3)
      self.play(Create(problem))
      achilles = Circle(radius=1, color=PINK, fill_opacity = 0.5).move_to(RIGHT*2.5)
      tortoise = Square(side_length=2, color=BLUE, fill_opacity = 0.5).move_to(LEFT*2.5)
      achillesLabel = Text('Achilles').scale(0.5).next_to(achilles, DOWN, buff=0.5)
      tortoiseLabel = Text('Tortoise').scale(0.5).next_to(tortoise, DOWN, buff=0.5)
      achillesSpeedLabel = Text('2 units/sec.', color=GREY).scale(0.5).next_to(achillesLabel, DOWN, buff=0.5)
      tortoiseSpeedLabel = Text('1 units/sec.', color=GREY).scale(0.5).next_to(tortoiseLabel, DOWN, buff=0.5)
      self.play(Create(achilles), Create(tortoise),Write(achillesLabel),Write(tortoiseLabel),Write(achillesSpeedLabel),Write(tortoiseSpeedLabel))
      self.wait(24)
      self.clear()
    def problemSimulationScene(self):
      numberLine = NumberLine(
            x_range=[0, 20, 1],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        )
      achilles = Circle(radius=0.2, color=PINK, fill_opacity = 0.5).move_to(numberLine.n2p(0))

      tortoise = Square(side_length=0.3, color=BLUE, fill_opacity = 0.5).move_to(numberLine.n2p(6))
      self.play(Create(numberLine))
      self.play(Create(achilles), Create(tortoise))
      self.wait(7)
      equationFirst = MathTex(r"2t = 6 + t").move_to(UP*1.5)
      equationSecond = MathTex(r"t = 6").move_to(UP*1.5)
      self.play(Write(equationFirst))
      self.play(Transform(equationFirst, equationSecond))
      self.play(achilles.animate.move_to(numberLine.n2p(16)), tortoise.animate.move_to(numberLine.n2p(16)), run_time = 7)
      self.wait(2)
      self.clear()
    def zenoMethodTitleScene(self):
      title = Text('Zeno\'s Method:')
      self.play(Write(title))
      self.wait(6)
      self.clear()
    def zenoMethodSimulationScene(self, iterations, setupWaitTime, crossWaitTime, cycleWaitTime, logArcs, animationTime = 1):
      numberLine = NumberLine(
            x_range=[0, 20, 1],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        )
      achillesPos = 0
      tortoisePos = 6
      timePos = 0
      time = Text('t='+str(timePos)).scale(0.5).to_edge(UR)
      achilles = Circle(radius=0.2, color=PINK, fill_opacity = 0.5).move_to(numberLine.n2p(achillesPos))
      tortoise = Square(side_length=0.3, color=BLUE, fill_opacity = 0.5).move_to(numberLine.n2p(tortoisePos))
      self.play(Create(numberLine), run_time = animationTime)
      self.play(Create(achilles), Create(tortoise), Write(time), run_time = animationTime)
      self.wait(setupWaitTime)
      target = Cross(scale_factor = 0.1).move_to(numberLine.n2p(tortoisePos))
      self.wait(crossWaitTime)
      self.play(Create(target), run_time = animationTime)
      arc = None
      desc = None
      arcListTitle = Text('Lengths: ').scale(0.5).to_edge(UL)
      arcListLast = arcListTitle
      if logArcs:
        self.play(Write(arcListTitle), run_time = animationTime)
      for iter in range(iterations):
        timeStep = (tortoisePos - achillesPos)/2
        timePos += timeStep
        achillesPos = tortoisePos
        tortoisePos += timeStep
        newTime = Text('t='+str(timePos)).scale(0.5).to_edge(UR)
        if arc == None:
          arc= ArcBetweenPoints(start=numberLine.n2p(achillesPos) + DOWN *0.5, end=numberLine.n2p(tortoisePos) + DOWN *0.5, stroke_color=YELLOW)
          desc = Text('Small distance').scale(0.5).next_to(arc, DOWN, buff=0.5)
          self.play(achilles.animate.move_to(numberLine.n2p(achillesPos)), tortoise.animate.move_to(numberLine.n2p(tortoisePos)), Transform(time, newTime), run_time = animationTime)
          self.play(Create(arc), Write(desc), run_time = animationTime)
          self.play(target.animate.move_to(numberLine.n2p(tortoisePos)), run_time = animationTime)
        else:
          newArc= ArcBetweenPoints(start=numberLine.n2p(achillesPos) + DOWN *0.5, end=numberLine.n2p(tortoisePos) + DOWN *0.5, stroke_color=YELLOW)
          self.play(achilles.animate.move_to(numberLine.n2p(achillesPos)), tortoise.animate.move_to(numberLine.n2p(tortoisePos)), Transform(time, newTime), Transform(arc, newArc), desc.animate.next_to(newArc, DOWN, buff=0.5), run_time = animationTime)
        if logArcs:
          shiftArc = ArcBetweenPoints(start=numberLine.n2p(achillesPos) + DOWN *0.5, end=numberLine.n2p(tortoisePos) + DOWN *0.5, stroke_color=YELLOW)
          self.add(shiftArc)
          self.play(shiftArc.animate.next_to(arcListLast, RIGHT, buff = 0.5), run_time = animationTime)
          arcListLast = shiftArc
        self.play(target.animate.move_to(numberLine.n2p(tortoisePos)), run_time = animationTime)
        self.wait(cycleWaitTime)
    def zenoMethodSimulationFirstScene(self, iterations, setupWaitTime, crossWaitTime, cycleWaitTime):
      numberLine = NumberLine(
            x_range=[0, 20, 1],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        )
      achillesPos = 0
      tortoisePos = 6
      timePos = 0
      time = Text('t='+str(timePos)).scale(0.5).to_edge(UR)
      achilles = Circle(radius=0.2, color=PINK, fill_opacity = 0.5).move_to(numberLine.n2p(achillesPos))
      tortoise = Square(side_length=0.3, color=BLUE, fill_opacity = 0.5).move_to(numberLine.n2p(tortoisePos))
      self.play(Create(numberLine))
      self.play(Create(achilles), Create(tortoise), Create(time))
      self.wait(setupWaitTime)
      target = Cross(scale_factor = 0.1).move_to(numberLine.n2p(tortoisePos))
      self.wait(crossWaitTime)
      self.play(Create(target))
      arc = None
      desc = None
      for iter in range(iterations):
        timeStep = (tortoisePos - achillesPos)/2
        timePos += timeStep
        achillesPos = tortoisePos
        tortoisePos += timeStep
        newTime = Text('t='+str(timePos)).scale(0.5).to_edge(UR)
        if arc == None:
          arc= ArcBetweenPoints(start=numberLine.n2p(achillesPos) + DOWN *0.5, end=numberLine.n2p(tortoisePos) + DOWN *0.5, stroke_color=YELLOW)
          desc = Text('Small distance').scale(0.5).next_to(arc, DOWN, buff=0.5)
          self.play(achilles.animate.move_to(numberLine.n2p(achillesPos)), tortoise.animate.move_to(numberLine.n2p(tortoisePos)), Transform(time, newTime))
          self.play(Create(arc), Create(desc))
          self.play(target.animate.move_to(numberLine.n2p(tortoisePos)))
        else:
          newArc= ArcBetweenPoints(start=numberLine.n2p(achillesPos) + DOWN *0.5, end=numberLine.n2p(tortoisePos) + DOWN *0.5, stroke_color=YELLOW)
          self.play(achilles.animate.move_to(numberLine.n2p(achillesPos)), tortoise.animate.move_to(numberLine.n2p(tortoisePos)), Transform(time, newTime), Transform(arc, newArc), desc.animate.next_to(newArc, DOWN, buff=0.5))
        self.play(target.animate.move_to(numberLine.n2p(tortoisePos)))
        self.wait(cycleWaitTime)
    def areYouConvincedScene(self):
        q1 = Text('Are you convinced?').move_to(UP*2)
        q2 = Text('Where did it go wrong?', color=BLUE).move_to(DOWN*2)
        # create a pause button using circles and rectangles
        pause = VGroup(
            Circle(radius=0.75, color=RED, fill_opacity = 0.5),
            Rectangle(width=0.1, height=0.5, color=WHITE, fill_opacity = 0.5).move_to(LEFT*0.2),
            Rectangle(width=0.1, height=0.5, color=WHITE, fill_opacity = 0.5).move_to(RIGHT*0.2)
        )
        self.play(Create(q1))
        self.play(Create(q2))
        self.wait(7)
        self.play(Create(pause))
        self.wait(8)
        self.clear()
    def infiniteIterationAnalysisScene(self):
        equationFirst = MathTex(r"\textrm{As number of iterations}\rightarrow \infty, \textrm{ distance (between Achilles and the tortoise)} \rightarrow 0", color = BLUE).scale(0.75).move_to(UP*1.5)
        equationSecond = MathTex(r"\textrm{When the distance is 0, Achilles catches up to the tortoise. Thus,}").scale(0.5)
        equationThird = MathTex(r"\textrm{As number of iterations}\rightarrow \infty, \textrm{ Achilles} \rightarrow \textrm{catching the tortoise}", color = YELLOW).scale(0.75).move_to(DOWN*1.5)
        self.play(Write(equationFirst))
        self.wait(8)
        self.clear()
        self.add(equationFirst)
        self.play(Write(equationSecond))
        self.wait(5)
        self.play(Write(equationThird))
        self.wait(8)
        self.play(equationFirst.animate.move_to(UP*2.5), equationSecond.animate.move_to(UP*1.5), equationThird.animate.move_to(UP*0.5))
        equationFourth = Paragraph("We need to prove that an infinite number of","iterations occurs in a finite amount of time.", color = RED, alignment="center").scale(0.75).move_to(DOWN*1.5)
        self.play(Write(equationFourth))
        self.wait(14)
        self.clear()
    def timeValueLimitAnalysisScene(self):
        timeRectangle = Rectangle(width=2.2, height=0.6, color=BLUE, fill_opacity = 0.5).to_edge(UR - 0.25*RIGHT- 0.25*UP)
        s1 = Text('The time keeps increasing, but never reaches 6.', color=BLUE).scale(0.75).move_to(UP*2)
        self.play(Write(s1), Create(timeRectangle))
        self.wait(2)
        self.clear()
        self.add(s1)
        s2 = MathTex(r"\textrm{As number of iterations}\rightarrow \infty, \textrm{ time} \rightarrow 6").scale(0.75).move_to(UP*1)
        self.play(Write(s2))
        self.wait(6)
        s3 = Paragraph('An infinite number of iterations occurs','in a finite amount of time: 6. Thus...', color = YELLOW, alignment="center").scale(0.75)
        self.play(Write(s3))
        self.wait(7)
        s4 = Text('Achilles does catch the tortoise.', color = RED).scale(1.25).move_to(DOWN*2)
        self.play(Write(s4))
        self.wait(6)
        self.clear()
    def zenoArgumentProblemScene(self):
        numberLine = NumberLine(
            x_range=[0, 20, 1],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        )
        self.play(Create(numberLine))
        timeBox = Rectangle(width = 0.5*6, height = 0.4, color=BLUE, fill_opacity = 0.5).move_to(numberLine.n2p(3))
        timeBoxDesc = Text('Points before Achilles and the tortoise converge', color=BLUE).scale(0.4).next_to(timeBox, DOWN, buff=0.5)
        self.play(Create(timeBox),Write(timeBoxDesc))
        self.wait(14)
        self.clear()
        concept = Text('The sum of an infinite number of things can be finite.', color=RED).scale(0.75)
        self.play(Write(concept))
        self.wait(10)
        self.clear()
        #demonstrate the concept of integration using the sum of slices of area under a curve
        axis = Axes(
            x_range=[0, 5],
            y_range=[0, 6],
            tips=False,
        )
        labels = axis.get_axis_labels()
        curve_1 = axis.plot(lambda x: 4 * x - x ** 2, x_range=[0, 4], color=BLUE_C)
        xInterval = 1
        riemann_area = axis.get_riemann_rectangles(curve_1, x_range=[0, 4], dx=xInterval, color=BLUE, fill_opacity=0.5)
        integrationTitle = Text('Integration', color=YELLOW).scale(1).to_edge(UP)
        integrationDesc = Paragraph('The sum of an','infinite number','of slices under','a curve.', color=RED, alignment="right").scale(0.5).to_edge(UR)
        self.play(Create(axis), Create(labels), Create(curve_1), Create(riemann_area), Write(integrationDesc), Write(integrationTitle))
        while xInterval >= 0.02:
            xInterval /=2
            new_riemann_area = axis.get_riemann_rectangles(curve_1, x_range=[0, 4], dx=xInterval, color=BLUE, fill_opacity=0.5)
            self.play(Transform(riemann_area, new_riemann_area), run_time=2)
        self.clear()
    def thankYouScene(self):
        thankYou = Text('Thank you for watching!', color=BLUE).scale(1)
        self.play(Write(thankYou))
        self.wait(8)
        self.clear()

    def construct(self):
      self.titleScene()
      self.zenosParadoxIntroductionScene()
      self.problemIntroductionScene()
      self.problemSimulationScene()
      self.zenoMethodTitleScene()
      self.zenoMethodSimulationScene(iterations = 2, setupWaitTime = 8, crossWaitTime = 2, cycleWaitTime = 5, logArcs = False)
      self.areYouConvincedScene()
      self.zenoMethodSimulationScene(iterations = 6, setupWaitTime = 1, crossWaitTime = 1, cycleWaitTime = 1, logArcs = True)
      self.infiniteIterationAnalysisScene()
      self.zenoMethodSimulationScene(iterations = 8, setupWaitTime = 0.1, crossWaitTime = 0.1, cycleWaitTime = 0.1, logArcs = True, animationTime=0.25)
      self.timeValueLimitAnalysisScene()
      self.zenoArgumentProblemScene()
      self.thankYouScene()