

# 学生类
class Student:
    def __init__(self,student_id,name,age,gender):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"学号: {self.student_id}, 姓名: {self.name}, 年龄: {self.age}, 性别: {self.gender}"
    
    def add_student(self,student_list):
        for student in student_list:
            if student.student_id == self.student_id:
                print(f"学号{self.student_id}已经存在")
                return
        student_list.append(self)
        print(f"学生{self.name}添加成功")

    def delete_student(self,student_list):
        for student in student_list:
            if student.student_id == self.student_id:
                student_list.remove(student)
                print(f"学号为 {self.student_id} 的学生已被删除！")
                return
        print(f"未找到学号为 {self.student_id} 的学生！")

    def update_student(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print(f"学号为 {self.student_id} 的学生信息已修改！")

    def search_student(self, student_list):
        for student in student_list:
            if student.student_id == self.student_id:
                print(student)
                return
        print(f"未找到学号为 {self.student_id} 的学生！")

    @staticmethod
    def display_students(student_list):
        if len(student_list) == 0:
            print("没有学生信息！")
        else:
            for student in student_list:
                print(student)
    
    @staticmethod
    def exit_system():
        print("退出学生管理系统。")
        exit()



class StudentManager:
    def __init__(self):
        self.students = []

    def run(self):
        while True:
            print("\n欢迎使用学生管理系统")
            print("1. 添加学生信息")
            print("2. 删除学生信息")
            print("3. 修改学生信息")
            print("4. 查询学生信息")
            print("5. 显示所有学生信息")
            print("6. 退出系统")
            choice = input("请输入您的选择: ")
            
            if choice == '1':
                student_id = input("请输入学号: ")
                name = input("请输入姓名: ")
                age = input("请输入年龄: ")
                gender = input("请输入性别: ")
                student = Student(student_id, name, age, gender)
                student.add_student(self.students)
            elif choice == '2':
                student_id = input("请输入要删除的学号: ")
                student = Student(student_id, "", "", "")
                student.delete_student(self.students)
            elif choice == '3':
                student_id = input("请输入要修改的学号: ")
                name = input("请输入新的姓名: ")
                age = input("请输入新的年龄: ")
                gender = input("请输入新的性别: ")
                student = Student(student_id, "", "", "")
                student.update_student(name, age, gender)
            elif choice == '4':
                student_id = input("请输入要查询的学号: ")
                student = Student(student_id, "", "", "")
                student.search_student(self.students)
            elif choice == '5':
                Student.display_students(self.students)
            elif choice == '6':
                Student.exit_system()
            else:
                print("无效的输入，请重新选择。")


if __name__ == "__main__":
    manager = StudentManager()
    manager.run()