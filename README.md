## Requisites
Below steps has been accomplished thru Openrefine (Cleaning to exporting), OSM_conflator tool and audit online tool.


## Getting source dataset
Visit https://dati.comune.milano.it/dataset/ds634-numeri-civici-coordinate and load CSV version in Openrefine

## Cleaning dataset
In Openrefine, apply file "operations"

## Exporting
In Openrefine, "export templating"

#### Subset
Dataset features 60.000+ nodes, so you can define subsets thru Openrefine facet on MUNICIPIO field

## Conflation
conflate -i <Openrefine exported>.json -v -c preview_test.json -o test.osm profile-py

## Audit
Sample audit for subset "MUNICIPIO 5"
http://audit.osmz.ru/project/MI-M5/

## Other resources
#### OSM addresses query
Please, use http://overpass-turbo.eu/s/Ufx as reference, changing Municipio <number> accoprdingly,
then wget using Export "raw data directly from Overpass API" URL
  
#### OSM highway names query
To identify potential unmaches between addr and street
http://overpass-turbo.eu/s/Dc1
wget -O OSM-MiHighWayNames.csv "http://overpass-api.de/api/interpreter?data=%5Bout%3Acsv%28%22name%22%29%5D%3Barea%5B%22name%22%3D%22Milano%22%5D%2D%3E%2Ea%3B%28way%5B%22highway%22%5D%28area%2Ea%29
%3B%29%3Bout%3B%0A"

