# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 19:09:17 2018

@author: anaylatiwal
"""

import jenkins
import json
from jenkinsapi.jenkins import Jenkins

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

   
with open("C:\\Users\\anayl\\Desktop\\project\\jenkins.json", "w") as json_file:
    for x in range(len(jenkins_job_items)):
        last_build_number = server.get_job_info(jenkins_job_items[x][0])['lastCompletedBuild']['number']
        #print(last_build_number)
        for i in range(1,last_build_number+1):
            build_info = server.get_build_info(jenkins_job_items[x][0], i)
            json.dump(build_info, json_file, indent=4)
            json_file.write("\n")
            #print (build_info)
            
            
            
