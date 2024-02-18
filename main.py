import model
import database

def main():
    user1 = model.UserData(1, "lanns")
    database.post_UserData(user1)
    res1 = database.get_UserData_by_id(1)
    print(res1)

if __name__ == "__main__":
    main()