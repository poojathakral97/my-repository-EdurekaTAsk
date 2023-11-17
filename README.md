# my-repository-EdurekaTAsk
1. git clone https://github.com/poojathakral97 my-repository-EdurekaTAsk.git
2. cd my-repository-EdurekaTAsk
3. python parse_swagger.py //run
4. git checkout -b feature/swagger-endpoints //new branch created
5. git add parse_swagger.py//add files
6. git commit -m "Add script to parse Swagger endpoints"
7. git push origin feature/swagger-endpoints
8. git checkout -b feature/new-branch//one more branch created
9. git pull origin feature/new-branch
10. git tag -a release-1.1 -m "Release 1.1"
11. git push origin release-1.1
12. git tag -a release-1.2 -m "Release 1.2"
13. git push origin release-1.2//Change in file and create a new tag release 1.2 and push to remote:
14. git tag -l//List all tags:
15. git push --delete origin release-1.1//Delete release 1.1 from remote:
16. git tag -d release-1.1 //Delete release 1.1 from local:

