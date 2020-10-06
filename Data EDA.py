import pandas as pd
titanic=pd.read_csv('titanic.csv')
print(titanic.head)

#Data EDA in two lines of code using pandas_profiling
import pandas_profiling as pp

profile = pp.ProfileReport(titanic, explorative=True)
profile.to_file('output.html')

#EDA using Sweetviz

import sweetviz as sv
sweet_report=sv.analyze(titanic)
sweet_report.show_html('sweet_report.html')

#EDA using Autoviz

from autoviz.AutoViz_Class import AutoViz_Class
aviz=AutoViz_Class(titanic)


#EDA using dtale
import dtale
dtale.show(titanic, ignore_duplicate=True)