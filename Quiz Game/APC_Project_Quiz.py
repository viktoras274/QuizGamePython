from tkinter import *
from tkinter import font as tkFont
from tkinter import ttk
import random

root = Tk()                                                                         # creates the root window of the program
root.title("Quiz Game")                                                             # sets a title to the root window(upper left corner)
root.iconbitmap("quiz.ico")                                                         # sets an icon to the root window(upper left corner) from the given destination folder
root.geometry("650x400")                                                            # sets fixed dimensions for the root window
root.configure(background='gray70')                                                 # sets a background color to the root window

# Fonts to be used in Labels or Buttons
arial24 = tkFont.Font(family='Arial', size=24, weight='bold')
arial12 = tkFont.Font(family='Arial', size=12, weight='bold')

# The majority of the questions have been taken from various internet sources that provide questions for quizzes.
class Easy:
    class GeneralKnowledgeEasy:
        general_knowledge_easy = [["Which is the smallest planet in our solar system?", "Mercury", "Venus", "Earth", "Neptune"],
                                  ["Which country in the world is believed \nto have the most miles of motorway?", "China", "USA", "Germany", "Russia"],
                                  ["What does the Latin Tempus mean in English?", "Time", "Temple", "Temporary", "Temper"],
                                  ["Which is the biggest ocean in the world?", "Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
                                  ["The food giant Nestle is based in which country?", "Switzerland", "Spain", "United Kingdom", "Hungary"],
                                  ["Which of the following is biologically \nclassified as an insect?", "Dragonfly", "African Elephant", "Golden Eagle", "Goldfish"],
                                  ["Which of the following is a popular condiment \namongst Americans to put on a hotdog?", "Mustard", "Wasabi", "Tartare sauce", "Mano chutney"],
                                  ["In which game do you have to match tiles?", "Dominoes", "Chess", "Monopoly", "Solitaire"],
                                  ["Which group of Scandinavians \ninvaded and conquered other lands?", "The Vikings", "The Knights", "The Romans", "The Foresters"],
                                  ["If you have cryophobia, what are you afraid of?", "Cold", "Heat", "Water", "Sun"]
                                  ]

    class GeographyEasy:
        geography_easy = [["Which is the capital city of Finland?", "Helsinki", "Oslo", "Stockholm", "Copenhagen"],
                          ["In which country would you be if \nyou were visiting the Taj Mahal?", "India", "China", "Pakistan", "Indonesia"],
                          ["In which city is the Big Ben located?", "London", "New York", "Los Angeles", "Paris"],
                          ["Which is the capital city of Greece?", "Athens", "Thessaloniki", "Patra", "Mykonos"],
                          ["What is the population of Belgium?", "11 million", "8 million", "25 million", "10 million"],
                          ["San Marino is the Capital of which country?", "SanMarino", "Anguilla", "Italy", "Monaco"],
                          ["Mexican hat dances are danced \naround which kind of headwear?", "Sombrero", "Cowboy hat", "Baseball cap", "Derby"],
                          ["In which country is lake Como located?", "Italy", "Austria", "Switzerland", "France"],
                          ["In which continent is Germany located?", "Europe", "Asia", "Australia", "Africa"],
                          ["In which continent is Austria located?", "Europe", "Asia", "Australia", "Africa"]
                          ]

    class HistoryEasy:
        history_easy = [["Who was the THIRD man to walk on the moon?", "Charles Pete Conrad", "Mark Hamill", "Neil Armstrong", "Astronaut Audrey"],
                        ["Where was the explorer Captain James Cook from?", "England", "Australia", "Portugal", "Germany"],
                        ["What colour was the Statue of Liberty originally?", "Copper", "White", "Green", "Yellow"],
                        ["Which war started in 1939 and ended in 1945?", "World War II", "World War I", "The Vietnam War", "The Falklands War"],
                        ["Who was the first president of USA?", "George Washington", "George Bush", "Ronald Reagan", "Donald Trump"],
                        ["Who roamed around Shewood Forest with his merry men?", "Robin Hood", "Richard the Lionheart", "King Arthur", "Braveheart"],
                        ["What was Che Guevara known as?", "A revolutionary", "Prime Minister of Peru", "25th President of the USA", "CEO of General Motors"],
                        ["In 1955, which famous American landmark \nopened in Anaheim, California?", "Disneyland", "The Statue of Liberty", "Knott's Berry Farm", "The Queen Mary Boat Tour"],
                        ["When did George Washington, the first US President, die?", "1799", "1599", "1999", "1299"],
                        ["Saddam Hussein was the President of which country?", "Iraq", "India", "Sudan", "Kuwait"]
                        ]

    class MoviesSeriesEasy:
        movies_series_easy = [["How many seasons does the TV series Friends has?", "10", "6", "4", "8"],
                              ["What is the name of the second movie in Harry Potter?", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Philosopher Stone", "Harry Potter and the Prisoner of Azkaban", "Harry Potter and The Order of The Phoenix"],
                              ["The head of what kind of animal is front-and-center \nin an infamous scene from The Godfather?", "Horse", "Dog", "Rabbit", "Rat"],
                              ["What 1994 crime film revitalized John Travolta’s career?", "Pulp Fiction", "Saturday Night Fever", "The Punisher", "Broken Arrow"],
                              ["What animated classic was the first film \nof the late-twentieth-century “Disney Renaissance?”", "The Little Mermaid", "The Lion King", "Hercules", "Bugs"],
                              ["Which of the following is NOT a James Bond movie?", "The Da Vinci Code", "Goldfinger", "Moonraker", "Spectre"],
                              ["In the movie 'Home Alone', which character was left behind?", "Kevin", "Craig", "Kyle", "Carlo"],
                              ["Which 1999 movie has this as its tagline, 'The Toys Are Back'?", "Toy Story 2", "Back To The Future", "Batman Forever", "Kate & Leopold"],
                              ["Which fictional boxer was portrayed by \nSilvester Stallone in six films from 1976 to 2006?", "Rocky Balboa", "Mike Tyson", "Ivan Drago", "Adonis Creed"],
                              ["What was the names of the two friends of Harry Potter?", "Hermione and Ron", "Lilo and Stich", "Daphne and Nick", "Samantha and Rupert"]
                              ]

    class MusicEasy:
        music_easy = [["In what decade was pop icon Madonna born?", "1950s", "1980s", "1970s", "1960s"],
                      ["In what song does Britney Spears \nsing 'I'm not that innocent?'", "Oops!...I Did It Again", "Boys", "Baby One More Time", "I'm A Slave 4 U"],
                      ["According to Spice Girls, if you wanna \nbe my lover, what do you gotta do?", "Get with my friends", "Meet my mom", "Put a ring on it", "Get a job"],
                      ["Which classic band recorded the songs 'Hey Jude' and 'Let It Be'?", "The Beatles", "Queen", "ABBA", "Spice Girls"],
                      ["Which band recorded the songs 'Highway To Hell' \nand 'You Shook Me All Night Long'?", "AC/DC", "Guns n' Roses", "Metallica", "Queen"],
                      ["Which singer has realized the songs \n'Pappa Don't Preach' and 'Open Your Heart'?", "Madonna", "Cher", "Britney Spears", "Gwen Stefani"],
                      ["What singer for a '70s British rock quartet \nchanged his name from Frederick Bulsara?", "Freddie Mercury", "Elton John", "John Lennon", "Michael Jackson"],
                      ["Which male singer sang 'Boyfriend' in 2012?", "Justin Bieber", "Justin Timberlake", "Usher", "Drake"],
                      ["Which male singer had a hit with 'Marry You'?", "Bruno Mars", "Justin Bieber", "Mac Miller", "Harry Styles"],
                      ["Which female singer had a hit with 'Stronger'?", "Kelly Clarkson", "Katy Perry", "Madonna", "Taylor Swift"]
                      ]

    class ScienceEasy:
        science_easy = [["What do you call the process of turning from liquid into vapor?", "Evaporation", "Condensation", "Precipitation", "Collection"],
                        ["In physics, what is defined as the ability of a body to do work?", "Energy", "Mass", "Strength", "Speed"],
                        ["WHat is the center of our solar system?", "The sun", "The Milky Way", "Mercury", "The Earth"],
                        ["Which planet is the closest to ours in the solar system?", "Venus", "Jupiter", "Mercury", "Uranus"],
                        ["What planet is closest in size to our moon?", "Mercury", "Zeus", "Mars", "Jupiter"],
                        ["What's removed from water in the process of desalination?", "Salt", "Sand", "Soil", "Dust"],
                        ["What's the base unit of mass in the metric system?", "The kilogram", "The liter", "The pound", "The feet"],
                        ["Which type of plastics can be recycled?", "Thermoplastics", "Polyethylene Terephthalate", "Polystyrene", "Polypropylene"],
                        ["In the human body, what does dermal relate to?", "Skin", "Head", "Ear", "Leg"],
                        ["In which part of the human body is the aortic valve?", "Heart", "Stomach", "Liver", "Lung"]
                        ]

    class SportsEasy:
        sports_easy = [["In which football team does Cristiano Ronaldo play at?", "Juventus", "Manchester United", "Barcelona", "Real Madrid"],
                       ["Which football team did win the Premier League in 2019-2020?", "Liverpool", "Chelsea", "Manchester City", "Arsenal"],
                       ["What are the five colours of the Olympic rings?", "Blue, Yellow, Black, Green and Red", "Black, Yellow, Green, Orange, Blue", "Red, Green, Blue, Black, Orange", "Blue, Purple, White, Green, Yellow"],
                       ["Which of these sporting figures does NOT have a \nfamous sibling involved in the same sport?", "Usain Bolt", "Peyton Manning", "Vitali Klitschko", "Serena Williams"],
                       ["Which of these professional soccer teams is NOT from Spain?", "Sporting Lisbon", "Atletico Madrid", "Atletic Bilbao", "Sevilla F.C."],
                       ["What is the name of both a grand slam tennis \ntournament and an FA Cup-winning English soccer team?", "Wimbledon", "Liverpool", "Arsenal", "Chelsea"],
                       ["Which of the following is not a team sport?", "Golf", "Basketball", "Handball", "Hockey"],
                       ["Which movie star was an Austrian \nJunior Olympic Weightlifting Champion?", "Arnold Schwarzenegger", "Silvester Stallone", "Robert De Niro", "Dwayne Johnson"],
                       ["What is the maximum number of clubs a golfer \nis allowed in their bag for a round of golf?", "14", "20", "9", "5"],
                       ["What is the 'perfect score' in a single game of Ten Pin Bowling?", "300", "500", "100", "200"]
                       ]

class Medium:
    class GeneralKnowledgeMedium:
        general_knowledge_medium = [["What is the name of the engine developed \nby Ford which aims to improve fuel efficiency \nwithout sacrificing power?", "EcoBoost", "SaveFuel", "GoFast", "WasteLess"],
                                    ["How is the first day of the 1929 Wall Street Crash often known?", "Black Thursday", "Bloody Sunday", "Shrove Tuesday", "Bank Holiday Monday"],
                                    ["What animal's name means 'little man in armor'?", "Armadillo", "Alpaca", "Aardvark", "Armadura"],
                                    ["The Nazi SS troops wore what color shirts?", "Black", "Red", "White", "Yellow"],
                                    ["What color is the M in McDonald's?", "Yellow", "Red", "White", "Brown"],
                                    ["Where were 'Belgian' waffles invented?", "Luxembourg", "Belgium", "The Netherlands", "France"],
                                    ["Which of the following types of fiber is produced \nsynthetically rather than occurring in nature?", "Polyester", "Cotton", "Silk", "Wool"],
                                    ["What year did the Titanic sink in the Atlantic Ocean \non its maiden voyage from Southampton?", "1912", "1930", "1940", "1905"],
                                    ["What is the main color of the UN flag?", "Blue", "White", "Red", "Black"],
                                    ]

    class GeographyMedium:
        geography_medium = [["How many countries are there in the region of \nEurope? (Recognised by the United Nations)", "44", "48", "52", "40"],
                            ["Machu Picchu can be found in which country?", "Peru", "Argentina", "Brazil", "Chile"],
                            ["The Sahara Desert extends into how many countries", "10", "5", "13", "7"],
                            ["Baku is the capital city of which eastern European country?", "Azerbaijan", "Ukraine", "Georgia", "Armenia"],
                            ["Which city would you visit to see Gaudi's fantastical architecture?", "Barcelona", "Madrid", "Porto", "Lisbon"],
                            ["Which city is the capital of Georgia?", "Tbilisi", "Baku", "Atlanta", "Tirana"],
                            ["What is the capital of the US state of New York?", "Albany", "New York", "Utica", "Springfield"],
                            ["In which city is the Taipei 101, formerly \nthe world's tallest building, located?", "Taiwan", "Kuala Lumpur", "Singapore", "USA"],
                            ["The United Kingdom is comprised of how many countries?", "4", "2", "3", "6"],
                            ["In which part of Asia is Afghanistan located?", "Southwest", "Northeast", "Northwest", "Southeast"]
                            ]

    class HistoryMedium:
        history_medium = [["Who did Henry VIII first marry?", "Catherine of Aragon", "Meghan Markle", "Kate Middleton", "Holly Willoughby"],
                          ["Which Roman emperor built a gigantic wall \nacross the North East of England in 122 AD?", "Hadrian", "Augustus", "Nero", "Caesar"],
                          ["What is Thomas Edison famous for inventing?", "Light Bulb", "WiFi", "iPad", "Telephone"],
                          ["Who was President of South Africa from 1994 to 1999?", "Nelson Mandela", "Kgalema Motlanthe", "Jacob Zuma", "Cyril Ramaphosa"],
                          ["Who painted the Mona Lisa?", "Leonardo Da Vinci", "El Greco", "Michelangelo", "Picasso"],
                          ["What was the name of the first Roman emperor to \nconquer Britannia (modern day England and Wales)?", "Claudius", "Chad", "Colin", "Cody"],
                          ["Which of these architectural periods \noccurred earliest in history?", "Romanesque", "Renaissance", "Baroque", "Gothic"],
                          ["Where was Christopher Columbus born?", "Genoa, Italy", " London, England", "Paris, France", "Lisbon, Portugal"],
                          ["What 1907 diplomatic conference focused on \nwartime law and rights of neutral nations?", "The Hague Peace Conference", "Geneva Conference", "Camp David Accords", "Concert of Europe"],
                          ["In what year was Queen Elizabeth II born?", "1926", "1940", "1910", "1933"]
                          ]

    class MoviesSeriesMedium:
        movies_series_medium = [["Which 2014 Seth Rogen film caused the North Korean \ngovernment to threaten action against the United States?", "The Interview", "The Pineapple Express", "This is the end", "Superbad"],
                                ["What is the name of Episode III in the Star Wars films?", "Revenge of the Sith", "Return of the Jedi", "The Phantom Menace", "New Hope"],
                                ["Which colour pill does Neo swallow in The Matrix?", "Red", "Blue", "Green", "White"],
                                ["Who is the only actor to receive an Oscar \nnomination for acting in a Lord of the Rings movie?", "Ian McKellen", "Orlando Bloom", "Elijah Wood", "Sean Bean"],
                                ["What is the highest-grossing R-rated movie of all time?", "Joker", "The Lord of The Rings: Return of The King", "The Avengers: Endgame", "Star Wars: The Rise of Skywalker"],
                                ["Who plays Gilbert in the film 'What's Eating Gilbert Grape'?", "Johnny Depp", "Tom Cruise", "Leonardo DiCaprio", "Mark Wahlberg"],
                                ["Which Disney movie was the first to have a soundtrack album?", "Snow White and the Seven Dwarfs", "Tron", "The Little Mermaid", "Hercules"],
                                ["Who plays Elizabeth Swann in 'Pirates of the Caribbean'?", "Keira Knightley", "Mandy Moore", "Paris Hilton", "Hilary Duff"],
                                ["Which actress stars in the movie \n'Eat Pray Love' released in 2010?", "Julia Roberts", "Jennifer Lopez", "Drew Barrymore", "Mandy Moore"],
                                ["Which actress played Daphne in the 2002 \nlive-action film of 'Scooby-Doo'?", "Sarah Michelle Gellar", "Nicole Kidman", "Amy Adams", "Kate Hudson"]
                                ]

    class MusicMedium:
        music_medium = [["In what year did The Beatles split up?", "1970", "1967", "1976", "1972"],
                        ["Globally popular in the late 1970s and early 1980s, \nwhat was the name of the new-wave band where Sting started out?", "The Police", "The FBI", "The Secret Service", "The Navy Seals"],
                        ["What famous Country singer Walked the LIne, \nfell into a Ring of Fire, and was a Boy Named Sue?", "Johnny Cash", "Willie Nelson", "Elvis Presley", "Hank Williams Jr"],
                        ["What Beatles song advises: \n'One thing I can tell you is you got to be free?", "Come Together", "Let it be", "Hey Jude", "Here comes the sun"],
                        ["What song includes the lines: \n'I've lived a life that's full / \nI traveled each and ev'ry highway...'?", "My way", "Strangers in the night", "Summer wind", "It was a very good year"],
                        ["Who was the first female artist to debut on \nthe Billboard album chart at Number One?", "Whitney Houston", "Cher", "Madonna", "Lady Gaga"],
                        ["In which group were Benn, Bjorn, Agnetha and Frida?", "ABBA", "Queen", "The Beatles", "AC/DC"],
                        ["How many solo number 1 singles had Michael Jackson?", "11", "20", "5", "7"],
                        ["What age did Michael Jackson die?", "50", "60", "45", "55"],
                        ["Who was the top-selling album artist of \nthe 1970s, according to Billboard?", "Elton John", "Michael Jackson", "Freddie Mercury", "John Lennon"]
                        ]

    class ScienceMedium:
        science_medium = [["Which of these space pioneers travelled in space first?", "Alan Shepard", "Neil Armstrong", "Buzz Aldrin", "Gus Grissom"],
                          ["If an airplane is travelling at the speed of \nsound, how fast is it going (in miles per hour)?", "767 mph", "76,700 mph", "7,670,000 mph", "7.67 mph"],
                          ["Which chemical element has the symbol Ni?", "Nickel", "Nobelium", "Niobium", "Nitrogen"],
                          ["What are the cold remains of a white dwarf called \nafter all its thermal energy has been exhausted?", "Black Dwarf", "Black Star", "Black Hole", "Blackbody"],
                          ["How many grams are in an ounce?", "28", "8", "280", "82"],
                          ["Which of these is one of the most viscous, \nslowest moving liquids on earth?", "Bitumen", "Water", "Honey", "Oil"],
                          ["What's the only metal that's \nnot a solid at room temperature?", "Mercury", "Iron", "Steel", "Sodium"],
                          ["What color does litmus turn when dipped into acid?", "Pink", "Black", "Purple", "Yellow"],
                          ["How many of the nine planets have moons?", "7", "9", "1", "5"],
                          ["What's the most malleable metal?", "Gold", "Magnesium", "Steel", "Aluminum"]
                          ]

    class SportsMedium:
        sports_medium = [["How many horses are on each team in a polo match?", "4", "6", "11", "8"],
                         ["Which European city hosted the 1936 Summer Olympics?", "Berlin", "London", "Montreal", "Paris"],
                         ["Including the home plate, how many bases are there on a standard baseball field?", "4", "6", "8", "2"],
                         ["Who was the first woman to win an Olympic gold medal?", "Charlotte Cooper", "Tara Lipinski", "Helen Jackson", "Vonetta Flowers"],
                         ["Which of these events is NOT an event in the modern pentathlon?", "High Jump", "Show jumping", "Swimming", "Fencing"],
                         ["Which city hosted the 2004 Olympic Games?", "Athens", "Paris", "London", "Beijing"],
                         ["Which country is the tennis star Rafael Nadal originally from?", "Spain", "Portugal", "France", "Italy"],
                         ["How often are the summer Olympic Games held?", "Every four years", "Every two years", "Every six years", "Every eight years"],
                         ["A shuttlecock is used in what sport?", "Badminton", "Ping-Pong", "Javelin", "Baseball"],
                         ["In Snooker what color is the ball that has a value of three points?", "3", "4", "6", "1"]
                         ]

class Hard:
    class GeneralKnowledgeHard:
        general_knowledge_hard = [["Which animal is not an insect?", "Centipede", "Wasp", "Beetle", "Flea"],
                                  ["Which of these snakes is the most venomous?", "Death adder", "Anaconda", "Sea snake", "Reticulated python"],
                                  ["In which city is the price of gold 'fixed' daily?", "London", "New York", "Singapore", "Tokyo"],
                                  ["Who was an English philosopher and physician \nknown as the 'Father of Classical Liberalism'?", "John Locke", "Francis Bacon", "Isaac Newton", "Thomas Hobbes"],
                                  ["For which deadly disease did Edward Jenner \ndevelop a vaccination technique in 1796?", "Smallpox", "Malaria", "Tuberculosis", "Japanese Encephalitis"],
                                  ["Which country uses the dong as its currency?", "Vietnam", "Thailand", "India", "Saudi Arabia"],
                                  ["How many permanent teeth does a dog have?", "42", "24", "18", "58"],
                                  ["What is the doll, Barbie's, full name?", "Barbara Millicent Roberts", "Dolly Barbie", "Sandy Gabriella Manny", "Marcella Williams"],
                                  ["What is the lifespan of a dragonfly?", "24 hours", "6 hours", "10 hours", "48 hours"],
                                  ["In what year was the first woman \nelected to the US Senate?", "1922", "1952", "1962", "1942"]
                                  ]

    class GeographyHard:
        geography_hard = [["Which is the capital city of Australia?", "Canberra", "Perth", "Melbourne", "Sydney"],
                          ["Which is the smallest country in the world?", "Vatican City", "Lichtenstein", "Luxembourg", "San Marino"],
                          ["Into which sea does the river Volga flow?", "The Caspian", "Baltic Sea", "Mediterranean Sea", "Black Sea"],
                          ["Which country has Anas Vaduz as its capital?", "Lichtenstein", "Bolivia", "Mongolia", "Montenegro"],
                          ["In which European city would you find the Spanish Steps?", "Rome", "Barcelona", "Madrid", "Lisbon"],
                          ["The Rialto Bridge is one of the four \nbridges spanning the Grand Canal in which town?", "Venice", "Rome", "Sicily", "Verona"],
                          ["Tangier is a coastal town in which Arab country?", "Morocco", "Qatar", "Lebanon", "Egypt"],
                          ["What is the traditional currency of Turkey?", "Lira", "Dirnam", "Drachma", "Pound"],
                          ["Which two locations are \nseparated by the Bering Strait?", "Alaska and Siberia", "Finland and Sweden", "The Netherlands and Sweden", "France and UK"],
                          ["Which country does not share a border with Germany?", "Italy", "Austria", "France", "Switzerland"]
                          ]

    class HistoryHard:
        history_hard = [["Who had the palaces and cathedrals built in Kremlin?", "Ivan The Great", "Peter The Great", "Lenin", "Catherine The Great"],
                        ["What natural disaster is believed to have caused \nthe decline of the culture of Ancient Crete?", "A Volcanic Eruption", "A Plague", "An Earthquake", "A Hurricane"],
                        ["When did the USA join the World War I?", "1917", "1914", "1916", "1918"],
                        ["Who was the first Secretary of the USSR Communist Party?", "Nikita Khrushchev", "Fidel Castro", "Joseph Stalin", "Anthony Eden"],
                        ["What was the first French settlement in North America?", "Quebec", "Montreal", "New York", "Nova Scotia"],
                        ["When did the French Revolution end, \nwith the seizure of power by Napoleon Bonaparte?", "1799", "1899", "1780", "1599"],
                        ["What was the name of the school in Athens, \nfounded by the philosopher Plato in 387 BC?", "The Academy", "University of Padua", "School of Athens", "Platonic University"],
                        ["What was the title for the medieval rulers of Italian \ncity-states such as Venice and Genoa?", "Doge", "Catt", "Hamstere", "Goldfishe"],
                        ["Which Greek philosopher tutored \nAlexander the Great until the age of 16?", "Aristotle", "Socrates", "Leonidas", "Plato"],
                        ["Who is the Viking that landed in Newfoundland in 1002?", "Leif Eriksson", "Ponce De Leon", "Christopher Columbus", "John Smith"]
                        ]

    class MoviesSeriesHard:
        movies_series_hard = [["Which was the first actor to play \nDumbledore in the Harry Potter films?", "Richard Harris", "Michael Gambon", "Christopher Lee", "Ian McKellen"],
                              ["Who is the alter ego of Scott Lang, as \nfeatured in the 2015 and 2018 Marvel films?", "Ant-Man", "Iron Man", "Hulk", "SpiderMan"],
                              ["What is the name of the elf played by \nWill Ferrell in the 2003 film Elf?", "Buddy", "Bushy", "Shiney", "Ben"],
                              ["Joe Pesci stars as 'Harry' and Daniel Stern is 'Marv' in which \n1990 Christmas comedy caper produced by John Hughes?", "Home Alone", "The Nightmare Before Christmas", "Jingle All the Way", "Miracle on 34th Street"],
                              ["Which 1993 Christmas film follows the misadventures \nof Jack Skellington, Halloweentown's pumpkin king?", "The Nightmare Before Christmas", "Jingle All the Way", "Miracle on 34th Street", "Home Alone"],
                              ["Which of the samurai in the 1954 film \n'Seven Samurai' is the first to die?", "Heihachi", "Shichiroji", "Kikuchiyo", "Kambei"],
                              ["What was the first James Bond feature film?", "Dr.No", "From Russia with Love", "Goldfinger", "Thunderball"],
                              ["The names of all seven of the daughters of Triton from \n'The Little Mermaid' start with which letter?", "A", "D", "R", "M"],
                              ["Mickey and Mallory are the names of the \nfamous mass murdering couple from what 90s movie?", "Natural Born Killers", "The Big Lebowski", "Die Hard", "Rushmore"],
                              ["In 'Pretty Woman', what are the names of the salesgirls \nwho help Vivian with her shopping spree?", "Mary Kate and Mare Frances", "Lizbeth and Elizabeth", "Kit and Barney", "Lana and Ava"]
                              ]

    class MusicHard:
        music_hard = [["Which two musicians collaborated on Another Way To Die,\n the theme song to 2008’s 007: Quantum of Solace?", "Alicia Keys and Jack White", "Michael Jackson and Justin Timberlake", "Adelle and Madonna", "Kenny Rogers and Dolly Parton"],
                      ["This Divine performer sang 'Wind Beneath My Wings' and 'The Rose'.", "Bette Midler", "Linda Ronstadt", "Liza Minnelli", "Tina Turner"],
                      ["Which song by Billy Joel includes brief, rapid-fire \nallusions to more than 100 headline events between 1949 and 1989?", "We Didn't Start The Fire", "Vienna", "Uptown Girl", "Just The Way You Are"],
                      ["What was the nickname of jazzman John Birks Gillespie?", "Dizzy", "Pizzi", "Dixie", "Kizzi"],
                      ["What 80's vocal group made up of three women released \nclassic dancing songs like, 'Venus' and 'Cruel Summer'?", "Bananarama", "Bangles", "The Go-Go's", "Blondie"],
                      ["What year were The Beatles formed?", "1959", "1965", "1945", "1950"],
                      ["What was John Lennon's middle name at birth?", "Winston", "Jon", "William", "Janny"],
                      ["'Lofsongur' is the national anthem of which country?", "Iceland", "Ireland", "United Kingdom", "Sweden"],
                      ["'The Abduction from the Seraglio' (Il Seraglio) \nis an opera by which composer?", "Wolfgang Amadeus Mozart", "Ludwig van Beethoven", "Johann Sebastian Bach", "Johannes Brahms"],
                      ["Ian Stewart was known as the sixth \nmember of which British rock group?", "The Rolling Stones", "Led Zeppelin", "Pink Floyd", "The Beatles"]
                      ]

    class ScienceHard:
        science_hard = [["What was the first probe to land on Venus?", "Venera 9", "Mariner 4", "Viking 1", "Venera 4"],
                        ["In the imperial system of measurements, \nhow many feet are there in a mile?", "5280", "1640", "7910", "3260"],
                        ["Which of these elements is NOT one \nof the halogens on the periodic table?", "Hydrogen", "Fluorine", "Iodine", "Chlorine"],
                        ["What carries the code for making \nproteins from the nucleus to the cytoplasm?", "Ribonucleic Acid", "Nitrogen Bubbles", "Iron Oxide", "Deoxyribonuc Ieic Acid"],
                        ["What is the chemical symbol for tungsten?", "W", "TUN", "GS", "BFF"],
                        ["How many main 'ring groups' are Saturn's \nthousands of rings split up into?", "7", "15", "3", "10"],
                        ["Which of these objects is not classified as a \nfull-fledged planet of a solar system?", "Ceres", "Mars", "Earth", "Jupiter"],
                        ["Fluorine, the most electronegative and reactive \nelement, is often found in what household product?", "Toothpaste", "Four", "Sugar", "Table salt"],
                        ["Who invented the periodic table?", "Dmitri Mendeleev", "Albert Einstein", "Issac Newton", "Blaise Pascal"],
                        ["Which metal is used in the making of microchips?", "Silicon", "Gold", "Steel", "Magnesium"]
                        ]

    class SportsHard:
        sports_hard = [["How many of his 45 races did Mike Hawthorn, \na former Formula One motor racing world champion, win?", "3", "2", "6", "5"],
                       ["Made from crushed stone, the courts \nat the French Open tennis tournament are said \nto be what kind of 'court'?", "Clay court", "Concrete court", "Cotton wool court", "Tarmac court"],
                       ["Which track and field event involves jumping \nover fence like obstacles while running?", "The Hurdles", "The High Jump", "The Pole Vault", "The Javelin Toss"],
                       ["What was the motto for the 2018 Winter Olympics?", "Passion connected.", "East Meets West", "Hot. Cool. Yours.", "Victory for all"],
                       ["Which country won three out of four FIFA World \nCups between 1958 and 1970, only interrupted in 1966?", "Brazil", "Hungary", "Sweden", "Czechoslovakia"],
                       ["How many men are on the field at \none time per team in American Football?", "11", "12", "13", "10"],
                       ["How many downs do you get to obtain \na first down in American Football?", "4", "6", "3", "2"],
                       ["Which two cities have the oldest stadiums \nin major league baseball in the USA?", "Boston and Detroit", "Chicago and Detroit", "Chicago and Boston", "New York and LA"],
                       ["In which decade were the \nBadminton Horse Trials first held?", "1940s", "1950s", "1960s", "1930s"],
                       ["In women's field hockey, which country \nhas won the most World Cups?", "The Netherlands", "Austria", "Australia", "Germany"]
                       ]

# This function destroys all widgets on root when called
def clear_root():
    root_slaves = root.grid_slaves()
    for widget in root_slaves:
        widget.destroy()

# This function disables the button provided in the parameter
def disable_button(button):
    button.configure(state=DISABLED)


# This class, when called with a given list of questions as parameter, initialises the quiz
class QuizGame:
    def __init__(self, questions_list):
        clear_root()
        self.quiz_questions = questions_list

        self.right_answer_button = Button(root, text="")            # This button has no text or any functionality(cannot be clicked). It is just made to store later the content of button with the correct answer and in case of given wrong answer to highlight the correct answer button with green color
        self.right_answer_button['font'] = arial12

        self.next_button = Button(root, text="Next", command=self.Question, bg="SkyBlue1")
        self.next_button['font'] = arial12

        self.right = 0                          # This variable will be used as a counter for the right answers per game
        self.question_number = 0
        self.Question()                         # call Question function to start generating questions

    # This function generates random questions and shuffles their answers.
    # Also creates buttons for each answer and some functions that set the
    # functionalities of those buttons. After the questions have been answered,
    # it shows the results of the game, the achieved score and provides the option
    # to give a name and save this score into the ranking table
    def Question(self):
        self.next_button.grid(row=5, column=0, pady=4, columnspan=3)

        if  self.question_number < 5:                                               # it checks whether the question_number is smaller than 5 (which is the maximum questions asked per game). If the question_number is less than 5, then continue, else jump to else..
            self.question_number += 1                                               # increment by 1 the question_number every time the conditions are met
            random_number = random.randint(0, len(self.quiz_questions) - 1)         # using the function randint from the random module, we create a random_number variable where we store random generated numbers from 0 to
            self.right_answer = self.quiz_questions[random_number][1]               # The right answer is stored inside the nested list in the second position with index 1

            answers = []
            for i in range(1, 5):                                                   # create an empty list where the 4 answers of every questions will be stored. We iterate from index 1 to 4(5 is excluded),
                answers.append(self.quiz_questions[random_number][i])               # because the answers in the quiz_questions nested lists are stored in those indexes and we want to append every single one from
            random.shuffle(answers)                                                 # every question. Then using the shuffle function from the random module we shuffle the order of the answers

            self.answer1 = answers[0]                                               # set as the first answer to be shown (in the first button) as the answer stored in index 0 of the answers list
            self.answer2 = answers[1]                                               # set as the first answer to be shown (in the first button) as the answer stored in index 1 of the answers list
            self.answer3 = answers[2]                                               # set as the first answer to be shown (in the first button) as the answer stored in index 2 of the answers list
            self.answer4 = answers[3]                                               # set as the first answer to be shown (in the first button) as the answer stored in index 3 of the answers list

            question = Label(root, text=self.quiz_questions[random_number][0], width=50, height=3, bg="SkyBlue1")           # The text of the question is stored inside the nested list in the first position with index 0
            question['font'] = arial12                                                                                  # By using a Label we project the question inside that Label above the answer buttons
            question.grid(row=0, column=0, padx=80, pady=(50, 5), columnspan=3)

            self.answer1_button = Button(root, text=self.answer1, width=30, height=2, bg="dodger blue", fg="white", disabledforeground="white", command=self.button1_click_functionality)       # create Button for the first answer, as text gets the content from answer1 variable, when clicked calls button1_click_functionality function
            self.answer1_button['font'] = arial12
            self.answer1_button.grid(row=1, column=0, pady=0.5)

            self.answer2_button = Button(root, text=self.answer2, width=30, height=2, bg="dodger blue", fg="white", disabledforeground="white", command=self.button2_click_functionality)       # create Button for the second answer, as text gets the content from answer2 variable, when clicked calls button2_click_functionality function
            self.answer2_button['font'] = arial12
            self.answer2_button.grid(row=1, column=1, pady=0.5)

            self.answer3_button = Button(root, text=self.answer3, width=30, height=2, bg="dodger blue", fg="white", disabledforeground="white", command=self.button3_click_functionality)       # create Button for the third answer, as text gets the content from answer3 variable, when clicked calls button3_click_functionality function
            self.answer3_button['font'] = arial12
            self.answer3_button.grid(row=2, column=0, pady=0.5)

            self.answer4_button = Button(root, text=self.answer4, width=30, height=2, bg="dodger blue", fg="white", disabledforeground="white", command=self.button4_click_functionality)       # create Button for the fourth answer, as text gets the content from answer4 variable, when clicked calls button4_click_functionality function
            self.answer4_button['font'] = arial12
            self.answer4_button.grid(row=2, column=1, pady=0.5)


            if self.answer1 == self.right_answer:                                   # checks whether the given answer (in this case answer1 from answer1_button) is the right answer
                self.right_answer_button = self.answer1_button                      # if true, then set the right_answer_button to be equal with this button(=answer1_button). If not check the next one

            elif self.answer2 == self.right_answer:                                 # checks whether the given answer (in this case answer2 from answer2_button) is the right answer
                self.right_answer_button = self.answer2_button                      # if true, then set the right_answer_button to be equal with this button(=answer2_button). If not check the next one

            elif self.answer3 == self.right_answer:                                 # checks whether the given answer (in this case answer3 from answer3_button) is the right answer
                self.right_answer_button = self.answer3_button                      # if true, then set the right_answer_button to be equal with this button(=answer3_button). If not check the next one

            else:                                                                   # checks whether the given answer (in this case answer4 from answer4_button) is the right answer
                self.right_answer_button = self.answer4_button                      # if true, then set the right_answer_button to be equal with this button(=answer4_button). If all previous 3 were false then this is going to be the right one

            self.quiz_questions.pop(random_number)                                  # pops a new random question from the chosen list of questions. Without it some questions may be repeated in the same game


        else:                                                                                       # when the question_number becomes 6, then no new question is popped from the questions list and the root is
            clear_root()                                                                            # cleared, so that the stats of the game can appear (and register the score to the player)

            label1 = Label(root, text="Right answers " + str(self.right) + "/5", bg="gray70")                     # creates a Label showing how many right answers have been given out of all the questions asked(=5)
            label1['font'] = arial12
            label1.grid(row=0, column=0, padx=(200,0), pady=(50,0))

            label2 = Label(root, text="You earned " + str(self.right * 10) + " points!", bg="gray70")             # creates a Label showing how many points have been earned according to performance
            label2['font'] = arial12
            label2.grid(row=1, column=0, padx=(200,0), pady=(15,0))

            label3 = Label(root, text="Enter your Name", bg="gray70")
            label3['font'] = arial12
            label3.grid(row=2, column=0, padx=(200,0), pady=(50, 0))

            global player_name
            player_name = Text(root, width=15, height=1)
            player_name['font'] = arial12
            player_name.grid(row=3, column=0, padx=(200,0), pady=(0, 50))

            save_score = Button(root, text="Save", bg="dodger blue", fg="white", command=lambda: [self.save('rankings.txt'), disable_button(save_score)])           # a command should be added here and a function should be created to save the score with the given name from the TextBox(maybe in a .txt file?)
            save_score['font'] = arial12
            save_score.grid(row=3, column=1, pady=(0,50))

            back_to_menu = Button(root, text="Back to Menu", bg="dodger blue", fg="white", command=run)    # creates a Button that returns player back to Start Menu
            back_to_menu['font'] = arial12
            back_to_menu.grid(row=4, column=0, padx=(200,0))

    # This function is called by the save function, after the save_score Button has been clicked.
    # When called it stores the returned sorted list from txt_sort function to a new list (alist) and
    # opens a txt file in write mode (w+). The plus sign means that in case that this file doesn't
    # exist in the file's location, then a new will be created with this name. Then all the elements
    # are written in the new txt file
    def write_new_txt(self):
        alist = self.txt_sort()
        with open('newrank.txt', 'w+') as text:
            for i in range(len(alist)):
                text.write(str(i+1) + ' ' + str(alist[i][0]) + ' ' + str(alist[i][1] + "\n"))        # str(i+1) because the first number in the rank is 1 not 0

    # This function is used to read the txt, where the scores are initially saved and do 3 things.
    # Sort the list based on name in order to gather all the duplicates, remove the duplicates but
    # before removing them add their scores and then sort the list again based on the scores in
    # descending order and return the sorted list.
    def txt_sort(self):
        with open('rankings.txt', 'r') as text:
            newlist = []
            for line in text:
                s = line.split()
                newlist.append(s)

            # sort based on name
            newlist.sort(key=lambda x: x[1])

            # check for duplicates
            for i in range(len(newlist) - 1):
                for j in range(i + 1, len(newlist) - 1):
                    if newlist[i][1] == newlist[j][1]:
                        newlist[i][0] = str(int(newlist[i][0]) + int(newlist[j][0]))
                        newlist[j][1] = '01'
                        newlist[j][0] = '01'

            # sort based on score
            for i in range(len(newlist) - 1):
                for j in range(len(newlist) - i - 1):
                    if int(newlist[j][0]) < int(newlist[j + 1][0]):
                        newlist[j], newlist[j + 1] = newlist[j + 1], newlist[j]

            # create a new nestedlist without the empty sublists
            finallist = []
            for i in range(len(newlist)):
                if newlist[i][1] != '01':
                    finallist.append(newlist[i])

            return finallist

    # This function is called when the save_score Button is clicked at the end of a game after a user has given a name.
    # As parameter is provided a txt file from the command of the Button. This file is opened in mode "append" (a+). The
    # plus sign means that in case that this file doesn't exist in the file's location, then a new will be created with
    # this name. Then 2 variables are defined, name and score. Name variable gets its value from the Text box, where the
    # player types and the score is calculated by multiplying the correct answers with 10. This 2 variables are written
    # in the txt file (score is typecasted in string) and then a function called "write_new_txt" is called.
    def save(self, path):
        with open(path, 'a+') as text:
            name = player_name.get("1.0", END)
            score = self.right * 10
            text.write(str(score) + ' ' + name)
        self.write_new_txt()


    # This function is called when the answer1_button is clicked.
    # First checks whether the buttons are locked. If not, then it
    # checks whether the given answer(=answer1) is the right answer
    # of the question. If not, then the clicked button(=answer1_button)
    # turns to Red color and the right answer(another button) turns Green.
    # If it is the right answer, then the clicked button turns to Green
    # color and increment the right variable by 1. After an answer button is
    # clicked and the results are given (red or green color button), the
    # lock_buttons variable is set to True and all buttons are locked.
    def button1_click_functionality(self):
        if self.right_answer != self.answer1:
            self.answer1_button.configure(bg="red")
            self.right_answer_button.configure(bg="green")
        else:
            self.answer1_button.configure(bg="green")
            self.right += 1
        disable_button(self.answer1_button)
        disable_button(self.answer2_button)
        disable_button(self.answer3_button)
        disable_button(self.answer4_button)

    # This function is called when the answer2_button is clicked.
    # First checks whether the buttons are locked. If not, then it
    # checks whether the given answer(=answer2) is the right answer
    # of the question. If not, then the clicked button(=answer2_button)
    # turns to Red color and the right answer(another button) turns Green.
    # If it is the right answer, then the clicked button turns to Green
    # color and increment the right variable by 1. After an answer button is
    # clicked and the results are given (red or green color button), the
    # lock_buttons variable is set to True and all buttons are locked.
    def button2_click_functionality(self):
        if self.right_answer != self.answer2:
            self.answer2_button.configure(bg="red")
            self.right_answer_button.configure(bg="green")
        else:
            self.answer2_button.configure(bg="green")
            self.right += 1
        disable_button(self.answer1_button)
        disable_button(self.answer2_button)
        disable_button(self.answer3_button)
        disable_button(self.answer4_button)

    # This function is called when the answer3_button is clicked.
    # First checks whether the buttons are locked. If not, then it
    # checks whether the given answer(=answer3) is the right answer
    # of the question. If not, then the clicked button(=answer3_button)
    # turns to Red color and the right answer(another button) turns Green.
    # If it is the right answer, then the clicked button turns to Green
    # color and increment the right variable by 1. After an answer button is
    # clicked and the results are given (red or green color button), the
    # lock_buttons variable is set to True and all buttons are locked.
    def button3_click_functionality(self):
        if self.right_answer != self.answer3:
            self.answer3_button.configure(bg="red")
            self.right_answer_button.configure(bg="green")
        else:
            self.answer3_button.configure(bg="green")
            self.right += 1
        disable_button(self.answer1_button)
        disable_button(self.answer2_button)
        disable_button(self.answer3_button)
        disable_button(self.answer4_button)

    # This function is called when the answer4_button is clicked.
    # First checks whether the buttons are locked. If not, then it
    # checks whether the given answer(=answer4) is the right answer
    # of the question. If not, then the clicked button(=answer4_button)
    # turns to Red color and the right answer(another button) turns Green.
    # If it is the right answer, then the clicked button turns to Green
    # color and increment the right variable by 1. After an answer button is
    # clicked and the results are given (red or green color button), the
    # lock_buttons variable is set to True and all buttons are locked.
    def button4_click_functionality(self):
        if self.right_answer != self.answer4:
            self.answer4_button.configure(bg="red")
            self.right_answer_button.configure(bg="green")
        else:
            self.answer4_button.configure(bg="green")
            self.right += 1
        disable_button(self.answer1_button)
        disable_button(self.answer2_button)
        disable_button(self.answer3_button)
        disable_button(self.answer4_button)


# This class, when called, clears the root window and creates a Start Quiz Button and a Ranking Button
class Start_Menu:
    def __init__(self):
        clear_root()
        self.Start_Quiz_Game = Button(root, text="Start Quiz", width=10, height=2, bg="dodger blue", fg="white", command=choose_difficulty)
        self.Start_Quiz_Game['font'] = arial24
        self.Start_Quiz_Game.grid(row=0, column=0, padx=200, pady=50)

        self.Rank = Button(root, text="Ranking", width=10, height=2, bg="dodger blue", fg="white", command=lambda: show_ranking('newrank.txt'))
        self.Rank['font'] = arial24
        self.Rank.grid(row=1, column=0 )

# This function is called when the Rank Button on the Start Menu window is clicked.
# It clears the root window from the previous widgets and opens the txt file provided in the
# parameter in read mode. In this txt all the scores and usernames are stored sorted in descending
# order and will be shown in this window, but because the length of this txt file may be longer than
# the fixed dimensions of the root window, a scrollbar has to be added first.
# After the creation of the scrollbar, 3 Labels are added (Number, Name and Score) in the top row,
# each in a different column. Then, an empty list (newlist) is created and every line from the txt
# file splits and its contents are stored in the newlist. Split() method returns the contents in a list,
# so the newlist becomes a nested list, with each sublist containing a number, name and score.
# With a for loop in the newlist, 3 labels are created for every iteration, starting from row 1 (since row 0 is
# already occupied and i starts with 0 a +1 is added in the row option). As text every label receives the string
# stored in the selected sublist.
# For example, for the first iteration i=0 so the newlist[0] is selected, for the hierarchy Label the string in
# newlist[0][0] is selected, since the number is stored first in the txt file, then the score in index 1 and in
# index 2 the name. After all the contents have been shown the txt is closed and a Button is added with a
# functionality to return the user to the Start Menu.
def show_ranking(path):
    clear_root()

    text = open(path, 'r')

    # Create main frame
    main_frame = Frame(root, bg="gray70", width=630, height=390)
    main_frame.grid(sticky='news')

    # Create a canvas
    canvas_ = Canvas(main_frame, bg="gray70", width=630, height=390)
    canvas_.grid(row=0, column=0, sticky='news')

    # Add scrollbar to canvas
    scrollbar_ = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas_.yview)
    scrollbar_.grid(row=0, column=3, sticky='ns')

    # Configure canvas
    canvas_.configure(yscrollcommand=scrollbar_.set)
    canvas_.bind('<Configure>', lambda e: canvas_.configure(scrollregion=canvas_.bbox("all")))

    # Create another frame inside canvas
    second_frame = Frame(canvas_, bg="gray70")

    # Add that new frame to a window in canvas
    canvas_.create_window((0,0), window=second_frame, anchor='nw')


    name_label = Label(second_frame, text="Name", bg="gray70", fg="dodger blue")
    name_label['font'] = arial24
    name_label.grid(row=0, column=1, padx=(0, 30), pady=7)

    score_label = Label(second_frame, text="Score", bg="gray70", fg="dodger blue")
    score_label['font'] = arial24
    score_label.grid(row=0, column=2, padx=0, pady=7)

    number = Label(second_frame, text='No.', bg="gray70", fg='dodger blue')
    number['font'] = arial24
    number.grid(row=0, column=0, padx=(150, 30), pady=7)

    newlist = []
    for line in text:
        s = line.split()
        newlist.append(s)

    for i in range(len(newlist)):
        hierarchy = Label(second_frame, text=newlist[i][0], bg='gray70')
        hierarchy['font'] = arial12
        hierarchy.grid(row=i+1, column=0, padx=(150,30), pady=7)

        names = Label(second_frame, text=newlist[i][2], bg="gray70")
        names['font'] = arial12
        names.grid(row=i+1, column=1, padx=(0, 30), pady=7)

        scores = Label(second_frame, text=newlist[i][1], bg="gray70")
        scores['font'] = arial12
        scores.grid(row=i+1, column=2, padx=0, pady=7)

    text.close()

    back_to_menu = Button(second_frame, text="←", bg="dodger blue", fg="white", command=run)  # creates a Button that returns user back to Start Menu
    back_to_menu['font'] = arial12
    back_to_menu.grid(row=len(newlist) + 1, column=1, padx=(0, 0))


# This function is called when the Start Quiz Button is clicked
# It clears the root window and creates a Label "Please Choose Difficulty Level"
# and beneath that Label creates 3 Buttons for each Difficulty
def choose_difficulty():
    clear_root()

    choose_difficulty_lbl = Label(root, text="Please Choose Difficulty Level", bg="gray70", fg="dodger blue")
    choose_difficulty_lbl['font'] = arial24
    choose_difficulty_lbl.grid(row=0, column=0, padx=75, pady=20)

    easy_btn = Button(root, text="Easy", width=10, height=2, bg="dodger blue", fg="white", command=choose_easy_category)
    easy_btn['font'] = arial12
    easy_btn.grid(row=1, column=0, pady=10, padx=10)

    medium_btn = Button(root, text="Medium", width=10, height=2, bg="dodger blue", fg="white", command=choose_medium_category)
    medium_btn['font'] = arial12
    medium_btn.grid(row=2, column=0, pady=10, padx=10)

    hard_btn = Button(root, text="Hard", width=10, height=2, bg="dodger blue", fg="white", command=choose_hard_category)
    hard_btn['font'] = arial12
    hard_btn.grid(row=3, column=0, pady=10, padx=10)


# This function is called when the Easy Difficulty Button is clicked.
# It destroys all widgets and creates a Label at the top "Please Choose Category",
# and beneath it creates one Button for each category (7 in total).
def choose_easy_category():
    clear_root()

    choose_category_lbl = Label(root, text="Please Choose Category", bg="gray70", fg="dodger blue")
    choose_category_lbl['font'] = arial24
    choose_category_lbl.grid(row=0, column=0, padx=100, pady=20, columnspan=2)

    general_btn = Button(root, text="General Knowledge", width=17, height=2, bg="dodger blue", fg="white", command=lambda: QuizGame(Easy.GeneralKnowledgeEasy.general_knowledge_easy))
    general_btn['font'] = arial12
    general_btn.grid(row=1, column=0, pady=10, padx=10)

    geography_btn = Button(root, text="Geography", width=17, height=2, bg="dodger blue", fg="white", command=lambda: QuizGame(Easy.GeographyEasy.geography_easy))
    geography_btn['font'] = arial12
    geography_btn.grid(row=2, column=0, pady=10, padx=10)

    history_btn = Button(root, text="History", width=17, height=2, bg="dodger blue", fg="white", command=lambda: QuizGame(Easy.HistoryEasy.history_easy))
    history_btn['font'] = arial12
    history_btn.grid(row=3, column=0, pady=10, padx=10)

    movies_btn = Button(root, text="Movies & TV Series", width=17, height=2, bg="dodger blue", fg="white", command=lambda: QuizGame(Easy.MoviesSeriesEasy.movies_series_easy))
    movies_btn['font'] = arial12
    movies_btn.grid(row=4, column=0, pady=10, padx=10)

    music_btn = Button(root, text="Music", width=17, height=2, bg="dodger blue", fg="white", command=lambda: QuizGame(Easy.MusicEasy.music_easy))
    music_btn['font'] = arial12
    music_btn.grid(row=1, column=1, pady=10, padx=0)

    science_btn = Button(root, text="Science", width=17, height=2, bg="dodger blue", fg="white", command=lambda: QuizGame(Easy.ScienceEasy.science_easy))
    science_btn['font'] = arial12
    science_btn.grid(row=2, column=1, pady=10, padx=0)

    sports_btn = Button(root, text="Sports", width=17, height=2, bg="dodger blue", fg="white", command=lambda: QuizGame(Easy.SportsEasy.sports_easy))
    sports_btn['font'] = arial12
    sports_btn.grid(row=3, column=1, pady=10, padx=0)


# This function is called when the Medium Difficulty Button is clicked
# It destroys all widgets and creates a Label at the top "Please Choose Category",
# and beneath it creates one Button for each category (7 in total).
def choose_medium_category():
    clear_root()

    choose_category_lbl = Label(root, text="Please Choose Category", bg="gray70", fg="dodger blue")
    choose_category_lbl['font'] = arial24
    choose_category_lbl.grid(row=0, column=0, padx=100, pady=20, columnspan=2)

    general_btn = Button(root, text="General Knowledge", width=17, height=2, bg="dodger blue", fg="white", command=lambda: QuizGame(Medium.GeneralKnowledgeMedium.general_knowledge_medium))
    general_btn['font'] = arial12
    general_btn.grid(row=1, column=0, pady=10, padx=10)

    geography_btn = Button(root, text="Geography", width=17, height=2, bg="dodger blue", fg="white", command=lambda: QuizGame(Medium.GeographyMedium.geography_medium))
    geography_btn['font'] = arial12
    geography_btn.grid(row=2, column=0, pady=10, padx=10)

    history_btn = Button(root, text="History", width=17, height=2, bg="dodger blue", fg="white", command=lambda: QuizGame(Medium.HistoryMedium.history_medium))
    history_btn['font'] = arial12
    history_btn.grid(row=3, column=0, pady=10, padx=10)

    movies_btn = Button(root, text="Movies & TV Series", width=17, height=2, bg="dodger blue", fg="white", command=lambda: QuizGame(Medium.MoviesSeriesMedium.movies_series_medium))
    movies_btn['font'] = arial12
    movies_btn.grid(row=4, column=0, pady=10, padx=10)

    music_btn = Button(root, text="Music", width=17, height=2, bg="dodger blue", fg="white", command=lambda: QuizGame(Medium.MusicMedium.music_medium))
    music_btn['font'] = arial12
    music_btn.grid(row=1, column=1, pady=10, padx=0)

    science_btn = Button(root, text="Science", width=17, height=2, bg="dodger blue", fg="white", command=lambda: QuizGame(Medium.ScienceMedium.science_medium))
    science_btn['font'] = arial12
    science_btn.grid(row=2, column=1, pady=10, padx=0)

    sports_btn = Button(root, text="Sports", width=17, height=2, bg="dodger blue", fg="white", command=lambda: QuizGame(Medium.SportsMedium.sports_medium))
    sports_btn['font'] = arial12
    sports_btn.grid(row=3, column=1, pady=10, padx=0)


# This function is called when the Hard Difficulty Button is clicked.
# It destroys all widgets and creates a Label at the top "Please Choose Category",
# and beneath it creates one Button for each category (7 in total).
def choose_hard_category():
    clear_root()

    choose_category_lbl = Label(root, text="Please Choose Category", bg="gray70", fg="dodger blue")
    choose_category_lbl['font'] = arial24
    choose_category_lbl.grid(row=0, column=0, padx=100, pady=20, columnspan=2)

    general_btn = Button(root, text="General Knowledge", width=17, height=2, bg="dodger blue", fg="white", command=lambda: QuizGame(Hard.GeneralKnowledgeHard.general_knowledge_hard))
    general_btn['font'] = arial12
    general_btn.grid(row=1, column=0, pady=10, padx=10)

    geography_btn = Button(root, text="Geography", width=17, height=2, bg="dodger blue", fg="white", command=lambda: QuizGame(Hard.GeographyHard.geography_hard))
    geography_btn['font'] = arial12
    geography_btn.grid(row=2, column=0, pady=10, padx=10)

    history_btn = Button(root, text="History", width=17, height=2, bg="dodger blue", fg="white", command=lambda: QuizGame(Hard.HistoryHard.history_hard))
    history_btn['font'] = arial12
    history_btn.grid(row=3, column=0, pady=10, padx=10)

    movies_btn = Button(root, text="Movies & TV Series", width=17, height=2, bg="dodger blue", fg="white", command=lambda: QuizGame(Hard.MoviesSeriesHard.movies_series_hard))
    movies_btn['font'] = arial12
    movies_btn.grid(row=4, column=0, pady=10, padx=10)

    music_btn = Button(root, text="Music", width=17, height=2, bg="dodger blue", fg="white", command=lambda: QuizGame(Hard.MusicHard.music_hard))
    music_btn['font'] = arial12
    music_btn.grid(row=1, column=1, pady=10, padx=0)

    science_btn = Button(root, text="Science", width=17, height=2, bg="dodger blue", fg="white", command=lambda: QuizGame(Hard.ScienceHard.science_hard))
    science_btn['font'] = arial12
    science_btn.grid(row=2, column=1, pady=10, padx=0)

    sports_btn = Button(root, text="Sports", width=17, height=2, bg="dodger blue", fg="white", command=lambda: QuizGame(Hard.SportsHard.sports_hard))
    sports_btn['font'] = arial12
    sports_btn.grid(row=3, column=1, pady=10, padx=0)


# This function, when called, initialises the Start_Menu class
def run():
    run = Start_Menu()


run()
root.mainloop()