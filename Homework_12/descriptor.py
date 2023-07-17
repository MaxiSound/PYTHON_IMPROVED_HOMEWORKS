from werkzeug.routing import ValidationError


class Descriptor_name:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, student):
        list_symbol = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                       '&', '*', '(', ')', '+', '}', '{', ']', '@', '!', '^', '%', ']', '}']
        if student[0].islower():
            raise ValidationError('Текст не должен начинаться с маленькой буквы')
        if not isinstance(student, str):
            raise ValidationError('В тексте должны быть только строчные символы')
        for i in student:
            for j in list_symbol:
                if i == j:
                    raise ValidationError('В тексте должны быть только строчные символы')

# class Descriptor_estimation:
#
#     def __set_name__(self, owner, name):
#         self.param_estimation = '_' + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.param_estimation)
#
#     def __set__(self, instance, value):
#         self.validate(value)
#         setattr(instance, self.param_estimation, value)
#
#     def __delete__(self, instance):
#         raise AttributeError(f'Свойство "{self.param_estimation}" нельзя удалять')
#
#     def validate(self, student):
