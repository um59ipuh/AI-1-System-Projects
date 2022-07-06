# Assignment 5: Semantic Web

## For running the code
### Prerequisites
> Use at least python version, python 3.7
 
## Required Libraries
> requests, psutil, signal

Install dependencies using pip: `$ pip install {library_name}`

### Steps
1. Go to folder `team02` and Run `zbQuery.py` with specified flag and file.
2. You can select any flags for build, update and run the problem file.


    -b : for building rdf data from xml file, You must provide xml file after this command flag

    -w : for update Blazegraph with rdf data, if -b present with xml file then no need to provide rdf file

    -r : running server with problem xml file and get the result.

2. As example for running with xml file the command would be 
   
   `~:team02 $python zbQuery.py -b {zbXml_data.xml} -w -r {problem_file.xml}`
3. `Solution.xml` will be generated under the `team02` folder contains all results.
