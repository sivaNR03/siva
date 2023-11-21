class VariableExample:
    # Static variable (Class-level variable)
    static_variable = 0

    def __init__(self, value):
        # Instance variable (Object-level variable)
        self.instance_variable = value

    def increment_variables(self, local_var):
        # Local variable (Method-level variable)
        local_var += 1
        self.instance_variable += 1
        VariableExample.static_variable += 1
        print("Local variable incremented:", local_var)
        print("Instance variable incremented:", self.instance_variable)
        print("Static variable incremented:", VariableExample.static_variable)

def main():
    # Creating two instances of VariableExample class
    obj1 = VariableExample(10)
    obj2 = VariableExample(20)

    # Calling increment_variables method for obj1
    obj1.increment_variables(5)

    # Calling increment_variables method for obj2
    obj2.increment_variables(15)

if __name__ == "__main__":
    main()


