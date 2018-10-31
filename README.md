## Getting source dataset
wget https://geoportale.comune.milano.it/Download/area_download/SIT/Toponomastica/OpenData_Civici.zip

## Cleaning dataset
Viario_20181001.operations
Civici_20181001.operations

## Linking tables
Civici_20181001.operations

## Exporting
Civici_20181001.export
#### tests
partial areas has been selected thru lat&log numeric facets

## Conflation
conflate -i Civici_20181001-csv-test.txt.json -v  -c preview_test.json -o test.osm profile-py

## Audit
http://audit.osmz.ru/project/MI-addr/

## Other resources
#### OSM highway names query
http://overpass-turbo.eu/s/Dc1
wget -O OSM-MiHighWayNames.csv "http://overpass-api.de/api/interpreter?data=%5Bout%3Acsv%28%22name%22%29%5D%3Barea%5B%22name%22%3D%22Milano%22%5D%2D%3E%2Ea%3B%28way%5B%22highway%22%5D%28area%2Ea%29
%3B%29%3Bout%3B%0A"

