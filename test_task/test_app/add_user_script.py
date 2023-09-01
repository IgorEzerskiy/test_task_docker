from models import User

USER_CREDENTIALS = {'first_user': {'first_name': 'Elena',
                                   'last_name': 'Tihonova',
                                   'probation': 3.5,
                                   'position': 'Trainee Python Dev',
                                   'username': 'emp1'},
                    'second_user': {'first_name': 'Irina',
                                    'last_name': 'Tihonova',
                                    'probation': 3.5,
                                    'position': 'Junior Python Dev',
                                    'username': 'emp2'},
                    'third_user': {'first_name': 'Oleg',
                                   'last_name': 'Tihonov',
                                   'probation': 3.5,
                                   'position': 'Senior Python Dev',
                                   'username': 'emp3'},
                    }

for key in USER_CREDENTIALS:
    User.objects.create_user(
        username=USER_CREDENTIALS[key]['username'],
        first_name=USER_CREDENTIALS[key]['first_name'],
        last_name=USER_CREDENTIALS[key]['last_name'],
        probation=USER_CREDENTIALS[key]['probation'],
        position=USER_CREDENTIALS[key]['position'],
        password='111'
    )
