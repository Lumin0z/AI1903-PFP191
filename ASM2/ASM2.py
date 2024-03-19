def display_menu():
    print("===========================================")
    print("1. Nhap thong tin cua n cuon sach cua FU")
    print("2. In ra man hinh thong tin vua nhap")
    print("3. Sap xep thong tin giam dan theo nam xuat ban va hien thi")
    print("4. Tim kiem theo ten sach")
    print("5. Tim kiem theo ten tac gia")
    print("6. Thoat")
    print("===========================================")

def enter_book_info(n):
    import glob
    file_path = glob.glob('FU*.txt')[0]
    with open(file_path, "w") as file:
        file.write(str(n) + "\n")
        for i in range(n):
            Ten_sach = input("Nhap ten sach {}: ".format(i+1))
            Ten_tac_gia = input("Nhap ten tac gia cuon sach {}: ".format(i+1))
            Nha_xuat_ban = input("Nhap tne nha xuat ban{}:".format(i+1))
            Nam_xuat_ban = input("nhap nam xuat ban sach{}: ".format(i+1))
            Gia = input("nhap gia tien sach {}: ".format(i+1))
            file.write(Ten_sach+"\n")
            file.write(Ten_tac_gia+ "\n")
            file.write(Nha_xuat_ban+ "\n")
            file.write(Nam_xuat_ban+ "\n")
            file.write(Gia+ "\n")
            file.write("\n")

def display_entered_info():
    import glob
    file_path = glob.glob('FU*.txt')[0]
    with open(file_path, "r") as file:
        lines = file.readlines()
        tong_so_sach = int(lines[0])
        print("Tong so cuon sach: {}".format(tong_so_sach))
        print("Thong tin sach:")
        print("{:<30} {:<30} {:<10} {:<10}".format("Ten sach", "Ten tac gia", "Nam xuat ban", "Gia"))
        for i in range(1, len(lines),6):
            Ten_sach = lines[i].strip()
            Ten_tac_gia = lines[i+1].strip()
            Nam_xuat_ban = lines[i+3].strip()
            Gia = lines[i+4].strip()
            print("{:<30} {:<30} {:<10} {:<10}".format(Ten_sach, Ten_tac_gia, Nam_xuat_ban, Gia))

import os
def sort_info_by_year():
    import glob
    file_path = glob.glob('FU*.txt')[0]
    with open(file_path, "r") as file:
        lines = file.readlines()
        tong_so_sach = int(lines[0])
        books = []
        for i in range(1, len(lines), 6):
            Ten_sach = lines[i].strip()
            Ten_tac_gia = lines[i+1].strip()
            Nam_xuat_ban = int(lines[i+3].strip())
            Gia = float(lines[i+4].strip())
            books.append((Ten_sach, Ten_tac_gia, Nam_xuat_ban, Gia))
        sorted_books = sorted(books, key=lambda x: (x[2], x[3]), reverse=True)
     
        with open(file_path, "w") as sorted_file:
            sorted_file.write(str(tong_so_sach)+"\n")
        for i in range(1, 6):  
            for book in sorted_books:
                sorted_file.write(book[i])
                sorted_file.write("\n")
                sorted_file.write(book[i+1])
                sorted_file.write("\n")
                sorted_file.write(book[i+2])
                sorted_file.write("\n")
                sorted_file.write(str(book[i+3]))
                sorted_file.write("\n")
                sorted_file.write(str(book[i+4]))
                sorted_file.write("\n")
        print("Tong so cuon sach: {}".format(tong_so_sach))
        print("Thong tin sach:")
        print("{:<30} {:<30} {:<10} {:<10}".format("Ten sach", "Ten tac gia", "Nam xuat ban", "Gia"))
        for book in sorted_books and i in range(1, 6):
            print("{:<30} {:<30} {:<10} {:<10}".format(book[i], book[i+1], book[i+3], book[i+4]))

        def rename_file(old_name, new_name):
           os.rename(old_name, new_name)
         
        old_file_name = "FU.txt"
        new_file_name = "FU2024.txt"
        rename_file(old_file_name, new_file_name)

def search_by_title(title):
    found = False
    import glob
    file_path = glob.glob('FU*.txt')[0]
    with open(file_path, "r") as file:
        lines = file.readlines()
        for i in range(1, len(lines), 6):
            Ten_sach = lines[i].strip()
            Ten_tac_gia = lines[i+1].strip()
            Nha_xuat_ban = lines[i+2].strip()
            if Ten_sach == title:
                found = True
                print("{},{},{}".format(Ten_sach, Ten_tac_gia, Nha_xuat_ban))
    if not found:
        print("Khong tim thay cuon sach nao.")

def search_by_author(author):
    count = 0
    import glob
    file_path = glob.glob('FU*.txt')[0]
    with open(file_path, "r") as file:
        lines = file.readlines()
        for i in range(1, len(lines), 6):
            Ten_sach = lines[i].strip()
            Ten_tac_gia = lines[i+1].strip()
            
            if Ten_tac_gia == author:
                count += 1
                print("{},{},{}".format(Ten_tac_gia, Ten_sach, count))
    if count == 0:
        print("Khong tim thay tac gia.")

def exit_program():
    print("Exiting the program...")
    import glob
    file_path = glob.glob('FU*.txt')[0]
    f = open(file_path, "r")
    f.close()

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            n = int(input("Nhap so luong cuon sach muon nhap: "))
            enter_book_info(n)
        elif choice == "2":
            display_entered_info()
        elif choice == "3":
            sort_info_by_year()
        elif choice == "4":
            title = input("Nhap ten sach muon tim: ")
            search_by_title(title)
        elif choice == "5":
            author = input("Nhap ten tac gia muon tim: ")
            search_by_author(author)
        elif choice == "6":
            exit_program()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
