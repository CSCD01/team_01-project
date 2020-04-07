import numpy as np
import pandas as pd


def header(msg):
    print('-' * 50)
    print('[' + msg + ']')


# COMMAND RUN FROM INSIDE PROJECT FOLDER: python -u "demoTest.py"

################################################### UNNAMED INDEX QUERY #######################################################

udata =  range(11, 20)
uindex = range(1, 10)
series = pd.Series(udata, index=uindex)

header('Series with unnamed index:')
print('>>> print(series)')
print(series)
# 1    11
# 2    12
# 3    13
# 4    14
# 5    15
# 6    16
# 7    17
# 8    18
# 9    19
# dtype: int64

header('Query series using keyword for series\' index, "index":')
print(">>> series.query('index < 5')")
print(series.query('index < 5'))
# 1    11
# 2    12
# 3    13
# 4    14
# dtype: int64

header('Query series using python as opposed to numexpr:')
print(">>> series.query('index > 5', False, engine='python')")
print(series.query('index > 5', False, engine='python')) # Pass kwargs as 3rd arg
# 6    16
# 7    17
# 8    18
# 9    19
# dtype: int64

header('Query series inplace, mutating the original series:')
print(">>> series.query('index != 1', True)")
series.query('index != 1', True) # inplace=True so Series is mutated
print(series)
# 2    12
# 3    13
# 4    14
# 5    15
# 6    16
# 7    17
# 8    18
# 9    19
# dtype: int64

header('Query series outside of index for an empty series:')
print(">>> series.query('index < 0')")
series.query('index < 0')
print(series)
# 2    12
# 3    13
# 4    14
# 5    15
# 6    16
# 7    17
# 8    18
# 9    19
# dtype: int64

header('Query series inplace using keyword for unnamed index at level 0, "ilevel_0":')
print(">>> series.query('ilevel_0 == 5', True)")
series.query('ilevel_0 == 5', True) # inplace=True so Series is mutated
print(series)
# 5    15
# dtype: int64

################################################### UNNAMED INDEX EVAL ########################################################

header('High level eval on series:')
print(">>> pd.eval('series + series')")
print(pd.eval('series + series'))
# 5    30
# dtype: int64

header('Series level eval on index:')
print(">>> series.eval('index == 5')")
print(series.eval('index == 5'))
# 5    True
# dtype: bool

################################################### NAMED MULTIINDEX QUERY ####################################################

years = range(2002, 2018)
fields = range(1, 5)
mdata = range(1, 65)
mindex = pd.MultiIndex.from_product([years, fields], names=['year', 'field'])
series_a = pd.Series(data=mdata, index=mindex)

header('Series with MultiIndex:')
print('>>> print(series)')
print(series_a)
# year  field
# 2002  1         1
#       2         2
#       3         3
#       4         4
# 2003  1         5
#                ..
# 2016  4        60
# 2017  1        61
#       2        62
#       3        63
#       4        64
# Length: 64, dtype: int64

header("Querying using named indexes in a Series with MultiIndex")
print(">>> series.query(year != 2010 & field == 3)")
print(series_a.query('year != 2010 & field == 3'))
# year  field
# 2002  3         3
# 2003  3         7
# 2004  3        11
# 2005  3        15
# 2006  3        19
# 2007  3        23
# 2008  3        27
# 2009  3        31
# 2011  3        39
# 2012  3        43
# 2013  3        47
# 2014  3        51
# 2015  3        55
# 2016  3        59
# 2017  3        63
# dtype: int64

header("Querying using keyword 'and' instead of '&'")
print(">>> series.query(year != 2010 and field == 3)")
print(series_a.query('year != 2010 and field == 3'))
# year  field
# 2002  3         3
# 2003  3         7
# 2004  3        11
# 2005  3        15
# 2006  3        19
# 2007  3        23
# 2008  3        27
# 2009  3        31
# 2011  3        39
# 2012  3        43
# 2013  3        47
# 2014  3        51
# 2015  3        55
# 2016  3        59
# 2017  3        63
# dtype: int64

################################################### NAMED MULTIINDEX EVAL #####################################################

header('Series level eval on MultiIndex:')
print(">>> series.eval('year != 2010 and field == 3')")
print(series_a.eval('year != 2010 and field == 3'))
# year  field
# 2002  1        False
#       2        False
#       3         True
#       4        False
# 2003  1        False
#                ...
# 2016  4        False
# 2017  1        False
#       2        False
#       3         True
#       4        False
# Length: 64, dtype: bool

eyears = range(2002, 2005)
efields = range(1, 3)
edata = range(1, 7)
eindex = pd.MultiIndex.from_product([eyears, efields], names=['year', 'field'])
series_b = pd.Series(data=edata, index=eindex)

header('Another Series with MultiIndex:')
print('>>> print(series_b)')
print(series_a)
# year  field
# 2002  1         1
#       2         2
#       3         3
#       4         4
# 2003  1         5
#                ..
# 2016  4        60
# 2017  1        61
#       2        62
#       3        63
#       4        64
# Length: 64, dtype: int64

header('High level eval on comparable series:')
print(">>> pd.eval('series_A + series_b')")
print(pd.eval('series_a + series_b'))
# year  field
# 2002  1        2.0
#       2        4.0
#       3        NaN
#       4        NaN
# 2003  1        8.0
#               ...
# 2016  4        NaN
# 2017  1        NaN
#       2        NaN
#       3        NaN
#       4        NaN
# Length: 64, dtype: float64

################################################### ERROR HANDLING ############################################################

header("KeyError when index is not recognized in query or eval")
print(">>> series.query(reay != 2010)")
print(series_a.query('reay != 2010'))
# Traceback (most recent call last):
#   File "c:\Users\seemi\Documents\Desktop\School\Uni\Semester-8-W20\CSCD01\Project\pandas\pandas\core\computation\scope.py", line 188, in resolve
#     return self.resolvers[key]
#     ...
# KeyError: 'reay'
print(">>> series.eval(reay != 2010)")
print(series_a.eval('reay != 2010'))
# During handling of the above exception, another exception occurred:
# Traceback (most recent call last):
#   File "c:\Users\seemi\Documents\Desktop\School\Uni\Semester-8-W20\CSCD01\Project\pandas\pandas\core\computation\scope.py", line 199, in resolve
#     return self.temps[key]
#     ...
# pandas.core.computation.ops.UndefinedVariableError: name 'reay' is not defined


###############################################################################################################################