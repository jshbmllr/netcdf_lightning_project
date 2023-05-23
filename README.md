## Overview
Historically, real-time lightning data has been provided by a few corporate owned lightning detection networks. Access has always been quite expensive. This changed with the launch of GOES-R satellites, each of which includes a [Geostationary Lightning Mapper](https://www.goes-r.gov/spacesegment/glm.html). Additionally, Amazon provides hosting and free access to many public datasets, including GOES-R NetCDF data: https://noaa-goes18.s3.amazonaws.com/index.html#GLM-L2-LCFA/

## The assignment 
Create a program that downloads a specified GLM NetCDF file and decodes the lightning strike data into memory. It should then allow the user to specify geographic bounding boxes. The program should efficiently query all the lightning strikes in the specified bounding box and display them to the user. 

An example execution could look like this:

```
> start.program
Provide a GLM file to download:
> OR_GLM-L2-LCFA_G18_s20231400000000_e20231400000200_c20231400000219.nc

…downloading GLM NetCDF
…decoding GLM NetCDF
…ready

Provide a bounding box (or enter to quit):
> -171,18,-66,71

…found 5 lightning strikes:
	-70,60 @ 2023-05-20T00:02:19.12345
	-71,61 @ 2023-05-20T00:02:19.11111
	-72,62 @ 2023-05-20T00:02:19.22222
	-73,63 @ 2023-05-20T00:02:19.33333
	-74,64 @ 2023-05-20T00:02:19.55555
```

### Consider the following goals:

- The exact format for user input and output is up to you, as long as it decodes the latitude, longitude, and time of each strike
- You are free to use any language and libraries of your choice
  - You are highly encouraged to use a library to decode the NetCDF input
  - If a library exists that specifically decodes GOES GLM lightning data, you are discouraged from using it (as it trivializes the exercise and prevents us from getting an accurate understanding of your skills as a developer.)
  - If you’re unsure, feel free to reach out to the team
- Your code should be optimized for efficient retrieval of lightning strikes within a specified bounding box (assume data will be loaded/decoded once, and then multiple bounding box queries will be made against the decoded dataset.)
  - Do not chose a language based on efficiency: work in a language you are comfortable with and aim for an efficient solution in that language
- Be prepared to talk about your design choices: language and library selection, algorithm selection, etc.

## Submission

You can either fork this repo and e-mail us a link to yours once you are done, or you can zip/tar up and e-mail your source code.

## Notes

Scientific libraries often require supporting binary packages in C or Fortran, and thus most encourage the use of a package manager like [Conda](https://docs.conda.io/en/latest/) to handle the installation. In our work environment we typically use Docker containers to manage the dependencies and keep all of the various packages off of our development systems. Feel free to do so in your work, there are many Docker images available.

While we want to develop a good understanding of your skills as a developer, it is NOT our intent to give you an extremely time consuming assignment. If you find this exercise taking more than a few hours, it is acceptable to turn in a partial solution along with an explanation or pseudocode of the remaining functionality. 

Please reach out with any questions!

## Resources

Some example Python packages that may help you along the way

https://github.com/Unidata/netcdf4-python

https://github.com/SciTools/iris

https://docs.xarray.dev/en/stable/index.html



