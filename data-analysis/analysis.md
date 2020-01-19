# Data Analysis - Deep Solar Dataset

## Informácie

Dáta pochádzajú [DeepSolar](http://web.stanford.edu/group/deepsolar/home)
projektu. DeepSolar je deep learning framework ktorý analyzuje satelitné dáta
na identifikáciu GPS lokácií a veľkostí solárnych fotovoltalických (PV) panelov.

## Atribúty (výber)

Datová sada obsahuje 169 atribútov. Niektoré atribúty sú:

- **tile_count** - počet obrazových snímkov (dlaždíc) v oblasti riadka
- **tile_count_residential** - počet obrazových snímkov v rezidenčnej oblasti
- **tile_count_nonresidential** - počet obrázskových snímkov v nebytovej oblasti
- **solar_system_count** - počet solárnych panelov vo všetkych dlaždiciach
- **average_household_income** - priemerný príjem na domácnosť
- **county** - okres/kraj
- **state** - štát
- **population** - počet obyvateľov
- **education_\*** - atribúty spojené so stupňom dosiahnutého vzdelania
- **heating_fuel_\*** - atribúty spojené s typom paliva použitého na vykurovanie
- **age_\*** - atribúty spojené s počtom obyvateľov v danej vekovej kategórii
- **lat, lon, elevation** - GPS koordináty
- **frost_days** - denná akumulácia stupňov kedy je priemerná denná teplota
  nižšia než 0 stupňov Celzia
- **daily_solar_radiation** - priemerná radiácia slnka (Kwh/meter štvorcový) za 
  deň
- **heating_degree_days** - počet dní, kedy je priemerná teplota menšia než 18
  stupňov, indikuje, či je nutné vykurovať
- **cooling_degree_days** - počet dní, kedy je priemerná teplota vačšia ako 18
  stupňov
- **wind_speed** - priemerná rýchlosť vetra
- **electricity_price_\*** - atribúty spojené s cenou elektriny (priemer za 5 rokov)