# PyQuiz
Quiz platform written in Python 3.4.3

##How to use
Questions are stored in the 'questions' array.<br><br>
To add or modifiy questions, answers and the correct answer, use this format:<br>
  \["\<Question>", ["\<Answer1>","\<Answer2>","\<Answer3>"], \<Correct>]<br>
(E.g: ["What is the capital of England?", ["London","Birmingham","Manchester", "Leeds"], 0])<br><br>
The 'correct' number is what answer in  the list is correct, starting from 0. In the example above, London is the capital of England. As England is the first in the list of answers, the 'correct' value is '0'.
