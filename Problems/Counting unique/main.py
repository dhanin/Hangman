# The following code is needed for us to check your answer, do not modify it, please.
students = json.loads(input())
Belov = students['Belov']
Smith = students['Smith']
Sarada = students['Sarada']
my_set = set(Belov)
my_set.update(Smith)
my_set.update(Sarada)
print(len(my_set))