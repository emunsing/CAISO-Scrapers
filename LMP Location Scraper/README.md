# CAISO LMP Location Scraper

Data returned from [OASIS] is given in terms of LMP node codes, representing ~5000 locations in the California grid for which [CAISO] calculates a  price for electricity, which ultimately is paid to the generators by the utilities.

The node codes provided by CAISO are mostly indecipherable, but they provide a [Google Maps visualization] of the current price data, which pipes in node locations from a [node location xml file].  With this location information, it is easier to understand the geographic correlation between prices, and how transmission congestion, weather, and load centers dictate electricity prices.

**This version was built on an [old visualization] that was used through December 2014, but appears to no longer be hosted.  To stay updated, the scraper needs to be adapted to the new visualizer**.  The scraper outputs a .json file that can easily be converted to .csv (included).  This CSV file was published to a [Google Fusion Table] for greater accessibility to the public, and the .json file is used by the [Electricity Mapper] project and its associated [github project].  Check out [Cleanweb] Berkeley for more projects!

Files
-----
- PointMapStripper.py : The [old visualization] included the full set of node information in the html source.  This Python file crawls through a downloaded html file to extract the node name, generation type, latitude, and longitude, and save it to an output file (.json format)
- LMP_Nodes.json : The 2247 nodes for which geographic data is provided, as a .json file for machine reading
- LMP_Nodes.csv : The same data as a .csv for easy manipulation and human reading
- LMPLocations_vs_FullList.xls : A comparison of the ~5000 nodes for which OASIS provides LMP data, and the smaller set of ~2250 nodes for which we have geographic data.  Aggregated Pricing Nodes (APNodes) are included as well.

To Do's:
--------
  - Review/update comments in code
  - Adapt to current [Google Maps visualization] 

Future Developments
------
  - Correlate with the CAISO [Full Network Model documents]
  - Correlate with the Excel database of power plants at [California Energy Almanac], which provides generator information
  - [Let me know] suggestions!


License
----

MIT

[CAISO]:http://www.caiso.com
[OASIS]:http://oasis.caiso.com
[Full Network Model documents]: http://www.caiso.com/market/Pages/NetworkandResourceModeling/Default.aspx
[Google Maps visualization]:http://www.caiso.com/pages/pricemaps.aspx
[node location xml file]:http://wwwmobile.caiso.com/Web.Service.Chart/api/v1/ChartService/GetPriceContourMap
[old visualization]:oasis.caiso.com/mrtu-oasis/lmp/DAM/POINTMap.html
[Google Fusion Table]:https://www.google.com/fusiontables/DataSource?docid=1HKopcS0TQ8UYuNSAqQP6obeMF4rnNXQ3nrSQ40AN
[Electricity Mapper]:http://electricitymapper.appspot.com
[github project]:https://github.com/emunsing/ElectricityMapper
[Cleanweb]:http://cleanweb.berkeley.edu
[let me know]:http://www.twitter.com/EcoMunsing
[California Energy Almanac]:http://www.energyalmanac.ca.gov/powerplants/


