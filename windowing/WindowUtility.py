import numpy as np

## Class to handle the windowing of 2D data
class WindowUtility(object):
    
    data:np.ndarray
    seeds:list
    
    def __init__(self, data:np.ndarray, seeds:list) -> None:
        self.__data = data
        self.__seeds = seeds
            
    # Properties
    @property
    def data(self) -> np.ndarray:
        return self.__data
    @data.setter
    def data(self, data:np.ndarray) -> None:
        self.__data = data
    
    @property
    def seeds(self) -> list:
        return self.__seeds
    @seeds.setter
    def seeds(self, seeds:list) -> None:
        self.__seeds = seeds
    
    # Methods
    def setup_windows(self, window_size_row:int=5, window_size_column:int = 5) -> np.ndarray:
        """Window the data using the seeds and window size."""
        # Get the shape of the data
        shape = (2*window_size_row+1, 2*window_size_column+1)
        # Create new dictionary to hold the windows
        windowed_data = {seed:np.zeros(shape=shape) for seed in self.__seeds}
        # Loop through the seeds
        for seed in self.__seeds:
            # Get the coordinates of the seed
            x, y = seed[0], seed[1]
            # Get the windowed data
            windowed_data[seed] = self.data[x-window_size_row:x+window_size_row+1, y-window_size_column:y+window_size_column+1]
        return windowed_data
    
    def get_window_argmax(self, windowed_data:dict) -> dict:
        """Get the argmax of the windowed data."""
        return {seed:np.unravel_index(np.argmax(window, axis=None), window.shape) for seed, window in windowed_data.items()}
       
    # Helper
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        pass
