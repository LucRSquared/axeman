# Geographic Profiling using Rossmo's Formula: Application of Rossmo's Formula

In the main notebook `geoprofiling.ipynb`, the network of the streets of the city of New-Orleans, LA is pulled using data from OpenStreetMap. Data from the serial murders by the so-called "Axeman of New Orleans" is loaded and plotted on the network.

Rossmo's formula is used to estimate the murderer's "anchor points" (i.e. places on the map with higher probability for it to be where he stayed or used as a "safe" spot). Rossmo's formula uses the manhattan distance. This implementation also allows for an actual traveled distance through the streets to be used.
