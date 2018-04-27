# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 16:59:49 2018

@author: anay_latiwal
"""

import pandas as pd
df1 = pd.read_csv("C:\\Users\\anay_latiwal\\Desktop\\Jenkins_collector\\jenkins.csv")
my_data = pd.DataFrame(df1,columns=["Cause","Duration","Est. duration","Name","Buid_no","Result","timestamp"])
print (my_data)
#print(pd.to_datetime(my_data["timestamp"],unit ='ns'))




