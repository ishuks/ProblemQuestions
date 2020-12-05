# ProblemQuestions

Time and Space complexities given on a function-wise basis in each problem file, assumptions and design decisions described below. 

Longest File Path:

  Assumptions:
    
    - Directory names will not contain a full-stop 
    - Only backslashes will be used to discriminate between dirs,subdirs and files (not forward facing as in mac OS) 
    - Input type will be a string with structure following that of problem definition file

  Design Decisions: 
  
    - Parse string and longest file path functions defined separately to modularise code and make components easier to test 
    - Object oriented solution chosen so that user could use it as "blackbox" without being confused regarding separate parse string and longest path functions
    - Closure (nested) function used within longest file path for ease in variable scope definiton 

Hit Counter: 

  Assumptions: 
  
    - valid timestamps (greater than 0) input to record function 
 
  Design Decisions: 
  
    - Two classes given for reference, one for ordered and one for unordered timestamp data, unordered used in final solution for its greater flexibility 
    - Total hits variable defined separately to avoid summing over a large array (time intensive) 
    - Dictionary used for key,value functionality which allows grouping of hits over timestamps - allows unordered input and reduced space in some cases (although         not in worst case of each timestamp having 1 hit only)
