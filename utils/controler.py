def gets_user_info(users_data: list) -> None:
    for user in users_data:
        print(f'Twój znajomy {user['name']} z miejscowości {user['location']} opublikował {user["posts"]} postów.')

def add_user(users_data:list)->None:
    new_name:str=input('Podaj imię nowego znajomka: ')
    new_localization:str=input('Podaj miejsce zamieszkania: ')
    new_posts:str=input('Podaj liczbę postów znajomego: ')
    users_data.append({'name': new_name, 'location': new_localization, 'posts': new_posts})
