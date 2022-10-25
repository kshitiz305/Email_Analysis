import imaplib
import email
import yaml
import pandas as pd



def get_credentials():
    global user, password
    with open('credentials.yaml') as f:
        content = f.read()
    my_credentials = yaml.load(content, Loader=yaml.FullLoader)
    user, password = my_credentials['user'], my_credentials['password']
    return user, password

user, password = get_credentials()


def initial_setters(user, password):

    imap_url = 'outlook.office365.com'  # 'imap.gmail.com'
    my_mail = imaplib.IMAP4_SSL(imap_url)
    my_mail.login(user, password)
    my_mail.select('Inbox')
    data = my_mail.search(None, 'ALL')
    mail_ids = data[1]
    id_list = mail_ids[0].split()
    # This should be equal to the total number of emails you have seen above
    first_email_id = int(id_list[0])
    latest_email_id = int(id_list[-1])
    return my_mail, data, id_list, first_email_id

def data_extarctor(my_mail, data, id_list, first_email_id,email_df):

    for i in range(first_email_id, len(id_list), 1):
        try:
            data = my_mail.fetch(str(i), '(RFC822)')
        except:
            print(f"Error in {i}")
            continue

        for response_part in data:
            arr = response_part[0]
            if isinstance(arr, tuple):
                msg = email.message_from_string(str(arr[1], 'ISO-8859–1'))
                # print(i)  # This will let you know what row is being appended
                new_row = pd.Series({"Date": msg['Date'], "From": msg['from'], "Subject": msg['subject'],
                                     "Status": msg['X-Antivirus-Status']})
                email_df = email_df.append(new_row, ignore_index=True)
    return email_df


def main():
    my_mail, data, id_list, first_email_id = initial_setters(user, password)
    email_df = pd.DataFrame(columns=['Date', 'From', 'Subject', 'Status'])
    email_df = data_extarctor(my_mail, data, id_list, first_email_id,email_df)
    analysis_data = email_df.groupby("From").count().sort_values("Date")




if __name__ == '__main__':
    main()
