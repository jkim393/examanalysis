# Exam Analysis Script (Python)

## Good To Know Beforehand
* This script requires a ".csv" file to run (refer to demoFile.csv for formatting exam data)
    - In Google Sheets: File > Download as > .csv
    - free response score is optional
* This script requires "numpy" package
     - python3 example: sudo apt install python3-pip > pip3 install numpy
* Although we created our csv files using google sheets, the process should be similar for Microsoft Excel.

## How to run demo file
* In terminal: python examAnalysis.py demoFile.csv
* demoFile_results.csv should be generated in same folder

## clarifciation of terminology in generated results file
* r with MC: Correlates a list of whether a student got the answer correct (0 or 1), with their respective exam score.  
    - tells us if students who generally scored higher did well on that question
    - lower may indicate students were just guessing on the question, or a very difficult question
* KR-20: measured reliability of the test
    - higher is better, score above .5 is reasonable
* "#" of A: number of people who chose answer choice A
* % of A: percent of people who choise answer choice A
* r of A: 
    - If A is the correct answer, r of A will equal r with MC.  
    - If A is the wrong answer, we would usually want a negative number.  A positive number would indicate that people who did well on the exam, tended to do poorly on that question.






Written by JiHwan Kim, Tasmiyah Qazi and Joshua Sun  
