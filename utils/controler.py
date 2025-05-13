def gets_user_info(users_data: list) -> None:
    for user in users_data:
        print(f'Twój znajomy {user['name']} z miejscowości {user['location']} opublikował {user["posts"]} postów.')

def add_user(users_data:list)->None:
    new_name:str=input('Podaj imię nowego znajomka: ')
    new_localization:str=input('Podaj miejsce zamieszkania: ')
    new_posts:str=input('Podaj liczbę postów znajomego: ')
    users_data.append({'name': new_name, 'location': new_localization, 'posts': new_posts})

def remove_user(users_data: list)->None:
    user_name:str=input('Podaj imię znajomego do usunięcia: ')
    for user in users_data:
        if user['name'] == user_name:
            users_data.remove(user)

def update_user(users_data: list)->None:
    user_name:str=input('Podaj imię znajomego do aktualizacji: ')
    for user in users_data:
        if user['name'] == user_name:
            user['name']=input('Podaj nowe imię znajomego: ')
            user['location']=input('Podaj nową miejscowość: ')
            user['posts']=input('Podaj nową ilość postów: ')

def get_coordinates(city_name:str)->list:
    import requests
    from bs4 import BeautifulSoup
    url=f"https://pl.wikipedia.org/wiki/{city_name}"
    response = requests.get(url).text
    response_html = BeautifulSoup(response, "html.parser")
    longitude = float(response_html.select(".longitude")[1].text.replace(",","."))
    lattitude = float(response_html.select(".latitude")[1].text.replace(",","."))
    print(longitude)
    print(lattitude)
    return [lattitude,longitude]

import folium
def get_map(users_data:list)->None:

    m = folium.Map(location=(52.23, 21.0),zoom_start=6)

    for user in users_data:

        folium.Marker(location=get_coordinates(user['location']),popup='<img src="https://wykop.pl/cdn/c3201142/comment_oAtt6TivPt5N2EipfXCimHEexxG4St6u.jpg"/>').add_to(m)

    m.save("index.html")