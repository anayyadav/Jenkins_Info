# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 19:09:17 2018

@author: anayl
"""

import jenkins
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
for x in range(len(jenkins_job_items)):
    last_build_number = server.get_job_info(jenkins_job_items[x][0])['lastCompletedBuild']['number']
    #print(last_build_number)
    for i in range(1,last_build_number+1):
        build_info = server.get_build_info(jenkins_job_items[x][0], i)
        print (build_info)





