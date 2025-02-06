'''
    Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

Example
scores = [12, 24, 10, 24]
Scores are in the same order as the games played. She tabulates her results as follows:

                                     Count
    Game  Score  Minimum  Maximum   Min Max
     0      12     12       12       0   0
     1      24     12       24       0   1
     2      10     10       24       1   1
     3      24     10       24       1   1

Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.

Function Description

Complete the breakingRecords function in the editor below.

breakingRecords has the following parameter(s):

int scores[n]: points scored per game
Returns

int[2]: An array with the numbers of times she broke her records. Index  is for breaking most points records, and index  is for breaking least points records.
'''

def breaking_records(scores):
    if not scores:
        return[0,0]
    min_score = scores[0]
    max_score = scores[0]
    min_count = 0
    max_count = 0
    for score in scores:
        if score < min_score:
            min_score = score
            min_count += 1
        elif score > max_score:
            max_score = score
            max_count += 1
    return [max_count, min_count]

scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
print(breaking_records(scores))