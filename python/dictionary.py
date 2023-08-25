#understanding dictionary datatype

#define dictionary od devops tools
devopsTools={
    "1":"Linux",
    "2":"Git",
    "3":"Docker",
    "4":"Kubernetes",
    "5":"Terraform",
    "6":"Ansible",
    "7":"Chef"}

#print the list of options for the user
print("""
DevOps Tools
------------------
1. Linux
2. Git
3. Docker
4. Kubernetes
5. Terraform
6. Ansible
7. Chef
""")

#ask the user to enter a choice
choice=input("Select your favorite DevOps tool from the list ")

#print the favorite devops tool
print(f"\nYour favorite DevOps tool is {devopsTools[choice]}. Good choice!!!")
