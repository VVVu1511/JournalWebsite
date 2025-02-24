from apps.models.database import TaskManager


def test():
    test = TaskManager()
    
    test.add_values(1,'Testing','25-2-2025','Undone')
    test.add_values(2,'Solving Math','27-3-2025','Done')
    
    print(test)


if __name__ == '__main__':
    test()
    