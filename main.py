import sys
import requests
import json


def check_email(email_address, api_key, output_file_good, output_file_bad):
    URL_email = f"https://emailverification.whoisxmlapi.com/api/v2?apiKey={api_key}&emailAddress={email_address}"

    r = requests.get(URL_email)

    # print(r.text)

    content_json = json.loads(r.text)

    try:
        print("#" * 10)
        email_address_out = content_json["emailAddress"]
        print("Email address: " + email_address_out)
        # print("Format: " + str(content_json["formatCheck"]))
        # print("DNS: " + str(content_json["dnsCheck"]))
        existing = content_json["smtpCheck"]
        print("SMTP: " + str(existing))
        print(existing)
        print(type(existing))
        if existing == "true":
            file_appender(output_file_good, email_address_out + "\n")
        else:
            file_appender(output_file_bad, email_address_out + "\n")
        print("Catch all: " + str(content_json["catchAllCheck"]))
        print("Disposable: " + str(content_json["disposableCheck"]))
        print("Free: " + str(content_json["freeCheck"]))
        print("\n")
    except Exception as x:
        print(x)


def file_reader(path):
    f = open(path, "r")
    return f.read()


def file_appender(path, content):
    f = open(path, "a")
    f.write(content)


# main

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Not enough arguments")
        print("Usage: python3 main.py APIKEY")
        sys.exit()

    api_key_ = sys.argv[1]

    file_to_read_path = "emails_to_search.txt"

    file_to_write_path_good = "emails_found.txt"

    file_to_write_path_bad = "emails_not_good.txt"

    email_list = []

    file_to_read_content = ""

    try:
        file_to_read_content = file_reader(file_to_read_path)
    except Exception as e:
        print(e)

    for one_email in file_to_read_content.split("\n"):
        email_list.append(one_email)

    for e in email_list:
        check_email(e, api_key_, file_to_write_path_good, file_to_write_path_bad)

