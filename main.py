import apps.views.cli as cli
import time
from apps.models.database import TaskManager

def main():
    task_manager = TaskManager()
    
    choice = int(input('Nhập lựa chọn: '))    
    match choice:
        # Thêm công việc mới
        case 1:
            task_manager.add_values()   
            pass
        #Xem danh sách công việc
        case 2:
            task_manager.search_tasks()
            pass
        # Sửa công việc
        case 3:
            task_manager.update_value()
            pass
        #Xóa công việc
        case 4:
            task_manager.remove_values()
            pass
        #Đánh dấu hoàn thành
        case 5:
            task_manager.mark_completed()
            pass
        #Tìm kiếm công việc 
        case 6:
            task_manager.search_tasks()
            pass
        #Sắp xếp công việc
        case 7:
            
            pass
        #Thoát
        case 8:
            print('Thank you for using our service!')
            time.sleep(2)
            exit()

if __name__ == '__main__':
    main()