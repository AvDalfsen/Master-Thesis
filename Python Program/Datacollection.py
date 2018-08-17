# -*- coding: utf-8 -*-
"""
Created on Thur May 17 11:58:10 2018

@author: Anne van Dalfsen
"""

# =============================================================================
# This program was intended mainly as a means to obtain the data necessary for a
# study into the efficacy of a combination of textual and emotional text features
# in the classification of those texts.
# 
# A secondary purpose was to allow for others to obtain their data in a similar fashion.
# Although the program is largely aimed at using the texts contained in the Brown
# Corpus, which is accessed through the NLTK package, an option exists to extract
# the data from your own texts as well. It would be a somewhat cumbersome process,
# especially with a large number of texts, but it would function and suffice for
# research purposes.
# 
# Once run, the program should provide sufficient instructions on how to use it.
# Nevertheless, notes have been made in the code for explananing what does what.
# 
# On a final note, at the time of writing this program I was, aside from the basics,
# largely self-taught in Python. As such, and I am well aware of this fact, the code
# is far from pretty and efficient. It functions and that is all it was made to do.
# =============================================================================

import nltk
from nltk.corpus import brown
import re
import pandas as pd
from collections import Counter
import numpy as np
import warnings
import sys
import csv
from nltk.corpus import stopwords

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)
warnings.simplefilter(action='ignore', category=Exception)

try: 
    nltk.data.find('brown')
    nltk.data.find('stopwords')
except LookupError:
    nltk.download('brown')
    nltk.download('stopwords')

df = pd.read_csv('CollectionData/dictionary.csv')
df_anger = pd.read_csv('CollectionData/anger.csv')
df_anticip = pd.read_csv('CollectionData/anticipation.csv')
df_disgust = pd.read_csv('CollectionData/disgust.csv')
df_fear = pd.read_csv('CollectionData/fear.csv')
df_joy = pd.read_csv('CollectionData/joy.csv')
df_neg = pd.read_csv('CollectionData/negative.csv')
df_pos = pd.read_csv('CollectionData/positive.csv')
df_sad = pd.read_csv('CollectionData/sadness.csv')
df_surp = pd.read_csv('CollectionData/surprise.csv')
df_trust = pd.read_csv('CollectionData/trust.csv')

removal = [',','!','"','#','$','%','(',')','[',']','*','+','.','/',"\\",';',':','@','_','—','?','”','“','``',"''",'--',"'","`"]

overloop = 1
main_loop = 1
loop = 1
loop2 = 0
loop3 = 0
loop4 = 0
loop5 = 0
loop6 = 0
loop7 = 0
loop8 = 0

