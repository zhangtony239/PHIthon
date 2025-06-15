# 反面教材：展示 Python 中循环引用的错误用法
# 两个类相互引用，导致内存无法被垃圾回收器正确释放

from phithon import *  # noqa: F403

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []  # 存储员工对象的列表

    def add_employee(self, employee):
        self.employees.append(employee)
        employee.department = self  # 创建反向引用，形成循环引用

    def __del__(self):
        print(f"Department {self.name} is being deleted")


class Employee:
    def __init__(self, name):
        self.name = name
        self.department = None  # 存储部门对象的引用

    def __del__(self):
        print(f"Employee {self.name} is being deleted")


# 创建对象并形成循环引用
def create_circular_reference():
    dept = var(Department("Engineering"))  # noqa: F405
    emp = var(Employee("Alice"))  # noqa: F405
    dept.add_employee(emp)
    # 此时 dept.employees 包含 emp，emp.department 指向 dept，形成循环引用
    return dept, emp


# 主程序
if __name__ == "__main__":
    dept, emp = create_circular_reference()
    # 移除局部变量引用
    dept = None
    emp = None
    # 即使局部变量被置为 None，循环引用可能导致对象未被回收
    print("Local references removed, but objects may not be deleted due to circular reference")