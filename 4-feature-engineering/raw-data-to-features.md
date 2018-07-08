Which of these features are related to the objective?

1) Objective: Predict total number of customers who will use a certain discount coupon
- Font of the text with which the discount is advertised on partner websites
- Price of the item the coupon applies to

2) Objective: Predict point-of-sale credit card fraudulent activity
- Whether cardholder has purchased these items at this store before
- Category of item being purchased

Why is the second a bad feature? What could go wrong? 
Hint: what happens if the cluster ID was taken from another model? What if that model updates without telling you? Will you still be able to learn anything from your training data?
- city: "US/SEA"
- inferred_city_cluster_id: 1952

- Feature definitions should not change over time
- Ambiguous feature field values could cause issues
- "inferred" seems to imply this field could come from another system which we may not have knowledge or control over the city-value mappings

Are these features knowable at prediction time?

1) Objective: Predict total number of customers who will use a certain discount coupon
- Number of discountable items sold the previous month
- Number of customers who viewed ads about item

2) Objective: Predict whether a credit card transaction is fraudulent
- Whether cardholder has purchased these items at this store before
- Category of item being purchased
- Online or in-person purchase
- Whether item is new at store (and can not have been purchased before)


Features should be Numeric

Which of these features are numeric (or could be in a useful form)?

1) Objective: Predict total number of customers who will use a certain discount coupon
- Percent value of the discount (e.g. 10% off, 20% off, etc.)
- Font an advertisement is in (Arial, Times New Roman, etc.) - categorical - not meaningful numeric
- Item category (1 for dairy, 2 for deli, 3 for canned goods, etc.) - categorical - not meaningful numeric

Which of these will it be difficult to get enough examples for?
---------

Objective: Predict customer discount coupon usage

- Percent discount of coupon (20%, 30%, etc.)
- Date that promotional offer starts
- Number of customers who opened advertising email
- answer is All of these we should be able enough examples for

Objective: Predict point-of-sale credit card fraudulent activity
- Example for Whether cardholder has purchased these items at this store before
- Example for Distance between cardholder address and store
- Example for Category of item being purchased
- Example for Online or in-person purchase
- none of above

Quiz
---

What are the characteristics of a good feature?
Have enough examples in the data
Be numeric with meaningful magnitude
Knowable at prediction time
Related to the objective

I want to build a model to predict whether Team A will win its soccer game against Team B. I will train my model on features computed on historical basketball games. One of my features is how many games this season Team A has won. How should I compute this feature?
- Compute num_games_won / num_games_played until the N-1 th game in order to train with the label for the N th game

I want to build a model to predict whether Team A will win its soccer game against Team B. Which of these attributes (computed on historical basketball games) are good features? Assume that these features are all computed appropriately without taking into account non-causal data.
- How often Team A wins games
- How often Team A wins games where its opponent is ranked in the top 10
- How many of the last 7 games that Team A played that it has won
- The fraction of games that Team A won when it played against Team B when both teams had this exact set of players


Imagine you are the business owner of a same-day grocery food delivery service which prides itself on driving and delivering the freshest foods to their customers. Recently, some of your customers have started to complain that they are not getting their food orders on time. You are thinking of building a machine learning model to help optimize route times between your warehouse and individual customers but you don't know which features you should focus on first.

From the below list of available data fields, pick the MOST useful and the LEAST useful to your food delivery service model and explain your reasoning.

Daily weather temperature and forecasts - Most useful because weather can cause the delay in delivery because of traffic or foggy weather
Route times for your common delivery areas - Most useful, the route time could be the busiest time for delivery area
Temperature sensors inside of your delivery trucks - Least useful. Has nothing to do with dealy
Category of items in each order - Most useful, more categories in an order more time it might take to collect them
Customer ratings of your delivery drivers - Most useful, some drivers can cause delay for unknown reasons like take slow routes or drive slow
