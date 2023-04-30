# stock-monitoring

I'm going to be building a stock news monitoring project. 
I don't know how many of you trade stocks out there, but I've recently learned about it. People who trade stocks professionally have access to a Bloomberg terminal. 
It provides them with a number of things, the current stock prices of whichever companies they're looking at, and also the breaking news that's relevant to those companies. 
So depending on whether if they had some good news say they earned a lot of money in the last quarter, or they built a really great product or they developed a new vaccine. 
Then obviously you can imagine the price of their company's stock go up or down depending on the type of news that comes out. And finally these platforms also give the 
ability to alert when relevant pieces of news happen that are related to stocks that I'm or you're following.

So I'm going to DIY my own a Bloomberg terminal or at least the parts of the functionality that are quite useful. 
First, I'm going to pull in the stock prices of the stocks that I'm interested in. So I will be using an API to get this data. 
In my Python program, I set the program to run and fetch some news whenever I get a slightly extraordinary rise or an extraordinary fall. That way I can figure out what is 
the reason for this rise or what is the reason for this fall.
At the end, I'm going to send ourseves an SMS message telling me that was the big fluctuation that happened and what is the relevant news so that I can decide there and 
then whether if I want to sell my stock, or if I should buy more. 
