
This is a competition from Kaggle, we need to predict whether a passenger could survive in this disaster.

Train.csv is provided for training proper models, so it includes survival information.

However, test.csv is provided for predicting, so it doesn't include survival information.


Related Variables are as follows:


|variable|explanation|type of Varible|null per|Solution|
|---|---|---|---|---|
|PassengerId|id|/|0|no use|
|Survived|y|/|0|utilize model|
|Pclass|categorical, ticket class|/|0|
|Name|id|/|0|
|Sex|/|categorical|0|
|Age|/|numerical|177/891|
|SibSp|of siblings / spouses aboard the Titanic.<br>The dataset defines family relations in this way...<br>ParcSibling = brother, sister, stepbrother, stepsisterh:<br>Spouse = husband, wife (mistresses and fiancés were ignored)|/|0|
|Parch|of parents / children aboard the Titanicstepsisterh<br>The dataset defines family relations in this way...<br>TickParent = mother, fatheret:<br>Child = daughter, son, stepdaughter, stepsonTicket number<br>FareSome children travelled only with a nanny, therefore parch=0 for them.:<br>Passenger fare<br>|/|0|
|Ticekt|Seat number|/|0|
|Cabin| Cabin number|/|687/891|no use|
|Embark|Port of Embarkation	C = Cherbourg, Q = Queenstown, S = Southampton|numerical|2/891|

# Step 1
## explorative data analysis