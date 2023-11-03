class emp_details():

    def __init__(self,emp_name,emp_id,emp_domain,emp_gmail):
        self.emp_name =emp_name
        self.emp_id = emp_id
        self.emp_domain = emp_domain
        self.emp_gmail = emp_gmail
    def display(self):
        print("EMP_NAME:",self.emp_name)
        print("EMP_ID:",self.emp_id)
        print("EMP_DOMINE:",self.emp_domain)
        print("EMP_GMAIL:",self.emp_gmail)

obj=emp_details("siva","2056","python","siva@marolix")        
obj.display()





