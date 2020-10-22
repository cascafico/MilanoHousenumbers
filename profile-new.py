source = 'Comune_di_Milano'

# do not add unique reference IDs to OSM?

# aggiunge tag ref:<dataset_id>=<id del Comune di Milano (IDMASTER)>
# True -> relying only on geometric matching every time
no_dataset_id = True
dataset_id = 'ds634'

overpass_timeout = 300
#query = [('addr:housenumber','.*')] 
#query = [('addr:housenumber','~.*')]  e se lettera e interno non hanno stesso case?
#query = [('addr:street','~.*'),('addr:city','Milano')] non tutti hanno city valorizzato
query = [('addr:street','~.*'),('addr:city','Milano')] 


bbox = True
max_request_boxes = 32


# tags to replace on matched OSM objects
master_tags = ('addr:housenumber', 'addr:street')

# delete_unmatched = True cancellerebbe anche i POI con indirizzo
delete_unmatched = False
tag_unmatched = { 'fixme':'cannot find this addr in input dataset: please check' }


# max_distance = 10 several housenumbers in polygon centriod unmatched... wider distance
max_distance = 10

# max distance to consider dataset duplicates
duplicate_distance = 2
