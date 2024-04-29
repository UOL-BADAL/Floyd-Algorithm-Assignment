Floyd-Warshall's Algorithm Assignment 

This project aims to use recursion in Floyd Warshall's algorithm and performning unit,functional and performance experience to compared it with the imperative and itertools implementation.



Before you start:

Ensure that you have installed the necessary packages listed in 'requirements.txt' prior to starting.

Explanation:

The function can be used from the collections of list used to represent the graph (provided by the University of Liverpool)

Graph provided by University of Liverpool 

graph = [[0, 7, INF, 8] ,[INF, 0, 5, INF],[INF, INF, 0, 2],[INF, INF, INF, 0]]

Definitions: 

INF - Represents the infinite distance i.e the edges that don't exist.

 0  - Represents the nodes in the graph. In the graph above, we notice four "0", meaning that we have 4 nodes.
 
Numbers- The other values(7,5,8,2) represents the edge's weight, representing the direct path to theat node. 


TEST 

MEMORY PERFORMANCE TEST RESULTS:

<img width="638" alt="Screenshot 2024-04-29 at 5 07 19 PM" src="https://github.com/UOL-BADAL/Floyd-Algorithm-Assignment/assets/167023997/3a28875b-65ca-4311-8304-1ca6cab71165">


SPEED PERFORMANCE TEST RESULTS: 

<img width="438" alt="Screenshot 2024-04-29 at 5 07 28 PM" src="https://github.com/UOL-BADAL/Floyd-Algorithm-Assignment/assets/167023997/839d2134-d158-4c70-b9b4-3a9ccafe1fde">



License

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the Licens