while overloop == 1:
    main_loop = 1
    loop = 1
    while main_loop == 1:
        text = []
        text2 = []
        data = []
        while loop == 1:
            print("\nWelcome to this text analysing program.")
            
            print("\nPlease choose one of the following options:")
            
            print("\n1) Entire genres from the Brown Corpus")
            print("2) Individual texts from the Brown Corpus")
            print("3) Your own text")
            
            print("\n4) Output all data from all individual texts in the Brown Corpus into a csv file.")
            print("   Note: This can take a considerable amount of time; a decent machine took ~11 minutes to finish.")
    
            print("\n0) Stop and Exit.")
            
            choice = input("Please enter your choice: ")
            if choice == '1':
                loop = 0
                loop2 = 1
            elif choice == '2':
                loop = 0
                loop2 = 2
            elif choice == '3':
                loop = 0
                loop2 = 3
            elif choice == '4':
                loop = 0
                main_loop = 3                
            elif choice == '0':
                sys.exit("\nProgram is stopping. Thank you for using this program.")
            else:
                print("\n----Incorrect input. Please just enter a single number matching the option of your choice----")
                
        while loop2 == 1:
            print("\n\n-----------------------------------------------------------\n")
            print("\nPlease choose from one of these genres:")
            
            print("\n1) Press: Reportage")
            print("2) Press: Editorial")
            print("3) Press: Reviews (theatre, books, music, dance)")
            print("4) Religion")
            print("5) Skills and Hobbies")
            print("6) Popular Lore")
            print("7) Belles Lettres, Biography, Memoirs, etc.")
            print("8) Miscelanneous")    
            print("9) Learned")
            print("10) General Fiction")
            print("11) Mystery and Detective Fiction")
            print("12) Science Fiction")
            print("13) Adventure and Western Fiction")
            print("14) Romance and Love Story")
            print("15) Humor")
    
            print("\n99) Return to previous selection screen")
            print("0) Stop and Exit")
            
            choice2 = input("Please enter your choice: ")
            if choice2 == '1':
                text = brown.words(categories='news')
                loop2 = 0
                no_of_docs = 44
                loop3 = 1
            elif choice2 == '2':
                text = brown.words(categories='editorial')
                loop2 = 0
                no_of_docs = 27
                loop3 = 1
            elif choice2 == '3':
                text = brown.words(categories='reviews')
                loop2 = 0
                no_of_docs = 17
                loop3 = 1
            elif choice2 == '4':
                text = brown.words(categories='religion')
                loop2 = 0
                no_of_docs = 17
                loop3 = 1
            elif choice2 == '5':
                text = brown.words(categories='hobbies')
                loop2 = 0
                no_of_docs = 36
                loop3 = 1
            elif choice2 == '6':
                text = brown.words(categories='lore')
                loop2 = 0
                loop3 = 1
                no_of_docs = 48
            elif choice2 == '7':
                text = brown.words(categories='belles_lettres')
                loop2 = 0
                no_of_docs = 75
                loop3 = 1
            elif choice2 == '8':
                text = brown.words(categories='government')
                loop2 = 0
                no_of_docs = 30
                loop3 = 1
            elif choice2 == '9':
                text = brown.words(categories='learned')
                loop2 = 0
                no_of_docs = 80
                loop3 = 1
            elif choice2 == '10':
                text = brown.words(categories='fiction')
                loop2 = 0
                no_of_docs = 29
                loop3 = 1
            elif choice2 == '11':
                text = brown.words(categories='mystery')
                loop2 = 0
                no_of_docs = 24
                loop3 = 1
            elif choice2 == '12':
                text = brown.words(categories='science_fiction')
                loop2 = 0
                no_of_docs = 6
                loop3 = 1
            elif choice2 == '13':
                text = brown.words(categories='adventure')
                loop2 = 0
                no_of_docs = 29
                loop3 = 1
            elif choice2 == '14':
                text = brown.words(categories='romance')
                loop2 = 0
                no_of_docs = 29
                loop3 = 1
            elif choice2 == '15':
                text = brown.words(categories='humor')
                loop2 = 0
                no_of_docs = 9
                loop3 = 1
            elif choice2 == '99':
                print("\n----Returned to the main menu.----")
                loop2 = 0
                loop = 1
            elif choice2 == '0':
                sys.exit("\nProgram is stopping. Thank you for using this program.")
            else:
                print("\n----Incorrect input. Please just enter a single number matching the option of your choice----")
            
        while loop2 == 2:
            print("\n\n-----------------------------------------------------------\n")
            print("\nPlease choose the genre from which you wish to select a text:")
            
            print("\n1) Press: Reportage")
            print("2) Press: Editorial")
            print("3) Press: Reviews (theatre, books, music, dance)")
            print("4) Religion")
            print("5) Skills and Hobbies")
            print("6) Popular Lore")
            print("7) Belles Lettres, Biography, Memoirs, etc.")
            print("8) Miscelanneous")    
            print("9) Learned")
            print("10) General Fiction")
            print("11) Mystery and Detective Fiction")
            print("12) Science Fiction")
            print("13) Adventure and Western Fiction")
            print("14) Romance and Love Story")
            print("15) Humor")
    
            print("\n99) Return to previous selection screen")
            print("0) Stop and Exit")
            
            choice2 = input("Please enter your choice: ")
            if choice2 == '1':
                loop4 = 1
                while loop4 == 1:
                    print("\n\n-----------------------------------------------------------\n")
                    print("\nPress: Reportage - Please select the text:")
                    
                    print("\n1) Atlanta Constitution, Political Reportage - 2) Dallas Morning News, Political Reportage")
                    print("3) Chicago Tribune, Political Reportage - 4) Christian Science Monitor, Political Reportage")
                    print("5) Providence Journal, Political Reportage - 6) Newark Evening News, Political Reportage")
                    print("7) New York Times, Political Reportage - 8) Times-Picayune, New Orleans, Political Reportage")
                    print("9) Philadelphia Inquirer, Political Reportage - 10) Oregonian, Portland, Political Reportage")
                    print("11) Sun, Baltimore, Sports Reportage - 12) Dallas Morning News, Sports Reportage")
                    print("13) Rocky Mountain News, Sports Reportage - 14) New York Times, Sports Reportage.")
                    print("15) St. Louis Post-Dispatch, Sports Reportage - 16) Chicago Tribune, Society Reportage")
                    print("17) Rocky Mountain News, Society Reportage - 18) Philadelphia Inquirer, Society Reportage")
                    print("19) Sun, Baltimore, Spot News - 20) Chicago Tribune, Spot News")
                    print("21) Detroit News, Spot News - 22) Atlanta Constitution, Spot News")
                    print("23) Oregonian, Portland, Spot News - 24) 	Providence Journal, Spot News")
                    print("25) San Francisco Chronicle, Spot News - 26) Dallas Morning News, Financial Reportage")
                    print("27) Los Angeles Times, Financial Reportage - 28) Wall Street Journal, Financial Reportage")
                    print("29) Dallas Morning News, Cultural Reportage - 30) Los Angeles Times, Cultural")
                    print("31) Miami Herald, Cultural Reportage - 32) San Francisco Chronicle, Cultural Reportage")
                    print("33) Washington Post, Cultural Reportage - 34) New York Times, News of the Week in Review")
                    print("35) James J. Maguire, A Family Affair - 36) William Gomberg Unions and the Anti-Trust Laws")
                    print("37) Time National Affairs - 38) Sports Illustrated, A Duel Golfers Will Never Forget")
                    print("39) Newsweek, Sports - 40) Time, People. Art & Education")
                    print("41) Robert Wallace, This Is The Way It Came About - 42) Newsweek, National Affairs")
                    print("43) U. S. News & World Report - Better Times for Turnpikes - 44) Saturday Review")
                    
                    print("\n99) Return to the previous genre selection screen")
                    print("0) Stop and Exit")
    
                    choice3 = int(input("Please select your text: "))
                    if 1 <= choice3 <= 44:
                        if 1 <= choice3 <= 9:
                            file = 'ca0' + str(choice3)
                            text = brown.words(fileids=[file])
                        elif 10 <= choice3 <= 44:
                            file = 'ca' + str(choice3)
                            text = brown.words(fileids=[file])
                        loop3 = 1
                        loop2 = 0
                        loop4 = 0
                    elif choice3 == 99:
                        print("\n----Returned to the previous menu.----")
                        loop4 = 0
                        loop2 = 2
                    elif choice3 == 0:
                        sys.exit("\nProgram is stopping. Thank you for using this program.")
                    else:
                        print("\n----Incorrect input. Please just enter a single number matching the option of your choice----")
                    no_of_docs = 1
            elif choice2 == '2':
                loop4 = 2
                while loop4 == 2:
                    print("\n\n-----------------------------------------------------------\n")
                    print("\nPress: Editorial - Please select the text:")
                    
                    print("\n1) Atlanta Constitution, Editorials - 2) Christian Science, Monitor Editorials")
                    print("3) Detroit News, Editorials - 4) Miami Herald, Editorials")
                    print("5) Newark Evening News, Editorials - 6) St. Louis Post-Dispatch, Editorials")
                    print("7) New York Times, Editorials - 8) Atlanta Constitution, Columns")
                    print("9) Christian Science Monitor, Columns - 10) Sun. Baltimore, Columns")
                    print("11) Los Angeles Times, Columns - 12) Newark Evening News, Columns")
                    print("13) Times-Picayune, New Orleans, Columns - 14) Atlanta Constitution, Columns")
                    print("15) Providence Journal, Letters to the Editor - 16) Chicago Tribune, Voice of the People")
                    print("17) Newark Evening News, What Readers Have to Say - 18) New York Times, Letters to the Times")
                    print("19) Philadelphia Inquirer, The Voice of the People - 20) Nation, Editorials")
                    print("21) Gerald W. Johnson, The Cult of the Motor Car - 22) Commonweal, Week by Week")
                    print("23) William F. Buckley, Jr., We Shall Return - 24) Time, Reviews")
                    print("25) Alexander Werth, Walkout in Moscow - 26) National Review, To the Editor")
                    print("27) Saturday Review, Letters to the Editor")

                    print("\n99) Return to the previous genre selection screen")
                    print("0) Stop and Exit")
    
                    choice3 = int(input("Please select your text: "))
                    if 1 <= choice3 <= 27:
                        if 1 <= choice3 <= 9:
                            file = 'cb0' + str(choice3)
                            text = brown.words(fileids=[file])
                        elif 10 <= choice3 <= 27:
                            file = 'cb' + str(choice3)
                            text = brown.words(fileids=[file])
                        loop3 = 1
                        loop2 = 0
                        loop4 = 0
                    elif choice3 == 99:
                        print("\n----Returned to the previous menu.----")
                        loop4 = 0
                        loop2 = 2
                    elif choice3 == 0:
                        sys.exit("\nProgram is stopping. Thank you for using this program.")
                    else:
                        print("\n----Incorrect input. Please just enter a single number matching the option of your choice----")
                    no_of_docs = 1
    
            elif choice2 == '3':
                loop4 = 3
                while loop4 == 3:
                    print("\n\n-----------------------------------------------------------\n")
                    print("\nPress: Reviews - Please select the text:")
                    
                    print("\n1) Chicago Daily Tribune, Reviews - 2) Christian Science Monitor, Reviews")
                    print("3) New York Times, Reviews - 4) Providence Journal, Reviews")
                    print("5) Christian Science Monitor, Reviews - 6) Wall Street Journals, Reviews")
                    print("7) New York Times, Reviews - 8) Providence Journal, Reviews")
                    print("9) New York Times, Reviews - 10) Providence Journal, Reviews")
                    print("11) New York Times, Reviews - 12) Christian Science Monitor, Reviews")
                    print("13) Wall Street Journal, Reviews - 14) New York Times, Reviews")
                    print("15) Life, Reviews - 16) Saturday Review, Reviews")
                    print("17) Time, Reviews")
    
                    print("\n99) Return to the previous genre selection screen")
                    print("0) Stop and Exit")
    
                    choice3 = int(input("Please select your text: "))
                    if 1 <= choice3 <= 17:
                        if 1 <= choice3 <= 9:
                            file = 'cc0' + str(choice3)
                            text = brown.words(fileids=[file])
                        elif 10 <= choice3 <= 17:
                            file = 'cc' + str(choice3)
                            text = brown.words(fileids=[file])
                        loop3 = 1
                        loop2 = 0
                        loop4 = 0
                    elif choice3 == 99:
                        print("\n----Returned to the previous menu.----")
                        loop4 = 0
                        loop2 = 2
                    elif choice3 == 0:
                        sys.exit("\nProgram is stopping. Thank you for using this program.")
                    else:
                        print("\n----Incorrect input. Please just enter a single number matching the option of your choice----")
                    no_of_docs = 1

            elif choice2 == '4':
                loop4 = 4
                while loop4 == 4:
                    print("\n\n-----------------------------------------------------------\n")
                    print("\nReligion: Please select the text:")
                    
                    print("\n1) William Pollard, Physicist and Christian - 2) Schubert Ogden, Christ Without Myth")
                    print("3) Edward E. Kelly, Christian Unity in England - 4) Jaroslav Pelikan, The Shape of Death")
                    print("5) Perry Miller, Theodore Parker: Apostasy With in Liberalism - 6) A Howard Kelly, Out of Doubt into Faith")
                    print("7) Peter Eldersveld, Faith Amid Fear - 8) Schuyler Cammann, The Magic Square of Three")
                    print("9) Eugene E. Golay, Organizing the Local Church - 10) Huston Smith, Interfaith Communication: The Contemporary Scene")
                    print("11) Paul Ramsey, War & the Christian Conscience - 12) Kenneth Underwood and Widen Jacobson, Probing the Ethics of Realtors")
                    print("13) Donald H. Andrews, The New Science & the New Faith - 14) Kenneth S. Latourette, Christianity in a Revolutionary Age")
                    print("15) Ernest Becker, Zen: A Rational critique - 16) Anonymous, What the Holy Catholic Bible Teach")
                    print("17) Anonymous, Guideposts: 15th Anniversary Issue")
        
                    print("\n99) Return to the previous genre selection screen")
                    print("0) Stop and Exit")

                    choice3 = int(input("Please select your text: "))
                    if 1 <= choice3 <= 17:
                        if 1 <= choice3 <= 9:
                            file = 'cd0' + str(choice3)
                            text = brown.words(fileids=[file])
                        elif 10 <= choice3 <= 17:
                            file = 'cd' + str(choice3)
                            text = brown.words(fileids=[file])
                        loop3 = 1
                        loop2 = 0
                        loop4 = 0
                    elif choice3 == 99:
                        print("\n----Returned to the previous menu.----")
                        loop4 = 0
                        loop2 = 2
                    elif choice3 == 0:
                        sys.exit("\nProgram is stopping. Thank you for using this program.")
                    else:
                        print("\n----Incorrect input. Please just enter a single number matching the option of your choice----")
                    no_of_docs = 1
    
            elif choice2 == '5':
                loop4 = 5
                while loop4 == 5:
                    print("\n\n-----------------------------------------------------------\n")
                    print("\nSkills and Hobbies - Please select the text:")
                    
                    print("\n1) Ben Welder, Henri de Courcy: Jr. Mr. Canada - 2) Dorothy Schroeder, Plant a Carpet of Bloom")
                    print("3) D. F. Martin, Will Aircraft or Missiles Win Wars? - 4) Harris Goldsmith, The Schnabel Pro Arte Trout")
                    print("5) Paul Nigro, The Younger Generation - 6) Joseph E. Choate, The American Boating Scene")
                    print("7) Paul Larson and Gordon Odegard, How to Design Your Interlocking Frame - 8) Don Francisco, Formulas and Math Every Hot Rodder Should Know")
                    print("9) Don McMahan, The Week at Ben White Raceway - 10) Larry Koller, The New Guns of 61")
                    print("11) Idwal Jones, Santa Cruz Run - 12) Julia Newman, Travel and Camera USA")
                    print("13) Robert Deardorff, Step by Step through Istanbul - 14) Ann Carnahan, Nick Manero's Cook-out Barbecue Book")
                    print("15) Anonymous, Pottery from Old Molds - 16) Hal Kelly, Build Hotei")
                    print("17) Anonymous, This is the Vacation Cottage You Can Build - 18) Lura W. Watkins, The Bridge Over the Merrimac")
                    print("19) Booth Hemingway and Stuart H. Brown, How to Own a Pool and Like It - 20) Anonymous, What You Should Know About Air Conditioning")
                    print("21) Richard McCosh, Recreation Site Selection - 22) Roy Harris, Roy Harris Salutes Serge Prokofieff")
                    print("23) Norman Kent, The Watercolor Art of Roy M. Mason - 24) Bonnie Prudden, The Dancer & the Gymnast")
                    print("25) Walter Ho Buchsbaum, Advances in Medical Electronics - 26) Bern Dibner, Oersted & the Discovery of Electromagnetism")
                    print("27) Mike Bay, What Can Additives Do for Ruminants? - 28) John R. Sargent, Where to Aim Your Planning")
                    print("29) Edward A. Walton, On Education for the Interior Designer - 30) Anonymous, The Attack on Employee Services")
                    print("31) Jim Dee, Expanding Horizons - 32) E. J. Tangerman, Which Way Up. Technical or Management?")
                    print("33) Robert Gray, Fifty Houses, One Tank - 34) Anonymous, The New Look in Signs")
                    print("35) Anonymous, The Industrial Revolution in Housing - 36) Ethel Norling, Renting a Car in Europe")

                    print("\n99) Return to the previous genre selection screen")
                    print("0) Stop and Exit")
    
                    choice3 = int(input("Please select your text: "))
                    if 1 <= choice3 <= 36:
                        if 1 <= choice3 <= 9:
                            file = 'ce0' + str(choice3)
                            text = brown.words(fileids=[file])
                        elif 10 <= choice3 <= 36:
                            file = 'ce' + str(choice3)
                            text = brown.words(fileids=[file])
                        loop3 = 1
                        loop2 = 0
                        loop4 = 0
                    elif choice3 == 99:
                        print("\n----Returned to the previous menu.----")
                        loop4 = 0
                        loop2 = 2
                    elif choice3 == 0:
                        sys.exit("\nProgram is stopping. Thank you for using this program.")
                    else:
                        print("\n----Incorrect input. Please just enter a single number matching the option of your choice----")
                    no_of_docs = 1
    
            elif choice2 == '6':
                loop4 = 6
                while loop4 == 6:
                    print("\n\n-----------------------------------------------------------\n")
                    print("\nPopular Lore - Please select the text:")
                    
                    print("\n1) Rosemary Blackmon, How Much Do You Tell When You Talk? - 2) Glenn Infield, America's Secret Poison Gas Tragedy")
                    print("3) Nathan Rapport, I've Been Here Before - 4) Ruth F. Rosevear, North Country School Cares for the Whole Child")
                    print("5) Richard S. Allen, When Fogg Flew the Mail - 6) Alice Ho Austin, Let's Discuss Retirement")
                    print("7) Marvin Sentnor and Stephen Hult, How to Have a Successful Honeymoon - 8) Philip Reaves, Who Rules the Marriage Bed?")
                    print("9) David Martinson, Fantastic Life & Death of the Golden Prostitute - 10) Jack Kaplan, Therapy by Witchcraft")
                    print("11) Lillian Pompian, Tooth-Straightening Today - 12) Marian Neater, New Methods of Parapsychology")
                    print("13) Orlin J. Scoville, Part-time Farming - 14) Harold Rosenberg, The Trial and Eichmann")
                    print("15) John A. O'Brien, Let's Take Birth Control Out of Politics - 16) James, Boylan Mutiny")
                    print("17) John Harnsberger and Robert P. Wilkins, Transportation on the Northern Plains - 18) Bell I. Willy, Home Letters of Johnny Reb & Billy Yank")
                    print("19) Tristram P. Coffin, Folklore in the American Twentieth Century - 20) Kenneth Allsop, The Bootleggers and Their Era")
                    print("21) Joseph Bernstein, Giant Waves - 22) Booton Herndon, From Custer to Korea, the 7th Cavalry")
                    print("23) Barry Goldwater, A Foreign Policy for America - 24) Peter J. White, Report on Laos")
                    print("25) David Boroff, Jewish Teen-Age Culture - 26) Amy Lathrop, Pioneer Remedies from Western Kansas")
                    print("27) Creighton Churchill, A Notebook for the Wines of France - 28) Frank O. Gatell, Doctor Palfrey Frees His Slaves")
                    print("29) Douglass Cater, The Kennedy Look in the Arts - 30) Frederic A. Birmingham, The Ivy League Today")
                    print("31) Edward Do Radin, Lizzie Borden: The Untold Story - 32) Florence M. Read, The Story of Spelman College")
                    print("33) James Be Conant, Slurs and Suburbs - 34) Frederic R. Senti and W. Dayton Maclay, Age-old uses of Seeds and Some New Ones")
                    print("35) Ramon F. Adams, The Old-time Cowhand - 36) Robert Easton and Mackenzie Brown, Lord of Beasts")
                    print("37) Samuel M. Cavert, On the Road to Christian Unity - 38) Robert Smith, Baseball in America")
                    print("39) Clark E. Vincent, Unmarried mothers - 40) William Greenleaf, Monopoly on Wheels")
                    print("41) George W. Oakes, Turn Right at the Fountain - 42) James Baldwin, Nobody Knows My Name")
                    print("43) Frank Getlein and Harold C. Gardiner, Movies, Morals, and Art - 44) Gibson Winter, The Suburban Captivity of the Churches")
                    print("45) Paul C. Phillips, The Fur Trade - 46) Russell Baker, An American in Washington")
                    print("47) Clara L. Simerville, Home Visits Abroad - 48) Paul Ramsey, Christian Ethics & the Sit-In")
                   
                    print("\n99) Return to the previous genre selection screen")
                    print("0) Stop and Exit")

                    choice3 = int(input("Please select your text: "))
                    if 1 <= choice3 <= 48:
                        if 1 <= choice3 <= 9:
                            file = 'cf0' + str(choice3)
                            text = brown.words(fileids=[file])
                        elif 10 <= choice3 <= 48:
                            file = 'cf' + str(choice3)
                            text = brown.words(fileids=[file])
                        loop3 = 1
                        loop2 = 0
                        loop4 = 0
                    elif choice3 == 99:
                        print("\n----Returned to the previous menu.----")
                        loop4 = 0
                        loop2 = 2
                    elif choice3 == 0:
                        sys.exit("\nProgram is stopping. Thank you for using this program.")
                    else:
                        print("\n----Incorrect input. Please just enter a single number matching the option of your choice----")
                    no_of_docs = 1
    
            elif choice2 == '7':
                loop4 = 7
                while loop4 == 7:
                    print("\n\n-----------------------------------------------------------\n")
                    print("\nBelles Lettres, Biography, Memoirs, etc. - Please select the text:")
                    
                    print("\n1) Edward P. Lawton, Northern Liberals & Southern Bourbons - 2) Arthur S. Miller, Toward a Concept of National Responsibility")
                    print("3) Peter Wyden, The Chances of Accidental War - 4) Eugene Burdick, The Invisible Aborigine")
                    print("5) Terence O'Donnell, Evenings at the Bridge - 6) Ruth Berges, William Steinberg, Pittsburgh's Dynamic Conductor")
                    print("7) Richard B. Morris, Seven Who Set Our Destiny - 8) Frank Murphy, New Southern Fiction: Urban or Agrarian?")
                    print("9) Selma J. Cohen, Avant-Garde Choreography - 10) Clarence Streit, How the Civil War Kept You Sovereign")
                    print("11) Frank Oppenheimer, Science and Fear - 12) Tom F. Driver, Beckett by the Madeleine")
                    print("13) Charles Glicksberg, Sex in Contemporary Literature - 14) Helen H. Santmeyer, There Were Fences")
                    print("15) Howard Nemerov, Themes and Methods: Early Storie of Thomas Mann - 16) John F. Hayward, Mimesis & Symbol in the Arts")
                    print("17) Randall Stewart, A Little History, a Little Honesty - 18) Charles W. Stork, Verner von Heidenstam")
                    print("19) R. F. Shaw, The Private Eye - 20) Dan McLachlan, Jr., Communication Networks & Monitoring")
                    print("21) Brainard Cheney, Christianity & the Tragic Vision - 22) Kenneth Reiner, Coping with Runaway Technology")
                    print("23) William C. Smith, Why Fear Ideas - 24) Sanchia Thayer, Personality & Moral Leadership")
                    print("25) Stanley Parry, The Restoration of Tradition - 26) Selma Fraiberg, Two Modern Incest Heroes")
                    print("27) Matthew Josephson, Jean Hélion. The Return from Abstract Art - 28) Arlin Turner, William Faulkner, Southern Novelist")
                    print("29) Anonymous, References for the Good Society - 30) Norwood R. Hanson, Copernican & Keplerian Astronomy")
                    print("31) Irving Fineman, Woman of Valor: Life of Henrietta Szold 1860-1945 - 32) Finis Farr, Frank Lloyd Wright")
                    print("33) Virgilia Peterson, A Matter of Life and Death - 34) Harry Golden, Carl Sandburg")
                    print("35) Dwight D. Eisenhower, Peace With Justice - 36) DeWitt Copp & Marshall Peck, Betrayal at the UN")
                    print("37) Gordon L. Hall, Golden Boats from Burma, 38) Bertrand A. Goldgar, The Curse of Party")
                    print("39) Edward Jablonski, Harold Arlen Happy with the Blues - 40) Gene Fowler, Skyline: A Reporter's Reminiscences of the 1920s")
                    print("41) Lillian R. Parka and Frances S. Leighton , My Thirty Years Backstairs at the White House - 42) Harold D. Lasswell, Epilogue")
                    print("43) Robert E. Lane, The Liberties of Wit - 44) Newton Stallknecht, Ideas and Literature")
                    print("45) W. A. Swanberg, Citizen Hearst: A Biography of W. R. Hearst - 46) Henry R. Winkler, George Macaulay Trevelyan")
                    print("47) Carry Davis, The World Is My Country - 48) Francis F. McKinney, Education in Violence")
                    print("49) Paul van K. Thomson, Francis Thompson, a Critical Biography - 50) Curtis C. Davis, The King's Chevalier")
                    print("51) Ilka Chase, The Carthaginian Rose - 52) Robert L. Duncan, Reluctant General")
                    print("53) Bertram Lippincott, Indians, Privateers, and High Society - 54) Mabel W. Wheaton & LeGette Blythe, Thomas Wolfe & His Family")
                    print("55) Ralph E. Flanders, Senator from Vermont, 112 - 56) Keith F. McKean, The Moral Measure of Literature")
                    print("57) Robin M. Williams, Jr., Values & Modern Education in the United States - 58) North Callahan, Daniel Morgan")
                    print("59) Esther R. Clifford, A Knight of Great Renown - 60) Gertrude Berg & Cherney Berg, Molly and Me")
                    print("61) Donald A. White, Litus Saxonicum - 62) C. H. Cramer, Newton D. Baker")
                    print("63) George Steiner, The Death of Tragedy - Mark Eccles, Shakespeare in Warwickshire")
                    print("65) Timothy P. Donovan, Henry Adams & Brooks Adams - 66) Van Wyck Brooks, From the Shadow of the Mountain")
                    print("67) Mark Schorer, Sinclair Lewis: An American Life - 68) Harris F. Fletcher, The Intellectual Development of John Milton")
                    print("69) Mark R. Hillegas, Dystopian Science Fiction - 70) Joseph W. Krutch, If You Don't Mind My Saying So")
                    print("71) Joseph Frank, André Malraux: The Image of Man - 72) J W. Fulbright, For a Concert of Free")
                    print("73) Carolyn See, The Jazz Musician as Patchen's Hero - 74) John McCormick, The Confessions of Jean Jacques Krim")
                    print("75) George Garrett, A Wreath for Garibaldi")
    
                    print("\n99) Return to the previous genre selection screen")
                    print("0) Stop and Exit")
    
                    choice3 = int(input("Please select your text: "))
                    if 1 <= choice3 <= 75:
                        if 1 <= choice3 <= 9:
                            file = 'cg0' + str(choice3)
                            text = brown.words(fileids=[file])
                        elif 10 <= choice3 <= 75:
                            file = 'cg' + str(choice3)
                            text = brown.words(fileids=[file])
                        loop3 = 1
                        loop2 = 0
                        loop4 = 0
                    elif choice3 == 99:
                        print("\n----Returned to the previous menu.----")
                        loop4 = 0
                        loop2 = 2
                    elif choice3 == 0:
                        sys.exit("\nProgram is stopping. Thank you for using this program.")
                    else:
                        print("\n----Incorrect input. Please just enter a single number matching the option of your choice----")
                    no_of_docs = 1
    
            elif choice2 == '8':
                loop4 = 8
                while loop4 == 8:
                    print("\n\n-----------------------------------------------------------\n")
                    print("\nMiscellaneous - Please select the text:")
                    
                    print("\n1) U. S Dep't of Commerce, Handbook of Federal Aids to Communities - 2) U. S. Dep't of State, An Act for International Development")
                    print("3) U. S. 87th Congress, House Document No. 487 - 4) R. I. Legislative Council, State Automobiles & Travel Allowances")
                    print("5) R. I. Leglelative Council, Taxing of Movable Tangible Property - 6) R. I. Development Council, Annual Report, 1960")
                    print("7) R. I. Legislative Council, linlform Fiscal Year for Municipalities - 8) John A. Notte, Jr., R. I. Governor's Proclamations")
                    print("9) U. S. 87th Congress, Public Laws 295, 300, 347 - 10) U. S. Dep't of Defense, Medicine in National Defense")
                    print("11) U. S. Dep't of Commerce, 1961 Reaearch Highlights, Nat'1 Bureau of Standards - 12) U. S. 87th Congress, Legislation on Foreign Rels")
                    print("13) U. S. 87th Congreas, Congressional Record: Extension of Remarks. May 2, 1961 - 14) U. S. Dep't of Health, Education & Welfare, Grants-in-Aid and Other Financial Assistance Programs")
                    print("15) U. S. Office of Civil and Defence Mobilization, The Family Fallout Shelter - 16) U. S. Reports, Cases AdJudged in the Supreme Court, October Tenm 1960")
                    print("17) U. S. Reports, Cases AdJudged in the Supreme Court, October Tenm 1959-60 - 18) Dean Rusk, The Department of State")
                    print("19) Peace Corps, Fact Book - 20) U. S. Dep't of Agriculture, Development Program for the National Forests")
                    print("21) Dwight D. Eisenhower, Public Papers, 1960-61 - 22) U. S. Dep't of State, U. S. Treatiea and Other International Agreements")
                    print("23) U. S. Federal Communications Commiasion, Pederal Communications Commission Reports - 24) U. S. Tresaury Dep't, Your Federal Income Tax")
                    print("25) Guggenheim Foundation, Report of the Secretary Gen'1 - 26) Anonymous, A Brief Background of Brown & Sharpe")
                    print("27) Robert Leeson, Leesona Corporation President's Report - 28) Carleton College, Carleton College Bulletin")
                    print("29) Sprague Electric Company, Sprague Log - 30) Carnegie Foundation, Annual Report of Year Ending June 30, 1961")
                   
                    print("\n99) Return to the previous genre selection screen")
                    print("0) Stop and Exit")
    
                    choice3 = int(input("Please select your text: "))
                    if 1 <= choice3 <= 30:
                        if 1 <= choice3 <= 9:
                            file = 'ch0' + str(choice3)
                            text = brown.words(fileids=[file])
                        elif 10 <= choice3 <= 30:
                            file = 'ch' + str(choice3)
                            text = brown.words(fileids=[file])
                        loop3 = 1
                        loop2 = 0
                        loop4 = 0
                    elif choice3 == 99:
                        print("\n----Returned to the previous menu.----")
                        loop4 = 0
                        loop2 = 2
                    elif choice3 == 0:
                        sys.exit("\nProgram is stopping. Thank you for using this program.")
                    else:
                        print("\n----Incorrect input. Please just enter a single number matching the option of your choice----")
                    no_of_docs = 1
    
            elif choice2 == '9':
                loop4 = 9
                while loop4 == 9:
                    print("\n\n-----------------------------------------------------------\n")
                    print("\nLearned - Please select the text:")
                    
                    print("\n1) Cornell H. Mayer, Radio. Emission of the Moon and Planets - 2) R. C. Binder et al., 1961 Heat Transfer & Fluid Mechanics Institute")
                    print("3) Harry H. Hull, Normal Forces & Their Thermodynamic Significance - 4) James A. Ibers et al., Proton Magnetic Resonance Study")
                    print("5) John R. Van Wazer, ed., Phosphorus and Its Compounds - 6) Francis J. Johnston & John E. Willard, Exchange Reaction Between C12 and CC14")
                    print("7) J. F. Vedder, Micrometeorites - 8) LeRoy Fothergill, Biological Warfare")
                    print("9) M. Yokayama et al., Chemical & Serological Characteristics - 10) B. J. D. Meeuse, The Story of Pollination")
                    print("11) Clifford H Pope, The Ciant Snakes - 12) Richard F McLaughlin et al., A Study of the Subgross Pulmonary Anatomy")
                    print("13) S. Idell Pyle et al., Onsets, Completions & Spans - 14) Jacob Robbins et al., The Thyroid-Stimulating Hormone")
                    print("15) J. W. C. Hagstrom et. al., Debilitating Muscular Weakness - 16) A. N. Nagaraj & L. M. Black, Localization of Wound-Tumor Virus Antigen")
                    print("17) E. Gellhorn, Prolegomena to a Theory of the Emotions - 18) Kenneth Hoffman & Ray Kunze, Linear Algebra")
                    print("19) Frederick Mosteller et al., Probability with Statistical Applications - 20) R. P. Jerrard, Inscribed Squares in Plane Curves")
                    print("21) C. R. Wylie, Jr., Line Involutions in S3 - 22) Max F. Millikan & Donald L. Blackmer, editors, The Emerging Nations")
                    print("23) Joyce O. Hertzler, American Social Institutions - 24) Howard J. Parad, Preventive Casework: Problems & Implications")
                    print("25) Sister Claire M. Sawyer, Some Aspects of Fertility of a Tri-Racial Isolate - 26) Frank Lorimer, Demographic Information on Tropical Africa")
                    print("27) Dale L. Womble, Functional Marriage Course for the Already Married - 28) William H. Ittelson & Samuel B. Kutash, editors, Perceptual Changes in Psychopathology")
                    print("29) Jesse W. Grimes & Wesley Allinsmith, Compulsivity, Anxiety & School Achievement - 30) Raymond J. Corsini, Roleplaying in Business & Industry")
                    print("31) Harold Searles, Schizophrenic Communication - 32) Hugh Kelly & Ted Ziehe, Glossary Lookup Made Easy")
                    print("33) Ralph Bc Long, The Sentence & Tts Parts - 34) H.A. Cleason	Review of African Language Studies")
                    print("35) A. T. Kroeber, Semantic Contribution of Lexicostatistics - 36) D. F. Fleming, The Cold War & Its Origins")
                    print("37) Douglas Ashford, Elections' in Morocco: Progress or Confusion - 38) Committee for Economic Development, Distressed Areas in a Growing Economy")
                    print("39) William O'Connor, Stocks, Wheat & Pharaohs - 40) James J. O'Leary, The outlook for Interest Rates in 1961")
                    print("41) Allan J. Braff & Roger F. Miller, Wage-Price Policies Under Public Pressure - 42) Morton A. Kaplan ~ Nicholas Katzenbach, The Political Foundation of Internationa1 Law")
                    print("43) Wallace Mendelson, Justices Black & Frankfurter - 44) J. Mitchell Reese, Jr., Reorganization Transfers")
                    print("45) Albert Schreiber et al., Defense Procurement & Small Business - 46) Irving Perluss, Agricultural Labor Disputes in California 1960")
                    print("47) William S. Ragan, Teaching America's Children - 48) Paul Cooke, Desegregated Education in the Middle-South Region")
                    print("49) Robert J. Havighurst, Social-Class Influences on American Education - 50) James C. Bonbright, Principles of Public Utility Rates")
                    print("51) Irving L. Horowitz, Philosophy, Science & the Sociology of Knowledge - 52) Brand Blanshard, The Emotive Theory")
                    print("53) William S. Haymond, Is Distance an Original Factor in Vision? - 54) Chester G. Starr, The Origins of Greek Civilization 1100-650 B.C.")
                    print("55) Jim B. Pearson, The Maxwell Land Grant - 56) Edwin L. Bigelow & Nancy H. Otis, Manchester, Vermont, A Pleasant Land")
                    print("57) J. H. Hexter	Thomas, More: on the Margins of Modernity - 58) John M. Ray, Rhode Island's Reactions to John Brown's Raid")
                    print("59) Clement Greenberg, Collage - 60) Robert A. Futterman, The Future of Our Cities")
                    print("61) Allyn Cox, Completing & Restoring the Capitol Frescos - 62) Jimmy Ernst, A Letter to Artists of the Soviet Union")
                    print("63) John H. Schaar, Escape from Authority, Perspectives of Erich Fromm - 64) Katherine G. McDonald, Figures of Rebellion")
                    print("65) Samuel Hynes, The Pattern of Hardy's Poetry - 66) Kenneth Rexroth, Disengagament: The Art of the Beat Generation")
                    print("67) William Whallon, The Diction of Beowulf - 68) Charles R. Forker, The Language of Hands in Great Expectations")
                    print("69) I. B. M. Corporation, IBM 7070, Autocoder Reference Manual - 70) Ross E. McKinney & Howard Edde, Aerated Lagoon for Suburban Sewage Disposal")
                    print("71) Thomas D. McGrath, Submarine Defense - 72) Mellon Institute, Annual Report; 1960, Independent Research")
                    print("73) Nat'l Research Council, Directory of Continuing Numerical Data Projects - 74) Harlan W. Nelson, Food Preservation by Ionizing Radiation")
                    print("75) W. K. Asbeck, Forces in Coatings Removal Knife Cutting Method - 76) Joel Frados, editor, Survey of Foamed Plastics")
                    print("77) William D. Appel, editor, 1961 Technical Manual of American Ass'n of Textile Chemists & Colorists - 78) Paul J. Dolon & Wilfrid F. Niklas, Gain & Resolution of Fiber Optic Intensifier")
                    print("79) Rutherford Aris, The O'ptim.A1 Design of Chemical Reactors - 80) C. J. Savant Jr. & R. C. Howard, Principles of Inertial Navigation")

                    print("\n99) Return to the previous genre selection screen")
                    print("0) Stop and Exit")
    
                    choice3 = int(input("Please select your text: "))
                    if 1 <= choice3 <= 80:
                        if 1 <= choice3 <= 9:
                            file = 'cj0' + str(choice3)
                            text = brown.words(fileids=[file])
                        elif 10 <= choice3 <= 80:
                            file = 'cj' + str(choice3)
                            text = brown.words(fileids=[file])
                        loop3 = 1
                        loop2 = 0
                        loop4 = 0
                    elif choice3 == 99:
                        print("\n----Returned to the previous menu.----")
                        loop4 = 0
                        loop2 = 2
                    elif choice3 == 0:
                        sys.exit("\nProgram is stopping. Thank you for using this program.")
                    else:
                        print("\n----Incorrect input. Please just enter a single number matching the option of your choice----")
                    no_of_docs = 1
    
            elif choice2 == '10':
                loop4 = 10
                while loop4 == 10:
                    print("\n\n-----------------------------------------------------------\n")
                    print("\nGeneral Fiction - Please select the text:")
                    
                    print("\n1) Christopher Davis, First Family - 2) Clayton C. Barbeau, The Ikon")
                    print("3) Tristram Coffin, Not to the Swift - 4) W. E. B. Du Bois, Worlds of Color")
                    print("5) David Stacton, The Judges of the Secret Court - 6) Louis Zara, Dark Rider")
                    print("7) Francis Pollini, Night - 8) Guy Endore, Voltaire! Voltaire!")
                    print("9) Howard Fast, April Morning - 10) Gladys H. Barr, The Master of & Geneva")
                    print("11) Robert Penn Warren, Wilderness - 12) Gerald Green, The Heartless Light")
                    print("13) William Maxwell, The Chateau - 14) Irving Stone, The Agony & the Ecstasy")
                    print("15) Ann Hebson, The Lattimer Legend - 16) Stephen Longstreet, Eagles Where I Walk")
                    print("17) Leon Uris, Mila 8 - 18) John Dos Passos, Midcentury")
                    print("19) Robert J Duncan, The Voice of Strangers - 20) Guy Bolton, The Olympians")
                    print("21) Bruce Palmer, My Brother's Keeper - 22) John Cheever, The Brigadier & the Golf Widow")
                    print("23) Prieda Arkin, The Tight of the Sea - 24) W. H. Gass, The Pedersen Kid")
                    print("25) Arthur Miller, The Prophecy - 26) Jane G. Rushing, Against the Moon")
                    print("27) E. Lucas Myers, The Vindication of Dr. Nestor - 28) Sallie Bingham, Moving Day")
                    print("29) Marvin Schiller, The Sheep's in the Meadow")
    
                    print("\n99) Return to the previous genre selection screen")
                    print("0) Stop and Exit")
    
                    choice3 = int(input("Please select your text: "))
                    if 1 <= choice3 <= 29:
                        if 1 <= choice3 <= 9:
                            file = 'ck0' + str(choice3)
                            text = brown.words(fileids=[file])
                        elif 10 <= choice3 <= 29:
                            file = 'ck' + str(choice3)
                            text = brown.words(fileids=[file])
                        loop3 = 1
                        loop2 = 0
                        loop4 = 0
                    elif choice3 == 99:
                        print("\n----Returned to the previous menu.----")
                        loop4 = 0
                        loop2 = 2
                    elif choice3 == 0:
                        sys.exit("\nProgram is stopping. Thank you for using this program.")
                    else:
                        print("\n----Incorrect input. Please just enter a single number matching the option of your choice----")
                    no_of_docs = 1    

            elif choice2 == '11':
                loop4 = 11
                while loop4 == 11:
                    print("\n\n-----------------------------------------------------------\n")
                    print("\nMystery and Detective Fiction - Please select the text:")
                    
                    print("\n1) Winfred Van Atta, Shock Treatment - 2) A. A. Fair, Bachelors Get Lonely")
                    print("3) Amber Dean, Encounter With Evil - 4) David Alexander, Bloodstain")
                    print("5) Brett Halliday, The Careless Corpse - 6) Thomas B. Dewey, Hunter at Large")
                    print("7) Genevieve Golden, Deadlier Than the Male - 8) Dell Shannon, The Ace of Spades")
                    print("9) Mignon G. Eberhart, The Cup, the Blade or the Swords - 10) Harry Bleaker, Impact")
                    print("11) Hampton Stone, The Man Who Looked Death in the Eye - 12) Whit Masterson, Evil Come, Evil Go")
                    print("13) Dolores Hitchens, Footsteps in the Night - 14) Frances & Richard Lockridge, Murder Has Its Points")
                    print("15) Doris M. Disney, Mrs. Meeker's Money - 16) Alex Gordon, The Cipher")
                    print("17) Brent James, Night of the Kill - 18) George H. Coxe, Error of Judgment")
                    print("19) Brad Williams, Make a Killing - 20) Ed Lacy, Death by the Numbers")
                    print("21) Helen McCloy, The Black Disk - 22) S. L. M. Barlow, Monologue of Murder")
                    print("23) J. W. Rose, Try My Sample Murders - 24) Fredric Brown, The Murders")
    
                    print("\n99) Return to the previous genre selection screen")
                    print("0) Stop and Exit")
    
                    choice3 = int(input("Please select your text: "))
                    if 1 <= choice3 <= 24:
                        if 1 <= choice3 <= 9:
                            file = 'cl0' + str(choice3)
                            text = brown.words(fileids=[file])
                        elif 10 <= choice3 <= 24:
                            file = 'cl' + str(choice3)
                            text = brown.words(fileids=[file])
                        loop3 = 1
                        loop2 = 0
                        loop4 = 0
                    elif choice3 == 99:
                        print("\n----Returned to the previous menu.----")
                        loop4 = 0
                        loop2 = 2
                    elif choice3 == 0:
                        sys.exit("\nProgram is stopping. Thank you for using this program.")
                    else:
                        print("\n----Incorrect input. Please just enter a single number matching the option of your choice----")
                    no_of_docs = 1   
    
            elif choice2 == '12':
                loop4 = 12
                while loop4 == 12:
                    print("\n\n-----------------------------------------------------------\n")
                    print("\nScience FictionPlease select the text:")
                    
                    print("\n1) Robert Heinlein, Stranger in a Strange Land - 2) Philip J. Farmer, The Lovers")
                    print("3) James Blish, The Star Dwellers - 4) Jim Harmon, The Planet with No Nightmare")
                    print("5) Anne McCaffrey, The Ship Who Sang - 6) Cordwainer Smith, A Planet Named Shayol")

                    print("\n99) Return to the previous genre selection screen")
                    print("0) Stop and Exit")
    
                    choice3 = int(input("Please select your text: "))
                    if 1 <= choice3 <= 6:
                        file = 'cm0' + str(choice3)
                        text = brown.words(fileids=[file])
                        loop3 = 1
                        loop2 = 0
                        loop4 = 0
                    elif choice3 == 99:
                        print("\n----Returned to the previous menu.----")
                        loop4 = 0
                        loop2 = 2
                    elif choice3 == 0:
                        sys.exit("\nProgram is stopping. Thank you for using this program.")
                    else:
                        print("\n----Incorrect input. Please just enter a single number matching the option of your choice----")
                    no_of_docs = 1   
    
            elif choice2 == '13':
                loop4 = 13
                while loop4 == 13:
                    print("\n\n-----------------------------------------------------------\n")
                    print("\nAdventure and Western Fiction - Please select the text:")
                    
                    print("\n1) Wayne D. Overholser, The Killer Marshall - 2) Clifford Irving, The Valley")
                    print("3) Cliff Farrell, The Trail of the Tattered Star - 4) James D. Horan, The Shadow Catcher")
                    print("5) Richard Ferber, Bitter Valley - 6) Thomas Anderson, Here Comes Pete Now")
                    print("7) Todhunter Ballard, The Night Riders - 8) Mary Savage, Just for Tonight")
                    print("9) Jim Thompson, The Transgressors - 10) Joseph Chadwick, No Land Is Free")
                    print("11) Gene Caesar, Rifle for Rent - 12) Edwin Booth, Outlaw Town")
                    print("13) Martha F. McKeown, Mountains Ahead - 14) Peter Field, Rattlesnake Ridge")
                    print("15) Donald J. Plantz, Sweeney Squadron - 16) Ralph J. Salisbury, On the Old Sante Fe Trail to Siberia")
                    print("17) Richard S. Prather, The Bawdy Beautiful - 18) Peter Bains, With Women Education Pays off")
                    print("19) David Jackson, The English Gardens - 20) T. C. McClary, The Flooded Dearest")
                    print("21) C. T. Sommers, The Beautiful Mankillers of Eromonga - 22) Gordon Johnson, A Matter of Curiosity.")
                    print("23) Wheeler Hall, Always Shoot to Kill - 24) T. K. Brown III, The Fifteenth Station")
                    print("25) Wesley Newton, Aid & Comfort to the Enemy - 26) Paul Brock, Toughest Lawman in the Old West")
                    print("27) James Hines & James Morris, Just Any Girl - 28) Ralph Grimshaw, Mrs. Hacksaw, New Orleans Society Killer")
                    print("29) Harlan Ellison, Riding the Dark Train Out")

                    print("\n99) Return to the previous genre selection screen")
                    print("0) Stop and Exit")
    
                    choice3 = int(input("Please select your text: "))
                    if 1 <= choice3 <= 29:
                        if 1 <= choice3 <= 9:
                            file = 'cn0' + str(choice3)
                            text = brown.words(fileids=[file])
                        elif 10 <= choice3 <= 29:
                            file = 'cn' + str(choice3)
                            text = brown.words(fileids=[file])
                        loop3 = 1
                        loop2 = 0
                        loop4 = 0
                    elif choice3 == 99:
                        print("\n----Returned to the previous menu.----")
                        loop4 = 0
                        loop2 = 2
                    elif choice3 == 0:
                        sys.exit("\nProgram is stopping. Thank you for using this program.")
                    else:
                        print("\n----Incorrect input. Please just enter a single number matching the option of your choice----")
                    no_of_docs = 1   
    
            elif choice2 == '14':
                loop4 = 14
                while loop4 == 14:
                    print("\n\n-----------------------------------------------------------\n")
                    print("\nRomance and Love Story - Please select the text:")
                    
                    print("\n1) Octavia Waldo, A Cup of the Sun - 2) Ann Ritner, Seize a Nettle")
                    print("3) Clark McMeekin, The Fairbrothers - 4) B. J. Chute, The Moon & the Thorn")
                    print("5) Allan R. Bosworth, The Crows of Edwina Hill - 6) Richard Tiernan, Land of the Silver Dollar")
                    print("7) Vina Delmar, The Big Family - 8) R. Leslie Course, With Gall & Honey")
                    print("9) Jesse Hill Ford, Mountains of Gilead - 10) Jay Williams, The Forger")
                    print("11) Bessie Breuer, Take Care of My Roses - 12) Morley Callaghan, A Passion in Rome")
                    print("13) Frank B. Hanes, The Fleet Rabble - 14) Frank B. Hanes, The Fleet Rabble")
                    print("15) Loretta Burrough, The Open Door - 16) Margery F. Brown, A Secret Between Friends")
                    print("17) Al Hine, The Huntress - 18) Anonymous, No Room in My Heart to For Give")
                    print("19) Anonymous, This Cancer Victim May Ruin My Life - 20) Spencer Norris, Dirty Dog Inn")
                    print("21) Elizabeth Spencer, The White Azalea - 22) Anonymous, A Husband Stealer from Way Back")
                    print("23) Barbara Robinson, Something Very Much in Common - 24) Samuel Elkin, The Ball Player")
                    print("25) William Butler, The Pool at Ryusenji - 26) Ervin D. Krause, The Snake")
                    print("27) Lee McGiffin, Measure of a Man - 28) Carol Hoover, The Shorts on the Bedroom Floor")
                    print("29) Robert Carson, My Hero")

                    print("\n99) Return to the previous genre selection screen")
                    print("0) Stop and Exit")
    
                    choice3 = int(input("Please select your text: "))
                    if 1 <= choice3 <= 29:
                        if 1 <= choice3 <= 9:
                            file = 'cp0' + str(choice3)
                            text = brown.words(fileids=[file])
                        elif 10 <= choice3 <= 29:
                            file = 'cp' + str(choice3)
                            text = brown.words(fileids=[file])
                        loop3 = 1
                        loop2 = 0
                        loop4 = 0
                    elif choice3 == 99:
                        print("\n----Returned to the previous menu.----")
                        loop4 = 0
                        loop2 = 2
                    elif choice3 == 0:
                        sys.exit("\nProgram is stopping. Thank you for using this program.")
                    else:
                        print("\n----Incorrect input. Please just enter a single number matching the option of your choice----")
                    no_of_docs = 1   
    
            elif choice2 == '15':
                loop4 = 15
                while loop4 == 15:
                    print("\n\n-----------------------------------------------------------\n")
                    print("\nHumor - Please select the text:")
                    
                    print("\n1) Anita Loos, No Mother to Guide Her - 2) Jean Mercier, Whatever You Do, Don't Panic")
                    print("3) Patrick Dennis, Little Me - 4) Edward Streeter, The Chairman of the Bored")
                    print("5) Evan Esar, Humorous English - 6) James Thurber, The Future, If Any, of Comedy")
                    print("7) John H. Wildman, Take It Off - 8) Leo Lemon, Catch Up With & Something to Talk About")
                    print("9) S. J. Perelman, The Rising Gorge")

                    print("\n99) Return to the previous genre selection screen")
                    print("0) Stop and Exit")
    
                    choice3 = int(input("Please select your text: "))
                    if 1 <= choice3 <= 9:
                        file = 'ck0' + str(choice3)
                        text = brown.words(fileids=[file])
                        loop3 = 1
                        loop2 = 0
                        loop4 = 0
                    elif choice3 == 99:
                        print("\n----Returned to the previous menu.----")
                        loop4 = 0
                        loop2 = 2
                    elif choice3 == 0:
                        sys.exit("\nProgram is stopping. Thank you for using this program.")
                    else:
                        print("\n----Incorrect input. Please just enter a single number matching the option of your choice----")
                    no_of_docs = 1   
    
            elif choice2 == '99':
                print("\n----Returned to the main menu.----")
                loop2 = 0
                loop = 1
            elif choice2 == '0':
                sys.exit("\nProgram is stopping. Thank you for using this program.")
            else:
                print("\n----Incorrect input. Please just enter a single number matching the option of your choice----")
               
        while loop2 == 3:
            print("\n\n-----------------------------------------------------------\n")
            print("\nPlease enter the name and the extension of the textfile that you wish to analyse, e.g. 'filename.txt'. Please ensure that it is indeed a .txt file and that it is located in the same folder as the program's Python file, as this program will otherwise not find the file.")
            print("\nOr enter either of these two options:")
            print("99) Return to the previous menu")
            print("0) Stop and Exit.")
            
            textfile = input("\nEnter your filename here: ")
            if re.search(".txt", textfile):
                text = open(textfile, 'r')
                text = text.read().split()
                text = np.array(text)
                text = text.tolist()
                for w in text:
                    if w not in removal:
                        text2 = text2 + [w]
                read_text = [w.lower() for w in text2]
                data = np.array(read_text)
                no_of_docs = 1
                loop2 = 0
                loop = 0
                loop4 = 1
                main_loop = 2
            elif textfile == '99':
                print("\n----Returned to the main menu.----")
                loop2 = 0
                loop = 1
            elif textfile == '0':
                sys.exit("\nProgram is stopping. Thank you for using this program.")
            elif not re.search(".txt", textfile):
                print("\n----You have not provided a filename with a .txt extension----")
            
        while loop3 == 1:
            text = np.array(text)
            text = text.tolist()
            for w in text:
                if w not in removal:
                    text2 = text2 + [w]
            text2 = [w.lower() for w in text2]
            digitfilter = [item for item in text2 if not item.isdigit()]
            read_text = list(digitfilter)
            loop = 0
            main_loop = 2
            loop3 = 0
    
    while main_loop == 2:
        data = np.array(read_text)
        
        data = [word for word in data if word not in stopwords.words('english')]
        
        d = Counter(data[np.isin(data, df.word)])
        
        pleasantness, activation, imagery = (0,0,0)
        count = len(data)
        tokens = len(set(data))
        richness = tokens / count
        fdist = nltk.FreqDist(data)
        
        for k,v in d.items():
            values = df.loc[df.word == k]
            pleasantness += values["pleasantness"].item()*v
            activation += values["activation"].item()*v
            imagery += values["imagery"].item()*v
        
        dict_count = sum(d.values())
        
        p_avg = pleasantness / dict_count
        a_avg = activation / dict_count
        i_avg = imagery / dict_count
        
        loop5 = 1
        while loop5 == 1:
            print("\n\n-----------------------------------------------------------\n")
            print("\nPlease choose which results you wish to view:")
            
            print("\n1) Basic information")
            print("2) Information regarding the rating according to Dictionary of Affect in Language")
            print("3) All of the above")
            
            print("\n4) The most common words")
    
            print("\n0) Stop and Exit")
        
            datachoice = input("Please enter your choice here: ")
            if datachoice == '1':  
                print("\n\n-----------------------------------------------------------\n")
                print("\nThe number of texts: ", no_of_docs)
                print("The total number of words: ", count)
                print("The number of unique tokens: ", tokens)
                print("The lexical richness: ", richness)
                loop7 = 1
                loop5 = 0
            elif datachoice == '2':
                print("\n\n-----------------------------------------------------------\n")
                print("\nThe total number of words: ", count)
                print("\nThe total number of words found in the Dictionary of Affect in Language: ", dict_count)
                print("The average pleasantness rating: ", p_avg)
                print("The average activation rating: ", a_avg)
                print("The average imagery rating: ", i_avg)
                loop7 = 1
                loop5 = 0
            elif datachoice == '3':
                print("\n\n-----------------------------------------------------------\n")
                print("\nThe number of texts: ", no_of_docs)
                print("The total number of words: ", count)
                print("The number of unique tokens: ", tokens)
                print("The lexical richness: ", richness)
                print("\nThe total number of words found in the Dictionary of Affect in Language: ", dict_count)
                print("The average pleasantness rating: ", p_avg)
                print("The average activation rating: ", a_avg)
                print("The average imagery rating: ", i_avg)
                loop7 = 1
                loop5 = 0
            elif datachoice == '4':               
                loop6 = 1
                loop5 = 0
                while loop6 == 1:
                    print("\n\n-----------------------------------------------------------\n")
                    print("\nPlease enter the number up to which you wish to see the most common words (i.e. 10, 50, 100, etc.)")
                    print("\nOr type 0 to return to the previous list of options.")
                    
                    number = int(input("\nPlease enter your number here: "))
                    if number is not None:
                        print("\n\n-----------------------------------------------------------\n")
                        print("\nThe ",number," most common words are: ", fdist.most_common(number))
                        loop7 = 1
                        loop6 = 0
                    elif number is None:
                        print("\nPlease enter a number.")
                    elif number == '0':
                        loop5 = 1
                        loop6 = 0
            elif datachoice == '0':
                sys.exit("\nProgram is stopping. Thank you for using this program.")
            else:
                print("\n----Incorrect input. Please just enter a single number matching the option of your choice.----")
        
        while loop7 == 1:
            print("\n\n-----------------------------------------------------------\n")
            print("\nWhat would you like to do now?")
            print("\n1) Get more/other data")
            print("2) Get data from different texts")
    
            print("\n0) Stop and Exit")
            
            continuechoice = input("Please enter your choice here: ")
            if continuechoice == '1':
                main_loop = 2
                loop5 = 1
                loop7 = 0
            elif continuechoice == '2':
                print("\n\n-----------------------------------------------------------\n\n")
                loop7 = 0
                main_loop = 1
            elif continuechoice == '0':
                sys.exit("\nProgram is stopping. Thank you for using this program.")
            else:
                print("\n----Incorrect input. Please just enter a single number matching the option of your choice----")
            
    while main_loop == 3:
        df = pd.read_csv('dictionary.csv')

        loop8 = 1
        textno = 0
        textinfo = []
        data = []
        text2 = []
        text = []
        category = 'ca'
        genre = 'pres_rep'
        genreno = int('1')
        
        while loop8 == 1:
            textno = textno + 1
            if category == 'ca':
                genre = 'press_rep'
                genreno = int('1')
            if category == 'cb':
                genre = 'press_ed'
                genreno = int('2')
            if category == 'cc':
                genre = 'press_rev'
                genreno = int('3')
            if category == 'cd':
                genre = 'religion'
                genreno = int('4')
            if category == 'ce':
                genre = 'skill_hob'
                genreno = int('5')
            if category == 'cf':
                genre = 'pop_lore'
                genreno = int('6')
            if category == 'cg':
                genre = 'bel_bio_mem'
                genreno = int('7')
            if category == 'ch':
                genre = 'misc'
                genreno = int('8')
            if category == 'cj':
                genre = 'learned'
                genreno = int('9')
            if category == 'ck':
                genre = 'gen_fic'
                genreno = int('10')
            if category == 'cl':
                genre = 'mys_det'
                genreno = int('11')
            if category == 'cm':
                genre = 'sci_fi'
                genreno = int('12')
            if category == 'cn':
                genre = 'adv_west'
                genreno = int('13')
            if category == 'cp':
                genre = 'rom_love'
                genreno = int('14')
            if category == 'cr':
                genre = 'humor'
                genreno = int('15')
            if 1 <= textno <= 9:
                file = str(category) + '0' + str(textno)
                text = brown.words(fileids=[file])
                
            if category == 'ca' and textno == 44:
                file = str(category) + str(textno)
                text = brown.words(fileids=[file])
                category = 'cb'
                textno = 0
            if category == 'cb' and textno == 27:
                file = str(category) + str(textno)
                text = brown.words(fileids=[file])
                category = 'cc'
                textno = 0
            if category == 'cc' and textno == 17:
                file = str(category) + str(textno)
                text = brown.words(fileids=[file])
                category = 'cd'
                textno = 0
            if category == 'cd' and textno == 17:
                file = str(category) + str(textno)
                text = brown.words(fileids=[file])
                category = 'ce'
                textno = 0
            if category == 'ce' and textno == 36:
                file = str(category) + str(textno)
                text = brown.words(fileids=[file])
                category = 'cf'
                textno = 0
            if category == 'cf' and textno == 48:
                file = str(category) + str(textno)
                text = brown.words(fileids=[file])
                category = 'cg'
                textno = 0
            if category == 'cg' and textno == 75:
                file = str(category) + str(textno)
                text = brown.words(fileids=[file])
                category = 'ch'
                textno = 0
            if category == 'ch' and textno == 30:
                file = str(category) + str(textno)
                text = brown.words(fileids=[file])
                category = 'cj'
                textno = 0
            if category == 'cj' and textno == 80:
                file = str(category) + str(textno)
                text = brown.words(fileids=[file])
                category = 'ck'
                textno = 0
            if category == 'ck' and textno == 29:
                file = str(category) + str(textno)
                text = brown.words(fileids=[file])
                category = 'cl'
                textno = 0
            if category == 'cl' and textno == 24:
                file = str(category) + str(textno)
                text = brown.words(fileids=[file])
                category = 'cm'
                textno = 0
            if category == 'cm' and textno == 6:
                file = str(category) + '0' + str(textno)
                text = brown.words(fileids=[file])
                category = 'cn'
                textno = 0
            if category == 'cn' and textno == 29:
                file = str(category) + str(textno)
                text = brown.words(fileids=[file])
                category = 'cp'
                textno = 0
            if category == 'cp' and textno == 29:
                file = str(category) + str(textno)
                text = brown.words(fileids=[file])
                category = 'cr'
                textno = 0
            if category == 'cr' and textno == 9:
                file = str(category) + '0' + str(textno)
                text = brown.words(fileids=[file])
                textno = 0
                loop8 = 0
                
            elif 10 <= textno <= 99:
                file = str(category) + str(textno)
                text = brown.words(fileids=[file])
          
            text = np.array(text)
            text = text.tolist()
            for w in text:
                if w not in removal:
                    text2 = text2 + [w]
            text2 = [w.lower() for w in text2]
            data = np.array(text2)
            
            data = [word for word in data if word not in stopwords.words('english')]
            data = np.array(data)
            
            count = len(data)
            tokens = len(set(data))
            richness = tokens / count
            
            d = Counter(data[np.isin(data, df.word)])
            d_anger = Counter(data[np.isin(data, df_anger.word)])
            d_anticip = Counter(data[np.isin(data, df_anticip.word)])
            d_disgust = Counter(data[np.isin(data, df_disgust.word)])
            d_fear = Counter(data[np.isin(data, df_fear.word)])
            d_joy = Counter(data[np.isin(data, df_joy.word)])
            d_neg = Counter(data[np.isin(data, df_neg.word)])
            d_pos = Counter(data[np.isin(data, df_pos.word)])
            d_sad = Counter(data[np.isin(data, df_sad.word)])
            d_surp = Counter(data[np.isin(data, df_surp.word)])
            d_trust = Counter(data[np.isin(data, df_trust.word)])
            
            word_1 = 1
            word_2 = 1
            word_af = 1
            word_also = 1
            word_american = 1
            word_another = 1
            word_arlene = 1
            word_around = 1
            word_back = 1
            word_bdikkat = 1
            word_business = 1
            word_came = 1
            word_car = 1
            word_christ = 1
            word_christian = 1
            word_church = 1
            word_come = 1
            word_could = 1
            word_day = 1
            word_development = 1
            word_door = 1
            word_ekstrohm = 1
            word_even = 1
            word_eyes = 1
            word_face = 1
            word_feed = 1
            word_first = 1
            word_fiscal = 1
            word_general = 1
            word_get = 1
            word_go = 1
            word_god = 1
            word_good = 1
            word_got = 1
            word_government = 1
            word_great = 1
            word_hal = 1
            word_helva = 1
            word_home = 1
            word_house = 1
            word_jack = 1
            word_jazz = 1
            word_know = 1
            word_last = 1
            word_life = 1
            word_like = 1
            word_line = 1
            word_little = 1
            word_long = 1
            word_looked = 1
            word_made = 1
            word_make = 1
            word_man = 1
            word_many = 1
            word_may = 1
            word_members = 1
            word_men = 1
            word_mercer = 1
            word_mike = 1
            word_mother = 1
            word_mr = 1
            word_mrs = 1
            word_much = 1
            word_music = 1
            word_must = 1
            word_never = 1
            word_new = 1
            word_number = 1
            word_old = 1
            word_one = 1
            word_people = 1
            word_power = 1
            word_president = 1
            word_program = 1
            word_public = 1
            word_right = 1
            word_said = 1
            word_school = 1
            word_see = 1
            word_shall = 1
            word_ship = 1
            word_spirit = 1
            word_state = 1
            word_states = 1
            word_still = 1
            word_system = 1
            word_tax = 1
            word_things = 1
            word_thought = 1
            word_three = 1
            word_time = 1
            word_two = 1
            word_united = 1
            word_us = 1
            word_use = 1
            word_used = 1
            word_war = 1
            word_water = 1
            word_way = 1
            word_week = 1
            word_well = 1
            word_went = 1
            word_work = 1
            word_world = 1
            word_would = 1
            word_year = 1
            word_years = 1
            
            for word in data:
                if word == '1':
                    word_1 = word_1 + 1
                elif word == '2':
                    word_2 = word_2 + 1
                elif word == 'af':
                    word_af = word_af + 1
                elif word == 'also':
                    word_also = word_also + 1
                elif word == 'american':
                    word_american = word_american + 1
                elif word == 'another':
                    word_another = word_another + 1
                elif word == 'arlene':
                    word_arlene = word_arlene + 1
                elif word == 'around':
                    word_around = word_around + 1
                elif word == 'back':
                    word_back = word_back + 1
                elif word == "b'dikkat":
                    word_bdikkat = word_bdikkat + 1
                elif word == 'business':
                    word_business = word_business + 1
                elif word == 'came':
                    word_came = word_came + 1
                elif word == 'car':
                    word_car = word_car + 1
                elif word == 'christ':
                    word_christ = word_christ + 1
                elif word == 'christian':
                    word_christian = word_christian + 1
                elif word == 'church':
                    word_church = word_church + 1
                elif word == 'come':
                    word_come = word_come + 1
                elif word == 'could':
                    word_could = word_could + 1
                elif word == 'day':
                    word_day = word_day + 1
                elif word == 'development':
                    word_development = word_development + 1
                elif word == 'door':
                    word_door = word_door + 1
                elif word == 'ekstrohm':
                    word_ekstrohm = word_ekstrohm + 1
                elif word == 'even':
                    word_even = word_even + 1
                elif word == 'eyes':
                    word_eyes = word_eyes + 1
                elif word == 'face':
                    word_face = word_face + 1
                elif word == 'feed':
                    word_feed = word_feed + 1
                elif word == 'first':
                    word_first = word_first + 1
                elif word == 'fiscal':
                    word_fiscal = word_fiscal + 1
                elif word == 'general':
                    word_general = word_general + 1
                elif word == 'get':
                    word_get = word_get + 1
                elif word == 'go':
                    word_go = word_go + 1
                elif word == 'god':
                    word_god = word_god + 1
                elif word == 'good':
                    word_good = word_good + 1
                elif word == 'got':
                    word_got = word_got + 1
                elif word == 'government':
                    word_government = word_government + 1
                elif word == 'great':
                    word_great = word_great + 1
                elif word == 'hal':
                    word_hal = word_hal + 1
                elif word == 'helva':
                    word_helva = word_helva + 1
                elif word == 'home':
                    word_home = word_home + 1
                elif word == 'house':
                    word_house = word_house + 1
                elif word == 'jack':
                    word_jack = word_jack + 1
                elif word == 'jazz':
                    word_jazz = word_jazz + 1
                elif word == 'know':
                    word_know = word_know + 1
                elif word == 'last':
                    word_last = word_last + 1
                elif word == 'life':
                    word_life = word_life + 1
                elif word == 'like':
                    word_like = word_like + 1
                elif word == 'line':
                    word_line = word_line + 1
                elif word == 'little':
                    word_little = word_little + 1
                elif word == 'long':
                    word_long = word_long + 1
                elif word == 'looked':
                    word_looked = word_looked + 1
                elif word == 'made':
                    word_made = word_made + 1
                elif word == 'make':
                    word_make = word_make + 1
                elif word == 'man':
                    word_man = word_man + 1
                elif word == 'many':
                    word_many = word_many + 1
                elif word == 'may':
                    word_may = word_may + 1
                elif word == 'members':
                    word_members = word_members + 1
                elif word == 'men':
                    word_men = word_men + 1
                elif word == 'mercer':
                    word_mercer = word_mercer + 1
                elif word == 'mike':
                    word_mike = word_mike + 1
                elif word == 'mother':
                    word_mother = word_mother + 1
                elif word == 'mr.':
                    word_mr = word_mr + 1
                elif word == 'mrs.':
                    word_mrs = word_mrs + 1
                elif word == 'much':
                    word_much = word_much + 1
                elif word == 'music':
                    word_music = word_music + 1
                elif word == 'must':
                    word_must = word_must + 1
                elif word == 'never':
                    word_never = word_never + 1
                elif word == 'new':
                    word_new = word_new + 1
                elif word == 'number':
                    word_number = word_number + 1
                elif word == 'old':
                    word_old = word_old + 1
                elif word == 'one':
                    word_one = word_one + 1
                elif word == 'people':
                    word_people = word_people + 1
                elif word == 'power':
                    word_power = word_power + 1
                elif word == 'president':
                    word_president = word_president + 1
                elif word == 'program':
                    word_program = word_program + 1
                elif word == 'public':
                    word_public = word_public + 1
                elif word == 'right':
                    word_right = word_right + 1
                elif word == 'said':
                    word_said = word_said + 1
                elif word == 'school':
                    word_school = word_school + 1
                elif word == 'see':
                    word_see = word_see + 1
                elif word == 'shall':
                    word_shall = word_shall + 1
                elif word == 'ship':
                    word_ship = word_ship + 1
                elif word == 'spirit':
                    word_spirit = word_spirit + 1
                elif word == 'state':
                    word_state = word_state + 1
                elif word == 'states':
                    word_states = word_states + 1
                elif word == 'still':
                    word_still = word_still + 1
                elif word == 'system':
                    word_system = word_system + 1
                elif word == 'tax':
                    word_tax = word_tax + 1
                elif word == 'things':
                    word_things = word_things + 1
                elif word == 'thought':
                    word_thought = word_thought + 1
                elif word == 'three':
                    word_three = word_three + 1
                elif word == 'time':
                    word_time = word_time + 1
                elif word == 'two':
                    word_two = word_two + 1
                elif word == 'united':
                    word_united = word_united + 1
                elif word == 'us':
                    word_us = word_us + 1
                elif word == 'use':
                    word_use = word_use + 1
                elif word == 'used':
                    word_used = word_used + 1
                elif word == 'war':
                    word_war = word_war + 1
                elif word == 'water':
                    word_water = word_water + 1
                elif word == 'way':
                    word_way = word_way + 1
                elif word == 'week':
                    word_week = word_week + 1
                elif word == 'well':
                    word_well = word_well + 1
                elif word == 'went':
                    word_went = word_went + 1
                elif word == 'work':
                    word_work = word_work + 1
                elif word == 'world':
                    word_world = word_world + 1
                elif word == 'would':
                    word_would = word_would + 1
                elif word == 'year':
                    word_year = word_year + 1
                elif word == 'years':
                    word_years = word_years + 1
            
            pleasantness, activation, imagery = (0,0,0)
            
            for k,v in d.items():
                values = df.loc[df.word == k]
                pleasantness += values["pleasantness"].item()*v
                activation += values["activation"].item()*v
                imagery += values["imagery"].item()*v
            
            dict_count = sum(d.values())
            
            p_avg = pleasantness / dict_count
            a_avg = activation / dict_count
            i_avg = imagery / dict_count
            
            genre = [genre]
            genreno = [genreno]
            filename = [file]
            count = [count]
            tokens = [tokens]
            richness = [richness]
            
            dict_count = [dict_count]
            p_avg = [p_avg]
            a_avg = [a_avg]
            i_avg = [i_avg]    
            
            anger = [sum(d_anger.values()) / len(data)]
            anticipation = [sum(d_anticip.values()) / len(data)]
            disgust = [sum(d_disgust.values()) / len(data)]
            fear = [sum(d_fear.values()) / len(data)]
            joy = [sum(d_joy.values()) / len(data)]
            negative = [sum(d_neg.values()) / len(data)]
            positive = [sum(d_pos.values()) / len(data)]
            sadness = [sum(d_sad.values()) / len(data)]
            surprise = [sum(d_surp.values()) / len(data)]
            trust = [sum(d_trust.values()) / len(data)]
            
            word_1 = [word_1]
            word_2 = [word_2]
            word_af = [word_af]
            word_also = [word_also]
            word_american = [word_american]
            word_another = [word_another]
            word_arlene = [word_arlene]
            word_around = [word_around]
            word_back = [word_back]
            word_bdikkat = [word_bdikkat]
            word_business = [word_business]
            word_came = [word_came]
            word_car = [word_car]
            word_christ = [word_christ]
            word_christian = [word_christian]
            word_church = [word_church]
            word_come = [word_come]
            word_could = [word_could]
            word_day = [word_day]
            word_development = [word_development]
            word_door = [word_door]
            word_ekstrohm = [word_ekstrohm]
            word_even = [word_even]
            word_eyes = [word_eyes]
            word_face = [word_face]
            word_feed = [word_feed]
            word_first = [word_first]
            word_fiscal = [word_fiscal]
            word_general = [word_general]
            word_get = [word_get]
            word_go = [word_go]
            word_god = [word_god]
            word_good = [word_good]
            word_got = [word_got]
            word_government = [word_government]
            word_great = [word_great]
            word_hal = [word_hal]
            word_helva = [word_helva]
            word_home = [word_home]
            word_house = [word_house]
            word_jack = [word_jack]
            word_jazz = [word_jazz]
            word_know = [word_know]
            word_last = [word_last]
            word_life = [word_life]
            word_like = [word_like]
            word_line = [word_line]
            word_little = [word_little]
            word_long = [word_long]
            word_looked = [word_looked]
            word_made = [word_made]
            word_make = [word_make]
            word_man = [word_man]
            word_many = [word_many]
            word_may = [word_may]
            word_members = [word_members]
            word_men = [word_men]
            word_mercer = [word_mercer]
            word_mike = [word_mike]
            word_mother = [word_mother]
            word_mr = [word_mr]
            word_mrs = [word_mrs]
            word_much = [word_much]
            word_music = [word_music]
            word_must = [word_must]
            word_never = [word_never]
            word_new = [word_new]
            word_number = [word_number]
            word_old = [word_old]
            word_one = [word_one]
            word_people = [word_people]
            word_power = [word_power]
            word_president = [word_president]
            word_program = [word_program]
            word_public = [word_public]
            word_right = [word_right]
            word_said = [word_said]
            word_school = [word_school]
            word_see = [word_see]
            word_shall = [word_shall]
            word_ship = [word_ship]
            word_spirit = [word_spirit]
            word_state = [word_state]
            word_states = [word_states]
            word_still = [word_still]
            word_system = [word_system]
            word_tax = [word_tax]
            word_things = [word_things]
            word_thought = [word_thought]
            word_three = [word_three]
            word_time = [word_time]
            word_two = [word_two]
            word_united = [word_united]
            word_us = [word_us]
            word_use = [word_use]
            word_used = [word_used]
            word_war = [word_war]
            word_water = [word_water]
            word_way = [word_way]
            word_week = [word_week]
            word_well = [word_well]
            word_went = [word_went]
            word_work = [word_work]
            word_world = [word_world]
            word_would = [word_would]
            word_year = [word_year]
            word_years = [word_years]
            
            textinfo = textinfo + [genre + genreno + filename + count + tokens + richness + p_avg + a_avg + i_avg + dict_count + anger + anticipation + disgust + fear + joy + negative + positive + sadness + surprise + trust + word_1 + word_2 + word_af + word_also + word_american + word_another + word_arlene + word_around + word_back + word_bdikkat + word_business + word_came + word_car + word_christ + word_christian + word_church + word_come + word_could + word_day + word_development + word_door + word_ekstrohm + word_even + word_eyes + word_face + word_feed + word_first + word_fiscal + word_general + word_get + word_go + word_god + word_good + word_got + word_government + word_great + word_hal + word_helva + word_home + word_house + word_jack + word_jazz + word_know + word_last + word_life + word_like + word_line + word_little + word_long + word_looked + word_made + word_make + word_man + word_many + word_may + word_members + word_men + word_mercer + word_mike + word_mother + word_mr + word_mrs + word_much + word_music + word_must + word_never + word_new + word_number + word_old + word_one + word_people + word_power + word_president + word_program + word_public + word_right + word_said + word_school + word_see + word_shall + word_ship + word_spirit + word_state + word_states + word_still + word_system + word_tax + word_things + word_thought + word_three + word_time + word_two + word_united + word_us + word_use + word_used + word_war + word_water + word_way + word_week + word_well + word_went + word_work + word_world + word_would + word_year + word_years]
            
            text2 = []
            data = []

        textinfo = [['genre', 'genreno', 'filename', 'count', 'tokens', 'richness', 'pleasantness', 'activation', 'imagery', 'dict_count', 'anger', 'anticipation', 'disgust', 'fear', 'joy', 'negative', 'positive', 'sadness', 'surprise', 'trust', 'word_1', 'word_2', 'word_af', 'word_also', 'word_american', 'word_another', 'word_arlene', 'word_around', 'word_back', 'word_bdikkat', 'word_business', 'word_came', 'word_car', 'word_christ', 'word_christian', 'word_church', 'word_come', 'word_could', 'word_day', 'word_development', 'word_door', 'word_ekstrohm', 'word_even', 'word_eyes', 'word_face', 'word_feed', 'word_first', 'word_fiscal', 'word_general', 'word_get', 'word_go', 'word_god', 'word_good', 'word_got', 'word_government',  'word_great',  'word_hal', 'word_helva', 'word_home', 'word_house', 'word_jack', 'word_jazz', 'word_know', 'word_last', 'word_life', 'word_like', 'word_line', 'word_little', 'word_long', 'word_looked', 'word_made', 'word_make', 'word_man','word_many', 'word_may', 'word_members', 'word_men', 'word_mercer', 'word_mike', 'word_mother', 'word_mr', 'word_mrs', 'word_much', 'word_music', 'word_must', 'word_never', 'word_new', 'word_number', 'word_old', 'word_one', 'word_people', 'word_power', 'word_president', 'word_program', 'word_public', 'word_right', 'word_said', 'word_school', 'word_see', 'word_shall', 'word_ship', 'word_spirit', 'word_state', 'word_states', 'word_still', 'word_system', 'word_tax', 'word_things', 'word_thought', 'word_three', 'word_time', 'word_two', 'word_united', 'word_us', 'word_use', 'word_used', 'word_war', 'word_water', 'word_way', 'word_week', 'word_well', 'word_went', 'word_work', 'word_world', 'word_would', 'word_year', 'word_years']] + textinfo

        datacsv = open('CollectionData.csv', 'w', newline = '')

        with datacsv:
            writer = csv.writer(datacsv)
            for row in textinfo:
                writer.writerow(row)

        print("\n\n-----------------------------------------------------------\n")
        print("\nThe file has been outputted to the folder in which the python file is located. Returning to the main menu in a few seconds.")
        print("\n\n-----------------------------------------------------------\n")
        main_loop = 0