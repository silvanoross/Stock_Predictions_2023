# Class to hold helper function code

class Helper:
    
    def __init__(self):
        pass
    
    def prophet_format(self, df):
        """Transform a dataframe into two columns labeled ['ds' 'y'] 
        for use in Prophet timeseries predictions
        index must be a datetime, but will try and reformat regardless
        """
        # imports
        import pandas as pd
        import datetime as dt
        columns = ['ds', 'y']
        prophet_df = df['close']
        prophet_df = prophet_df.reset_index()
        prophet_df.columns = columns
        prophet_df['ds'] = pd.to_datetime(prophet_df['ds'], infer_datetime_format=True)
        prophet_df['ds'] = prophet_df['ds'].dt.tz_localize(None)
        
        return prophet_df
    
    def datetime_converter(self, df, column):
        """Takes a dataframe and transforms the desired column into a datetime object"""
        pass
    
    