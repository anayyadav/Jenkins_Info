# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 22:21:19 2018

@author: anayl
"""
import os
os.system("jenkins_bulid_information,py")
import pandas as pd 
import datetime
import time
import csv
data= pd.read_csv("C:\\Users\\anayl\\Desktop\\data\\jenkins.csv")

def name_of_jobs():
    job_names=[]
    temp = data["Job Name"][0]
    job_names.insert(0,temp)
    j = 1
    for i in range(len(data["Job Name"])):
        if(temp != data["Job Name"][i]):
            temp = data["Job Name"][i]
            job_names.insert(j,temp)
            j = j + 1
    return job_names  
        

#total build for each job
def totalNoOfBuildByJobname(job_name):
    return len(data[(data['Job Name'] == job_name)])

def job_vs_total_no_build():
    total_no_of_build=[]
    jobs = name_of_jobs()
    for i in range(len(jobs)):
        total_no_of_build.insert(i,totalNoOfBuildByJobname(jobs[i]))

#build fails for each job for each type
def totalNoOfBuildFailedByJobname(job_name,Result_type):
    return len(data[(data['Job Name'] == job_name) & (data['Result'] == Result_type)])
    
def build_time_by_bID(job_name, bID):
    i = bID
    return datetime.datetime.fromtimestamp(int(data[(data['Buid_no'] == i) & (data['Job Name'] == job_name)]['timestamp'])/1000).strftime('%Y-%m-%d %H:%M:%S')    
 
# latest build
def latest_build_done(job_name):
    latest_build = []
    total_build = totalNoOfBuildByJobname(job_name)
    for i in range(total_build,0,-1):
        #print("Build No : ",i," ",str(data[(data['Buid_no'] == i) & (data['Job Name'] == job_name)]['Result']).split('    ')[1]," ",datetime.datetime.fromtimestamp(int(data[(data['Buid_no'] == i) & (data['Job Name'] == job_name)]['timestamp'])/1000).strftime('%Y-%m-%d %H:%M:%S'))
        latest_build.insert(i,(str(data[(data['Buid_no'] == i) & (data['Job Name'] == job_name)]['Result']).split('    ')[1],datetime.datetime.fromtimestamp(int(data[(data['Buid_no'] == i) & (data['Job Name'] == job_name)]['timestamp'])/1000).strftime('%Y-%m-%d %H:%M:%S')))
    return latest_build_done

def date_diff(st1):
    date_format = "%Y-%m-%d %H:%M:%S"
    ts = time.time()
    st =datetime.datetime.fromtimestamp(ts).strftime(date_format)
    a = datetime.datetime.strptime(st, date_format)
    b = datetime.datetime.strptime(st1, date_format)
    delta = b - a
    return delta.days

def last_two_day_build(job_name):
    no_of_builds = 0
    total_build = totalNoOfBuildByJobname(job_name)
    for i in range(total_build,0,-1):
        build_time = build_time_by_bID(job_name,i)
        if(date_diff(build_time) <= 2 and date_diff(build_time) != 0 ):
            no_of_builds= no_of_builds+1
    return no_of_builds

def todaysNoOfBuild(job_name):
    no_of_builds = 0
    total_build = totalNoOfBuildByJobname(job_name)
    for i in range(total_build,0,-1):
        build_time = datetime.datetime.fromtimestamp(int(data[(data['Buid_no'] == i) & (data['Job Name'] == job_name)]['timestamp'])/1000).strftime('%Y-%m-%d %H:%M:%S')
        if(date_diff(build_time) == 0 ):
            no_of_builds= no_of_builds+1
    return no_of_builds

def main():
    with open("C:\\Users\\anayl\\Desktop\\data\\jenkins_final.csv", "w+") as output:
        writer = csv.writer(output,lineterminator=',')
        header =["project_name","no_of_builds","No_of_success_builds","No_of_failed_builds","No_of_build_done_today","nso_of_build_done_last_2days"]
        for val in header:
            writer.writerow([val])
       
        jobs = name_of_jobs()
        for i in range(len(jobs)):
            writer.writerow("\n") 
            data_set = [jobs[i],totalNoOfBuildByJobname(jobs[i]),totalNoOfBuildFailedByJobname(jobs[i],"SUCCESS"),totalNoOfBuildFailedByJobname(jobs[i],"FAILURE"),todaysNoOfBuild(jobs[i]),last_two_day_build(jobs[i])]
            for val in data_set:
                writer.writerow([val])
              
            
            
if __name__ == "__main__":
    main()
