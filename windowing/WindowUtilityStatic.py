## Official Import
import numpy as np
import plotly.graph_objects as go
from plotly.offline import iplot, init_notebook_mode

## Custom Import
from windowing.WindowUtility import WindowUtility


#%% Class
class WindowUtilityStatic(object):
    @staticmethod
    def quick_window(data:np.ndarray, seeds:list, window_size_row:int=5, window_size_column:int = 5)->dict:
        with WindowUtility(data, seeds) as engine:
            return engine.setup_windows(window_size_row, window_size_column)
    
    @staticmethod
    def multi_window(data:dict, seeds:list, window_size_row:int=5, window_size_column:int = 5)->dict:
        windowed_data = {}
        for key in data:
            with WindowUtility(data[key], seeds) as engine:
                windowed_data[key] = engine.setup_windows(window_size_row, window_size_column)
        return windowed_data
    
    @staticmethod
    def quick_winMax(data:np.ndarray, seeds:list, window_size_row:int=5, window_size_column:int = 5)->dict:
        with WindowUtility(data, seeds) as engine:
            windowed_data = engine.setup_windows(window_size_row, window_size_column)
            win_argmax = engine.get_window_argmax(windowed_data)
            try:
                assert np.all([(window_size_row, window_size_column) == win_argmax[seed] for seed in seeds])
            except AssertionError:
                print("Window size and argmax do not match.\nThus, the max is not in the center of the window.\nPlease check the window size and seeds.")
            return win_argmax
        
    @staticmethod
    def plot_window(data:dict, seed:tuple, window_size_row:int=5, window_size_column:int = 5, figsize:tuple=(800,800), alpha:float = 0.70, is_notebook: bool = True):
        if is_notebook:
            init_notebook_mode()
        # Get the data to plot
        plot_data = []
        for key in data:
            with WindowUtility(data[key], [seed]) as engine:
                plot_data.append(engine.setup_windows(window_size_row, window_size_column)[seed])    
                    
        plot_data = [go.Surface(z = data, opacity=alpha, colorscale=cmap, showscale=False) for data, cmap in zip(plot_data, ["Reds", "Greens", "Blues", "Oranges", "Purples", "Greys", "YlOrBr", "YlOrRd", "Bluered", "RdBu", "Reds", "Blues", "Greens", "YlGnBu", "YlGn"])]
        
        # Create the figure
        fig = go.Figure(data=plot_data)
        
        fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                  highlightcolor="black", project_z=True))

        fig.update_layout(title='Surface Comaparison', autosize=False,
                        scene_camera_eye=dict(x=1.87, y=0.88, z=-0.64),
                        width=figsize[0], height=figsize[1],
                        margin=dict(l=65, r=50, b=65, t=90)
                        )  
        
        return iplot(fig)