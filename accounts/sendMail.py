from django.core.mail import send_mail


def sendmail(to, admin_id, password):
    result = send_mail("Credential for admin of this PG.",
                       f"Welcome To PG Manager,\nadminId - {admin_id}\npassword - {password}\nThank you for choosing us.\nRegards\nPayroll Manager",
                       "pgmanager@gmail.com",
                       [to],)
    if result > 0:
        return True
    else:
        return False