import model
import database

def main():
    res1 = database.get_UserData_by_id(2)
    print(res1)

if __name__ == "__main__":
    main()