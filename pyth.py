def display_menu():
    print("\n=== MENU ===")
    print("1. Thêm phần tử vào danh sách")
    print("2. Xóa phần tử khỏi danh sách")
    print("3. Sắp xếp danh sách")
    print("4. Tìm kiếm phần tử trong danh sách")
    print("5. Hiển thị danh sách")
    print("6. Đếm số lần xuất hiện của phần tử trong danh sách")
    print("7. Đảo ngược danh sách")
    print("8. Xóa toàn bộ danh sách")
    print("9. Hiển thị tổng số phần tử trong danh sách")
    print("10. Áp dụng thực tế: Lập bảng tần suất xuất hiện của phần tử")
    print("11. Áp dụng thực tế: Gom nhóm các phần tử liên tiếp giống nhau")
    print("12. Áp dụng thực tế: Tìm chuỗi con tăng dài nhất trong danh sách số")
    print("13. Áp dụng thực tế: Tìm cặp phần tử có tổng lớn nhất trong danh sách số")
    print("0. Thoát")

def add_element(lst):
    element = input("Nhập phần tử cần thêm: ")
    lst.append(element)
    print(f"Đã thêm {element} vào danh sách.")
    print(f"Danh sách hiện tại: ", lst)

def remove_element(lst):
    element = input("Nhập phần tử cần xóa: ")
    if element in lst:
        lst.remove(element)
        print(f"Đã xóa {element} khỏi danh sách.")
    else:
        print(f"Không tìm thấy {element} trong danh sách.")
    print(f"Danh sách hiện tại: ", lst)

def sort_list(lst):
    print(f"Danh sách hiện tại: ", lst)
    lst.sort()
    print("Danh sách đã được sắp xếp ", lst)

def search_element(lst):
    element = input("Nhập phần tử cần tìm: ")
    if element in lst:
        print(f"Phần tử {element} có trong danh sách tại vị trí {lst.index(element)}.")
    else:
        print(f"Phần tử {element} không có trong danh sách.")

def display_list(lst):
    if lst:
        print("Danh sách hiện tại: ", lst)
    else:
        print("Danh sách đang trống.")

def count_occurrences(lst):
    element = input("Nhập phần tử cần đếm: ")
    count = lst.count(element)
    print(f"Phần tử {element} xuất hiện {count} lần trong danh sách.")

def reverse_list(lst):
    lst.reverse()
    print("Danh sách đã được đảo ngược.")

def clear_list(lst):
    lst.clear()
    print("Danh sách đã được xóa toàn bộ.")

def list_length(lst):
    print(f"Danh sách hiện tại có {len(lst)} phần tử.")

def frequency_table():
    lst = input("Nhập danh sách các phần tử, cách nhau bởi dấu cách: ").split()
    if not lst:
        print("Danh sách trống.")
        return

    freq = []  # Sử dụng list thay vì dict
    unique_items = []  # Lưu danh sách các phần tử đã xuất hiện

    for item in lst:
        if item in unique_items:
            for pair in freq:
                if pair[0] == item:
                    pair[1] += 1
                    break
        else:
            unique_items.append(item)
            freq.append([item, 1])

    print("Bảng tần suất xuất hiện của các phần tử:")
    for item, count in sorted(freq):
        print(f"{item}: {count}")

def group_consecutive():
    lst = input("Nhập danh sách các phần tử, cách nhau bởi dấu cách: ").split()
    if not lst:
        print("Danh sách trống.")
        return

    grouped = []
    current_group = [lst[0]]

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            current_group.append(lst[i])
        else:
            grouped.append(current_group)
            current_group = [lst[i]]

    grouped.append(current_group)

    print("Các nhóm phần tử liên tiếp giống nhau:", grouped)

def longest_increasing_subsequence():
    lst = input("Nhập danh sách các số, cách nhau bởi dấu cách: ").split()
    try:
        lst = [int(i) for i in lst]
    except ValueError:
        print("Vui lòng nhập danh sách số nguyên.")
        return

    if not lst:
        print("Danh sách trống.")
        return

    longest = []
    current = [lst[0]]

    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            current.append(lst[i])
        else:
            if len(current) > len(longest):
                longest = current
            current = [lst[i]]

    if len(current) > len(longest):
        longest = current

    print("Chuỗi con tăng dài nhất là:", longest)

def max_sum_group():
    lst = input("Nhập danh sách các số, cách nhau bởi dấu cách: ").split()
    try:
        lst = [int(i) for i in lst]
    except ValueError:
        print("Vui lòng nhập danh sách số nguyên.")
        return

    if len(lst) < 2:
        print("Danh sách cần có ít nhất hai phần tử.")
        return

    n = int(input("Nhập số lượng phần tử trong nhóm (n): "))
    if n > len(lst):
        print("Số lượng phần tử trong nhóm lớn hơn độ dài danh sách.")
        return

    max_sum = float('-inf')
    max_group = []

    for i in range(len(lst) - n + 1):
        current_group = lst[i:i + n]
        current_sum = sum(current_group)
        if current_sum > max_sum:
            max_sum = current_sum
            max_group = current_group

    print(f"Nhóm {n} phần tử có tổng lớn nhất là: {max_group} với tổng là {max_sum}.")

def main():
    lst = []
    while True:
        display_menu()
        choice = input("Chọn một chức năng (1-13): ")
        if choice == '1':
            add_element(lst)
        elif choice == '2':
            remove_element(lst)
        elif choice == '3':
            sort_list(lst)
        elif choice == '4':
            search_element(lst)
        elif choice == '5':
            display_list(lst)
        elif choice == '6':
            count_occurrences(lst)
        elif choice == '7':
            reverse_list(lst)
        elif choice == '8':
            clear_list(lst)
        elif choice == '9':
            list_length(lst)
        elif choice == '10':
            frequency_table()
        elif choice == '11':
            group_consecutive()
        elif choice == '12':
            longest_increasing_subsequence()
        elif choice == '13':
            max_sum_group()
        elif choice == '0':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()


"""
1 /s
--- Ứng dụng thực tế:
+ Phân tích dữ liệu: Đếm số lần xuất hiện của các phần tử, ví dụ: phân tích từ trong văn bản hoặc sản phẩm trong kho hàng.
+ Thống kê: Sử dụng để xây dựng bảng phân phối tần suất.
2 / 
--- Ứng dụng thực tế:
+ Xử lý chuỗi: Ví dụ: nén chuỗi trong thuật toán nén dữ liệu (run-length encoding).
+ Phân tích dữ liệu thời gian: Tìm các chuỗi dữ liệu liên tiếp có giá trị giống nhau (ví dụ: phát hiện tín hiệu liên tục).
3 / 
--- Ứng dụng thực tế:
+ Tài chính: Tìm chuỗi tăng của giá cổ phiếu hoặc doanh thu.
+ Quản lý dữ liệu: Phân tích xu hướng tăng liên tục trong các dãy số liệu.
4 / 
--- Ứng dụng thực tế:
+ Tối ưu hóa: Chọn hai giá trị tối ưu từ một tập dữ liệu để đạt tổng cao nhất (ví dụ: giá trị sản phẩm kết hợp).
+ Khoa học dữ liệu: Tìm các cặp giá trị đặc biệt trong phân tích dữ liệu.

"""