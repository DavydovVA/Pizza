# Usage

1. Create in a root directory file custom_settings.py with:

        service_user_email = 'email_of_service'   #use @mail.ru
        service_password_email = 'email_password'
        
        su_email = 'email_of_superuser'
        su_first_name = 'first_name_of_superuser'
        su_last_name = 'last_name_of_superuser'
        su_password = 'password'

2. Change fill_menu command path to the Pizza Images directory in 
        runserver.sh (or remove this command).

3. docker-compose up --build.