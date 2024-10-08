"""
INSERT INTO Manufacturer
"""

from yoyo import step

__depends__ = {}

steps = [
    step(''' 
INSERT INTO Manufacturer (title_country, address_of_manufacturer, contact_list) VALUES
('Россия', 'Улан-Удэ, ул Ленина 54б, офис 504', 'www.ichthyonella.ru, info@chthyonella.ru'),
('Китай', 'Room 901, building 2, 1255 north chouzhou road', 'prc.ru'),
('Россия', 'г. Москва, Фридриха Энгельса 56', 'Marvelcosmetics.com'),
('Россия', 'г. Москва, Бульвар Карла-Маркса 34/3', 'www.theact.ru'),
('Россия', 'г. Москва, ул. Сергея Макеева, д. 13', 'www.rexona.ru'),
('Россия', 'Московская обл, г. Протвино, Железнодорожная ул., 14', 'info@aravia-prof.ru, 8-800-777-0312'),
('Россия', 'Санкт-Петербург, Пискарёвский пр., д. 63, корп 6', 'www.estel.pro'),
('Россия', 'г. Новосибирск, ул. Маяковского, д. 78/1', 'www.aromagica.ru'),
('Россия', 'г. Москва, ул. 1-я Фрезерная, д. 2/1', '+7-(495)-120-10-10'),
('Германия', 'GmbH Schneiderstrasse 82, Langenfeld', 'www.voilet.com, +49 2173 2032631')''')
]

