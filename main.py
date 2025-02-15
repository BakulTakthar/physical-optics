from manim import *
import numpy as np

class PhysicsScene(Scene):
    def Diffraction(self):
        self.lambda_value = 7e-7
        self.d = 1e-5 
        self.D = 1 
        self.I0 = 10
        self.y_values = np.linspace(-0.008, 0.009, 400)
        k = 2 * np.pi / self.lambda_value
        beta = (k * self.y_values * self.d / (2 * self.D))
        I_net_values = self.I0 * (np.sin(beta) ** 2) / (beta ** 2 + 1e-9)
        return self.y_values, I_net_values

    def construct(self):
        axes = Axes(
            x_range=[-10, 10, 1], 
            y_range=[0, 25, 1],  
            x_length=40, 
            y_length=1, 
            axis_config={'include_numbers': True}, 
            x_axis_config={'color': ORANGE}, 
            y_axis_config={'color': ORANGE}
        )

        x_values, y_values = self.Diffraction()

        # Corrected curve plotting
        curve = axes.plot(
            lambda x: np.interp(x, x_values, y_values),  
            color=BLUE
        )

        axes_label = axes.get_axis_labels(x_label='y', y_label='I(y)') 

        self.add(axes, curve, axes_label)  
        self.wait(2)  # Avoid interactive mode issues
        self.interactive_embed()

if __name__ == "__main__":
    scene = PhysicsScene()
    scene.render()
