from manim import *
import numpy as np

class PhysicsScene(Scene):

        
    def Interference(self):  
        self.v_value = 4.3e14 
        self.lambda_value = 7e-7
        self.d = 1e-5 
        self.D = 1 
        self.I0 = 10
        self.y_values = np.linspace(-0.5, 0.5, 400)
        phi = (2 * np.pi / self.lambda_value) * (self.d * self.y_values / self.D)
        I_net_values = self.I0 * np.cos(phi/2)**2
        return self.y_values, I_net_values
    
    def Diffraction(self):
        self.v_value = 4.3e14 
        self.lambda_value = 7e-7
        self.d = 1e-5 
        self.D = 1 
        self.I0 = 10
        self.y_values = np.linspace(-0.5, 0.5, 400)
        k = 2 * np.pi / self.lambda_value
        beta = (k * self.y_values * self.d / (2 * self.D))  # Fixed calculation
        I_net_values = self.I0 * (np.sin(beta) ** 2) / (beta ** 2 + 1e-9)  # Avoid division by zero
        return self.y_values, I_net_values
    
    def construct(self):  # Manim requires `construct()`, not `Main()`
        axes = Axes( 
            x_range=[-0.008, 0.009, 2], 
            y_range=[-6, 7, 2], 
            x_length=6, 
            y_length=4, 
            axis_config={'include_numbers': True}, 
            x_axis_config={'color': ORANGE}, 
            y_axis_config={'color': ORANGE}
        ) 
        
        x_values, y_values = self.Diffraction()
        graph = axes.plot_line_graph(x_values, y_values, line_color=YELLOW) 
        
        axes_label = axes.get_axis_labels(x_label='y', y_label='I(y)') 
        self.add(axes, graph, axes_label) 
        self.interactive_embed()