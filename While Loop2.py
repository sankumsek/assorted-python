#Project 5: Indefinite Iteration
#2: NBA Fan by State

states = {"Arizona": "Phoenix Suns",
          "Minnesota": "Minnesota Timberwolves",
          "California": "Los Angeles Lakers/Clippers or Golden State Warriors or Sacramento Kings",
          "Oklahoma": "Oklahoma City Thunder",
          "Texas": "Dallas Mavericks or San Antonio Spurs or Houston Rockets",
          "Georgia": "Atlanta Hawks",
          "Massachusetts": "Boston Celtics",
          "North Carolina": "Charlotte Bobcats",
          "Louisiana": "New Orleans Pelicans",
          "Tennessee": "Memphis Grizzlies",
          "Pennsylvania": "Philadelphia 76ers",
          "New York": "Brooklyn Nets or New York Knicks",
          "Ohio": "Cleveland Cavaliers",
          "Indiana" : "Indiana Pacers",
          "Wisconsin": "Milwaukee Bucks",
          "Florida": "Miami Heat or Orlando Magic",
          "Illinois": "Chicago Bulls",
          "Michigan": "Detroit Pistons",
          "Colorado": "Denver Nuggets",
          "Utah": "Utah Jazz",
          "Oregon": "Portland Trailblazers",
          "Canada": "Toronto Raptors",
          "District of Columbia": "Washington Wizards"}

while True:
    z = str(input("Enter your state (unless your from Canada): "))
    if z in states:
        print ("So I see your a fan of", states[z],)
