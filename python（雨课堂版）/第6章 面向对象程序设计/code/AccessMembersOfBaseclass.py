# -*- coding:utf-8 -*-
# Filename: AccessMembersOfBaseclass.py
# --------------------
# Function description:
# Show how to access method and data of parent class
# --------------------
# Author: 董付国
# Email: dongfuguo2005@126.com
#--------------------
# Date: 2014-11-27,Updated on 2017-4-4
# --------------------

class Person(object):
    def __init__(self, name = '', age = 20, sex = 'man'):
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)
        
    def setName(self, name):
        assert isinstance(name, str), 'name must be string.'
        self.__name = name
        
    def setAge(self, age):
        assert isinstance(age, int), 'age must be integer.'
        self.__age = age
        
    def setSex(self, sex):
        assert sex in ('man', 'woman'), 'sex must be "man" or "woman"'
        self.__sex = sex
        
    def show(self):
        print('Name:', self.__name)
        print('Age:', self.__age)
        print('Sex:', self.__sex)

class Teacher(Person):
    def __init__(self, name='', age = 30, sex = 'man', department = 'Computer'):
        super(Teacher, self).__init__(name, age, sex)
        # 也可以使用下面的形式对基类数据成员进行初始化
        #Person.__init__(self, name, age, sex)
        self.setDepartment(department)
        
    def setDepartment(self, department):        
        assert isinstance(department, str), 'department must be a string.'
        self.__department = department
        
    def show(self):
        super(Teacher, self).show()
        print('Department:', self.__department)

if __name__ =='__main__':
    print('='*30)
    zhangsan = Person('Zhang San', 19, 'man')
    zhangsan.show()

    print('='*30)
    lisi = Teacher('Li Si',32, 'man', 'Math')
    lisi.show()
    print('='*30)
    lisi.setAge(40)
    lisi.show()
