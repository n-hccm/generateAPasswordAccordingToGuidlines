import check_deny_list
import password_generator

if __name__ == '__main__':
    password = password_generator.generate_password()
    print(f"Generated password: {password}")
    if password_generator.check_password(password):
        print("Password is strong.")
    else:
        print("Password is weak.")
    if check_deny_list.check_deny_list(password):
        print("Password is in the deny list.")
    else:
        print("Password is not in the deny list.")
    print("Enjoy your password.")