# BetwaySkybetArb
Simple web scraping to retrieve data from Skybet and Betway. The dataanalysis.py script compares implied probabilities to investigate whether a statistically safe bet can be placed, which is indicated by either arb1 or arb2 being less than 100%. The script produces a graph showing the arbitrage for both combinations. If arb1 is the statistically safe bet, then one would you use Skybet to bet on fighter 1 winning and Betway to bet on fighter2 winning. Conversely, if arb2 is the safe bet, then one would use Betway to bet on fighter1 to win and Skybet to bet on fighter2 to win.
The script works well 90% of the time. In some cases the script run too quickly for the internet speed, or the internet may be too slow at times, and returns an error stating an element is not clickable. Also, in the plot, it does not always show the arbitrage values for some reason.

It has been successful in finding a configuration of bets that are statistically safe. Configurations which return 40% of the initial bet have been found regularly, only when Skybet boosts bets in the lead up to certain events, which are is far greater than typical arbitrage bets associated with football, where it is rare to find an arbitrage greater than 10%. This could be due to mixed martials arts being a less established sport, and so there is a greater variance between betting companies when setting odds. As betting companies monitor other betting sites to avoid arbitrage being possible, the difference could be due to MMA bets not being monitored as closely as football. Though, these theories are conjecture based on my observations with no real data backing this up. It will likely be another project of mine to investigate how one could maximise returns by placing configurations of multiple bets.
