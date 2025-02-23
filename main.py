import apps.views.cli as cli
import time

def main():
    cli.print_menu()
    try:
        choice = int(input('Nhập lựa chọn: '))    
        match choice:
            # Thêm công việc mới
            case 1:
                pass
            #Xem danh sách công việc
            case 2:
                pass
            # Sửa công việc
            case 3:
                pass
            #Xóa công việc
            case 4:
                pass
            #Đánh dấu hoàn thành
            case 5:
                pass
            #Tìm kiếm công việc
            case 6:
                pass
            #Sắp xếp công việc
            case 7:
                pass
            #Thoát
            case 8:
                print('Thank you for using our service!')
                time.sleep(2)
                exit()
    
    except Exception as e:
        print('Lựa chọn không hợp lệ. Vui lòng nhập lại!')

if __name__ == '__main__':
    main()