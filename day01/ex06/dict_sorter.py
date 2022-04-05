#!/usr/bin/env python3

list_of_tuples = [
('Russia', '25'),
('France', '132'),
('Germany', '132'),
('Spain', '178'),
('Italy', '162'),
('Portugal', '17'),
('Finland', '3'),
('Hungary', '2'),
('The Netherlands', '28'),
('The USA', '610'),
('The United Kingdom', '95'),
('China', '83'),
('Iran', '76'),
('Turkey', '65'),
('Belgium', '34'),
('Canada', '28'),
('Switzerland', '26'),
('Brazil', '25'),
('Austria', '14'),
('Israel', '12')
]

dict_to_sort = dict(list_of_tuples)

def get_num(country):
    return int(dict_to_sort[country])


if __name__ == '__main__':
    
    countries = list(dict_to_sort.keys())
    countries.sort(key=lambda x: (-get_num(x), x))
    print(*countries, sep='\n')