import json
from pygal.maps.world import World
from pygal.style import RotateStyle, LightColorizedStyle
from country_codes import get_country_code

#wczytanie danych i umieszczenie ich na liście 
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

#utworzenie słownika danych dotyczące populacji
cc_populations = {}
# wyświetlenie populacji poszczegółnych państw w 2010 
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
   
# Podzielenie państw na try grupy wełdug liczebności populacji
cc_pops_1,cc_pops_2, cc_pops_3 = {}, {}, {} 
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 100000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

wm_style = RotateStyle('#336699', base_style = LightColorizedStyle ) # pobiera kolor rgb w systemie szesnastkowym
wm = World(style = wm_style)
wm.force_uri_protocol = 'http'
wm.title = 'Populacja na świecie w 2010 roku (dane dla poszczególnych państw)'
wm.add('0-10 mln', cc_pops_1)
wm.add('10mln - 1mld', cc_pops_2)
wm.add('> 1mld', cc_pops_3)
wm.render_to_file('World_population.svg')