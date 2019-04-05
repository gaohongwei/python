Solution 1:
  RoR 
    1. Create deplayed jobs

  Python
    1. Read job from redis
    2. Get the model data/parameters by call REST API 
    3. Update the model status to runnning
    4. Calculte the model, score etc 
    5. Update the ml models (in RoR) with RestAPI



Solution 2:
  Let RoR control the jobq

  RoR 
    1. Create deplayed jobs
    2. Deplayed job logic
      Get the model data/parameters
      Pass data to Python by calling RestAPI
      Update the model status to runnning

  With Python RestAPI
    1. Learning
      Get ml model data/parameters
      Run machine learnig algorithms
      Calculte the model, score etc 
      Update the ml models (in RoR) with RestAPI

  Problem
    Will have many jobs running in python end
