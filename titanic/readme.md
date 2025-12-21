
This is a competition from Kaggle, we need to predict whether a passenger could survive in this disaster.

* submission result

|time|Kaggle test score|train cross_val_score|
|---|---|---|
|1|0.76076|0.805831|
|2|0.77272|0.8441|


Train.csv is provided for training proper models, so it includes survival information.

However, test.csv is provided for predicting, so it doesn't include survival information.


Related Variables are as follows:


|variable|explanation|type of Varible|Solution|
|---|---|---|---|
|PassengerId|id|/|no use|
|Survived|y|/|0|utilize model|
|Pclass|categorical, ticket class|
|Name|id|
|Sex|/|categorical|
|Age|/|numerical|
|SibSp|of siblings / spouses aboard the Titanic.<br>The dataset defines family relations in this way...<br>ParcSibling = brother, sister, stepbrother, stepsisterh:<br>Spouse = husband, wife (mistresses and fiancés were ignored)|
|Parch|of parents / children aboard the Titanicstepsisterh<br>The dataset defines family relations in this way...<br>TickParent = mother, fatheret:<br>Child = daughter, son, stepdaughter, stepsonTicket number<br>FareSome children travelled only with a nanny, therefore parch=0 for them.:<br>Passenger fare<br>|
|Ticekt|Seat number|/|
|Cabin| Cabin number|/|Used to Classify level|
|Embark|Port of Embarkation	C = Cherbourg, Q = Queenstown, S = Southampton|numerical|
