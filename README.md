highway names query
http://overpass-turbo.eu/s/Dc1
wget -O MiHighWayNames.csv "http://overpass-api.de/api/interpreter?data=%5Bout%3Acsv%28%22name%22%29%5D%3Barea%5B%22name%22%3D%22Milano%22%5D%2D%3E%2Ea%3B%28way%5B%22highway%22%5D%28area%2Ea%29%3B%29%3Bout%3B%0A"

replacing decimal separator:
sed -i  -e 's/,/./g' ds634_civici_coordinategeografiche_20181001.csv 

cut or reduce reduntant data:
cat ds634_civici_coordinategeografiche_20181001.csv  | awk -F ";"  '{ printf("%s;%s;%s;%2.5f;%2.6f\n",$1,$3,$4,$15,$16) }' > short_ds634



### ALTERNATIVE

wget https://geoportale.comune.milano.it/Download/area_download/SIT/Toponomastica/OpenData_Civici.zip
