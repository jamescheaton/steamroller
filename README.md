# Steamroller

Steamroller is an attempt to perform sentiment analysis on breaking news in sports to identify "steamers", a market with rapidly dropping odds e.g. a team's key player becomes injured / suspended.

This requires two parts, firstly the sentiment analysis needs to scan twitter / other breaking news sites and perform sentiment analysis.

The second part needs to determine whether this breaking news will have a positive / negative effect on the odds of that team and determine whether or not to back lay.

But before any of this, we need to see if it is possible to make a profit doing this.

We have to conistently identify odds that will shorten / lengthen by a significant amount to make profit. If the odds movements are too small, we would have to stake very large amounts for a small reward, and so a false positive becomes extremely risky. We need to factor in exchange commission as well.

The first part of this project will be analysing historical data to determine the correlation between odds movements and team information. We can get historical price data from Betfair. For the sentiment side, we need to find accounts that consistently post reliable news ahead of the rest of the pack. Think 'leakers', but these are consistently unreliable.

## Background

I have been an on / off matched bettor for a few years. Mainly off at the moment due to getting gubbed from almost every betting site.

Once you get on the gubbings the only way forward is the casino and advantage play. I have done some casino in the past (low / med risk) but I never had the bankroll for the high risk casino and value betting. I understand the maths & statistics behind these, but you do need to stomach the variance and risk being down for many months - for example a casino edge is only about 1% for blackjack, but they have the luxury of a massive bankroll and thousands of hands per hour.

I have just been made redudant from work (my employer went bankrupt) so I had been looking at some side-hustles in the meantime and came across Outplayed's new tool called the [Steam Chaser](outplayed.com/products/steam-chaser). This aims to identify quickly dropping odds and notifies the user before the bookmakers adjust their odds. This seems like a good idea, but even in their example they are betting on Brazilian markets just before their odds are adjusted, which seems like a surefire way to get stake restricted. But instead of the bookmaker, why not use the exchange? Do they react faster than the bookmakers? Can you make a profit reacting faster than the market?

### The Basic Idea

Matched betting is almost always focused on placing bets manually, so a lot of the tools are not focused on placing bets using an API. This is actually not straightforward, as smarkets does not have a public API, and Betfair requires a lump sum of ~£400 for access. So I understand why this is not taught (maybe this is the real goldmine?), so why not look into creating / using bots to trade for us? There are probably similar things running on the exchange, so we want to see if this is actually viable.

Thankfully, Betfair provides its [historical data](https://historicdata.betfair.com/#/home), however only the minute frequency is available for free. I am 100% sure we will need the /second data and 50% sure we need the /millisecond data.
