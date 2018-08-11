# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 19:09:17 2018

@author: anayl
"""

import jenkins
import csv
from jenkinsapi.jenkins import Jenkins

def parseData(build_info):
    new_data = []
    i = 0
    j = 0
    for key,value in build_info.items():
        if (i == 1):
            new_data.insert(j,build_info["actions"][0]['causes'][0]['shortDescription'])
            j = j +1
        elif( i== 6 or i == 7 or i == 9 or i == 10 or i == 14 or i == 15 ):
            new_data.insert(j, value)
            j = j+1
        i = i+1
    return new_data   
        
       
# connecting to the jenkins
server = jenkins.Jenkins('http://localhost:8080', username='anay', password='anay')
jenkins_server = Jenkins('http://localhost:8080', username='anay', password='anay')
# user information
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
# Print all jobs in Jenkins
jenkins_job_items = jenkins_server.items()
# build info

   
with open("C:\\Users\\anay_latiwal\\Desktop\\Jenkins_collector\\jenkins.csv", "w+") as output:
    writer = csv.writer(output, lineterminator=',')
    header =["Cause","Duration","Est. duration","Name","Buid_no","Result","timestamp"]
    for val in header:
        writer.writerow([val])
    for x in range(len(jenkins_job_items)):
        last_build_number = server.get_job_info(jenkins_job_items[x][0])['lastCompletedBuild']['number']
        #print(last_build_number)
        for i in range(1,last_build_number+1):
            build_info = server.get_build_info(jenkins_job_items[x][0], i)
            writer.writerow("\n") 
            for val in parseData(build_info):
                writer.writerow([val])
               
        #print (build_info)
    




