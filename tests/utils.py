class DfWrap:
    """
    A wrapper class for a pandas DataFrame that provides custom functionality, 
    such as comparing equality with another DataFrame.
    """
    
    def __init__(self, df):
        """
        Initializes the DfWrap instance with a pandas DataFrame.

        Parameters:
        df (pd.DataFrame): The DataFrame to wrap.
        """
        self.df = df

    def __eq__(self, df2):
        """
        Checks if the wrapped DataFrame is equal to another DataFrame.

        Parameters:
        df2 (pd.DataFrame): The DataFrame to compare with the wrapped DataFrame.

        Returns:
        bool: True if the two DataFrames are equal, False otherwise.
        """
        return all(self.df == df2)