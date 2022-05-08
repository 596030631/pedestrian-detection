import pickle


def cat_all_user():
    with open('users.pkl', 'rb') as f1:
        users = pickle.load(f1)
        for u in users.keys():
            print(f"User << [{u}]  password[{users[u][0]}]")


def delete_user(key):
    print(key)
    with open('users.pkl', 'rb') as f1:
        users = pickle.load(f1)
        user_data = ["",""]
        users[key] = user_data
        pickle.dump(key,f1)


if __name__ == '__main__':
    print("abc")
    # cat_all_user()

    # delete_user('11111111')

    # cat_all_user()
