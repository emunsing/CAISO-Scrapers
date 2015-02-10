# CAISO LMP Scrapers

In [my work] researching renewable energy and the electricity grid, I regularly use data from the California Indepdent System Operator ([CAISO]), typically accessed through the Open Access Same-Time Information System ([OASIS]). This xml-based API was designed around the needs of generation companies, but not necessarily the needs of the public or researchers.

This repository is a set of tools which I'm developing to help make the electricity system more transparent.  Working with the [Cleanweb] group at UC Berkeley, I'm contributing to a more open and accessible pool of energy data that can help inform business, policy, and personal behavior. Check out the [Electricity Mapper] that I've developed so that you can visualize grid energy data, and if you like it fork the [ElectricityMapper github project].

## Tools:
We have developed a number of tools which scrape data from the [OASIS] API and related documents.  Please [let me know] if there are more that I should link to:
##My Tools:
  - [CAISO Node Location Scraper:] Scrapes geographic location (lat/lon) for Location Marginal Price (LMP) nodes, which are the local hubs where energy is bought and sold

##Other People's Tools:
  - [Cleanweb Berkeley CAISO Scraper:] Tools for scraping  for scraping the real-time and historical LMP data
  - [Pyiso:] An awesome project by our friends at [WattTime]

License
----

MIT

[my work]:http://linkedin.com/in/emunsing
[CAISO]:http://www.caiso.com
[OASIS]:http://oasis.caiso.com
[Electricity Mapper]:http://electricitymapper.appspot.com
[ElectricityMapper github project]:https://github.com/emunsing/ElectricityMapper
[Cleanweb]:http://cleanweb.berkeley.edu
[Cleanweb Berkeley CAISO Scraper:]:https://github.com/cwBerkeley/code
[let me know]:http://www.twitter.com/EcoMunsing
[Pyiso:]:https://github.com/watttime/pyiso
[WattTime]:http://www.watttime.org/
